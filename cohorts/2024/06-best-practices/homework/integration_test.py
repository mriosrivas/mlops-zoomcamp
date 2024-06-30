import pandas as pd
import os
from datetime import datetime


def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


def get_input_path(year, month):
    input_pattern = os.getenv("INPUT_FILE_PATTERN", None)
    return input_pattern.format(year=year, month=month)


def main():
    year = 2023
    month = 1

    input_file = get_input_path(year, month)

    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),
    ]

    columns = [
        "PULocationID",
        "DOLocationID",
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
    ]

    df = pd.DataFrame(data, columns=columns)

    s3_endpoint = os.getenv("S3_ENDPOINT_URL", None)
    print(f"S3 endoint: {s3_endpoint}")

    options = {"client_kwargs": {"endpoint_url": s3_endpoint}}

    df.to_parquet(
        input_file,
        engine="pyarrow",
        compression=None,
        index=False,
        storage_options=options,
    )


if __name__ == "__main__":
    main()
