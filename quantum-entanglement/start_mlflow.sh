#! /bin/bash

mlflow server --backend-store-uri "file://${HOME}/mlflow/backend" \
    --default-artifact-root "file://${HOME}/mlflow/artifacts" \
    --port 5000