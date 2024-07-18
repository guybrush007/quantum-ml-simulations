# Stage 1: Install dependencies
FROM jupyter/base-notebook:x86_64-python-3.11.6 AS dependencies

# Copy requirements and constraints files
COPY ./requirements-image.txt ./
COPY ./constraints-3.11.txt ./

# Install dependencies
RUN pip install -r requirements-image.txt --constraint constraints-3.11.txt

# Stage 2: Build final image
FROM jupyter/base-notebook:x86_64-python-3.11.6

# Copy installed dependencies from the previous stage
COPY --from=dependencies /opt/conda /opt/conda

# Copy the necessary files
COPY --chown=jovyan:users ./notebooks/*.ipynb /home/jovyan/
COPY --chown=jovyan:users ./notebooks/*.py /home/jovyan/
RUN mkdir /home/jovyan/simulated_data
COPY --chown=jovyan:users ./notebooks/simulated_data/* /home/jovyan/simulated_data
