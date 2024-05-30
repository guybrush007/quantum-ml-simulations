alias helm="microk8s helm"

# Install Airflow
helm repo add apache-airflow https://airflow.apache.org

export SSH_PRIVATE_KEY=$(base64 ~/.ssh/id_ed25519 -w 0) 
helm upgrade airflow apache-airflow/airflow  --values values_airflow.yaml --namespace airflow --create-namespace --install

# Install Postgres
helm repo add bitnami https://charts.bitnami.com/bitnami 
helm upgrade postgres bitnami/postgresql --namespace airflow --create-namespace --install --values values_postgres.yaml

# Install MLFlow
helm upgrade --install mlflow community-charts/mlflow --namespace mlflow  --create-namespace  --values values_mlflow.yaml
