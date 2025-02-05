import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
import joblib

numeric_features = [
  'latitude', 'longitude', 'minimo_noites', 'numero_de_reviews',
  'reviews_por_mes', 'calculado_host_listings_count', 'disponibilidade_365',
  'dias_desde_ultima_review', 'coord_interaction', 'coord_sum', 
  'reviews_per_availability', 'listing_efficiency', 'price_per_night',
  'reviews_squared', 'noites_squared', 'disponibilidade_squared',
  'location_availability', 'reviews_availability', 'reviews_noites',
  'disponibilidade_ratio', 'ocupacao_estimada'
]
categorical_features = ['bairro_group', 'bairro', 'room_type']

def create_features(df):
   df = df.copy()
   df['ultima_review'] = pd.to_datetime(df['ultima_review'])
   df['dias_desde_ultima_review'] = (pd.Timestamp.now() - df['ultima_review']).dt.days
   df['dias_desde_ultima_review'] = df['dias_desde_ultima_review'].fillna(0)
   df['coord_interaction'] = df['latitude'] * df['longitude']
   df['coord_sum'] = df['latitude'] + df['longitude']
   df['reviews_por_mes'] = df['reviews_por_mes'].fillna(0)
   df['reviews_per_availability'] = df['numero_de_reviews'] / (df['disponibilidade_365'] + 1)
   df['listing_efficiency'] = df['numero_de_reviews'] / (df['calculado_host_listings_count'] + 1)
   df['price_per_night'] = 0  # Adicionar valor default
   df['reviews_squared'] = df['numero_de_reviews'] ** 2
   df['noites_squared'] = df['minimo_noites'] ** 2
   df['disponibilidade_squared'] = df['disponibilidade_365'] ** 2
   df['location_availability'] = df['coord_interaction'] * df['disponibilidade_365']
   df['reviews_availability'] = df['numero_de_reviews'] * df['disponibilidade_365']
   df['reviews_noites'] = df['numero_de_reviews'] * df['minimo_noites']
   df['disponibilidade_ratio'] = df['disponibilidade_365'] / 365
   df['ocupacao_estimada'] = 1 - df['disponibilidade_ratio']
   return df

def prepare_new_data(sample):
   df = pd.DataFrame([sample])
   df = create_features(df)
   X = df[numeric_features + categorical_features]
   X[numeric_features] = scaler.transform(X[numeric_features])
   return X

novo_apartamento = {
   'id': 2595,
 'nome': 'Skylit Midtown Castle',
 'host_id': 2845,
 'host_name': 'Jennifer',
 'bairro_group': 'Manhattan',
 'bairro': 'Midtown',
 'latitude': 40.75362,
 'longitude': -73.98377,
 'room_type': 'Entire home/apt',
 'minimo_noites': 1,
 'numero_de_reviews': 45,
 'ultima_review': '2019-05-21',
 'reviews_por_mes': 0.38,
 'calculado_host_listings_count': 2,
 'disponibilidade_365': 355
}

model = CatBoostRegressor()
model.load_model('catboost_model.cbm')
scaler = joblib.load('scaler.pkl')

X_new = prepare_new_data(novo_apartamento)
preco_log = model.predict(X_new)
preco_final = np.expm1(preco_log) * 10

print(f"Preço sugerido: ${float(preco_final[0]):.2f}")