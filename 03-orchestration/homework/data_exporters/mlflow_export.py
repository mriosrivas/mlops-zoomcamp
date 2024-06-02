from typing import List, Tuple

import mlflow
import pickle

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    vec_filename = 'dict_vectorizer.pkl'
    with open(vec_filename, 'wb') as f:
        pickle.dump(data[0], f)

    model_filename = 'model.pkl'
    with open(model_filename, 'wb') as f:
        pickle.dump(data[1], f)

    mlflow.set_tracking_uri("http://mlflow:5000/")
    mlflow.set_experiment("nyc-taxi-experiment")

    try:
        mlflow.end_run()
    except:
        pass

    with mlflow.start_run():
        mlflow.log_artifact(vec_filename)
        mlflow.log_artifact(model_filename)
        #mlflow.sklearn.save_model(data[1], "models")# Specify your data exporting logic here
