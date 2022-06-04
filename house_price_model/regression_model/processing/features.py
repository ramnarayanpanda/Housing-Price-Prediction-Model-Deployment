# This module contains some custom feature transformers
# To test this features.py file we also have a test module check that out
from typing import List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
    """This will return time difference in years between
    reference variable and each column/variable in variables list"""

    def __init__(self, variables: List[str], reference_variable: str):

        if not isinstance(variables, list):
            raise ValueError("Variables must be a list")

        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]

        return X


class Mapper(BaseEstimator, TransformerMixin):
    """Categorical variable mapper"""

    def __init__(self, variables: List[str], mappings: dict):

        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables
        self.mappings = mappings

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X
