FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "wevioo_doc", "/bin/bash", "-c"]

COPY . .

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000