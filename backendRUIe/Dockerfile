#imagen a instalar
FROM python:3.9

#creamos el directorio de trabajo
RUN mkdir -p /usr/src/backendRUIe

#usamos el directorio de trabajo
WORKDIR /usr/src/backendRUIe

#ESTABLECER VARIABLES DEL ENTORNO 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#ACTUALIZAR PIP
RUN pip install --upgrade pip
#actualizar e instalar mysql
RUN apt-get update && apt-get install -y gcc libpq-dev python3-dev musl-dev
#Copiar los requisitos del sistema
COPY ./req.txt ./
#instalar dependencias 
RUN pip install -r req.txt
#se crea el directorio para archivos de django
RUN mkdir /usr/src/backendRUIe/staticfiles

#Copiar el proyecto entero
COPY . .
#se ejecuta el archivo
#ENTRYPOINT ["/usr/src/django_proj/entrypoint.sh"]