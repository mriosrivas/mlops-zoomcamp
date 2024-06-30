#!/bin/bash

export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=""

export INPUT_FILE_PATTERN="s3://nyc-duration-/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration-/out/{year:04d}-{month:02d}.parquet"
#export S3_ENDPOINT_URL="http://localhost:4566"
unset S3_ENDPOINT_URL

echo "All variables set!"
echo "S3_ENDPOINT_URL=$S3_ENDPOINT_URL"
