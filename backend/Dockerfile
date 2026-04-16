# Usa una imagen oficial de Python
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Instalación de dependencias básicas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia del código
COPY . .

# Comando para iniciar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]