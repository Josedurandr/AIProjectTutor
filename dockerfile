# Usa una imagen base de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /AIProjectTutor

# Copia los archivos de requerimientos y las rutas a la imagen
COPY requirements.txt /AIProjectTutor/requirements.txt
COPY routes/ /AIProjectTutor/routes/
COPY APP /AIProjectTutor/app.py


# Instala las dependencias de Python
RUN pip install -r requirements.txt

# Expon el puerto 80 para FastAPI
EXPOSE 80

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
