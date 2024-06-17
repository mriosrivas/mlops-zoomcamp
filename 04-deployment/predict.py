import pickle

from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

with open("model.bin", "rb") as f_in:
    (dv, model) = pickle.load(f_in)


categorical = ["PULocationID", "DOLocationID"]


def read_data(filename):
    df = pd.read_parquet(filename)

    df["duration"] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df["duration"] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype("int").astype("str")

    return df


def prepare_features(year, month):
    df = read_data(
        f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"
    )
    dicts = df[categorical].to_dict(orient="records")
    features = dv.transform(dicts)
    return features


def predict(features):
    preds = model.predict(features)
    return preds  # float(preds[0])


# # if __name__ == "main":
# year = "2023"
# month = "04"
# features = prepare_features(year, month)
# preds = predict(features)
# print(f"PREDS STD: {np.std(preds)}")


app = Flask("duration-prediction")


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json()
    print(f"DATA: {data}")
    year = data["year"]
    month = data["month"]

    print(f"Year: {year}")
    print(f"Month: {month}")

    features = prepare_features(year, month)
    preds = predict(features)

    # result = {"duration": preds}

    # print(f"PREDS STD: {np.std(preds)}")

    result = {"duration_std": str(np.std(preds)), "duration_mean": str(np.mean(preds))}

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
