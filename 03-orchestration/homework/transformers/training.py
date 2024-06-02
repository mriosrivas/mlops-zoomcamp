from typing import List, Tuple

from pandas import DataFrame, Series
from sklearn.feature_extraction import DictVectorizer
from sklearn.base import BaseEstimator

from mlops.homework.utils.data_preparation.encoders import vectorize_features
from mlops.homework.utils.data_preparation.feature_selection import select_features

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(
    data: DataFrame, **kwargs
# ) -> Tuple[
#     DictVectorizer,
#     BaseEstimator,
# ]:
) -> DictVectorizer:
    print("Hello")
    df = data
    target = kwargs.get('target', 'duration')

    X, _, dv = vectorize_features(select_features(df))
    y: Series = df[target]

    # X_train, X_val, dv = vectorize_features(
    #     select_features(df_train),
    #     select_features(df_val),
    # )
    # y_train = df_train[target]
    # y_val = df_val[target]

    return data


