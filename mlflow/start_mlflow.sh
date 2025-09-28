ROOT=`dirname $PWD`
mlflow server \
    --backend-store-uri sqlite:///${ROOT}/mlflow/mlruns.db \
    --registry-store-uri sqlite:///${ROOT}/mlflow/mlruns.db \
    --default-artifact-root /${ROOT}/mlflow/mlartifacts
