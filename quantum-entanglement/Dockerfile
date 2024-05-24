FROM jupyter/base-notebook:x86_64-python-3.11.6

COPY  ./requirements-image.txt ./
COPY --chown=jovyan:users ./notebooks/*.ipynb /home/jovyan/
COPY --chown=jovyan:users ./notebooks/*.py /home/jovyan/
RUN mkdir simulated_data
COPY --chown=jovyan:users ./notebooks/simulated_data/* /home/jovyan/simulated_data
RUN pip install -r requirements-image.txt