# Predição de Preços de Imóveis em NY 🏠

## Sobre o Projeto
Sistema de predição de preços de imóveis em Nova York baseado em características como localização, tipo de quarto e métricas de reviews. Desenvolvido com Python e recursos de análise de dados.

## Como Usar

### Instalação
```bash
# Clone o repositório
git clone https://github.com/lucas-ponte-e-silva/projeto.git
cd nome-do-repo

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Exemplo de Uso
```python
# Exemplo de dados de um imóvel para predição
dados = {
    'id': 2595,
    'nome': 'Skylit Midtown Castle',
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

# Para fazer uma predição, execute:
python predict.py
```

## Estrutura do Projeto
```
projeto/
├── predict.py            # Script principal de predição
├── requirements.txt      # Dependências do projeto
├── catboost_model.cbm   # Modelo treinado
└── scaler.pkl           # Normalizador de dados
```

## Requirements.txt
```
pandas==2.0.3
numpy==1.24.3
catboost==1.2
joblib==1.3.2
```

## Características dos Imóveis
Para fazer uma predição, você precisa fornecer:
- **nome**: Nome do imóvel
- **host_name**: Nome do anfitrião
- **bairro_group**: Região (Manhattan, Brooklyn, etc.)
- **bairro**: Bairro específico
- **latitude/longitude**: Coordenadas do imóvel
- **room_type**: Tipo de quarto
- **minimo_noites**: Mínimo de noites para reserva
- **numero_de_reviews**: Quantidade de avaliações
- **ultima_review**: Data da última avaliação
- **reviews_por_mes**: Média de avaliações por mês
- **calculado_host_listings_count**: Número de imóveis do anfitrião
- **disponibilidade_365**: Dias disponíveis no ano

## Autor
Lucas Ponte e Silva
