import typing as t

import numpy as np
import pandas as pd

from regression_model import __version__ as _version
from regression_model.config.core import config
from regression_model.processing.data_manager import load_pipeline
from regression_model.processing.validation import validate_inputs

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)





just_check = [
    {
      "Alley": "string",
      "BedroomAbvGr": 0,
      "BldgType": "string",
      "BsmtCond": "string",
      "BsmtExposure": "string",
      "BsmtFinSF1": 0,
      "BsmtFinSF2": 0,
      "BsmtFinType1": "string",
      "BsmtFinType2": "string",
      "BsmtFullBath": 0,
      "BsmtHalfBath": 0,
      "BsmtQual": "string",
      "BsmtUnfSF": 0,
      "CentralAir": "string",
      "Condition1": "string",
      "Condition2": "string",
      "Electrical": "string",
      "EnclosedPorch": 0,
      "ExterCond": "string",
      "ExterQual": "string",
      "Exterior1st": "string",
      "Exterior2nd": "string",
      "Fence": "string",
      "FireplaceQu": "string",
      "Fireplaces": 0,
      "Foundation": "string",
      "FullBath": 0,
      "Functional": "string",
      "GarageArea": 0,
      "GarageCars": 0,
      "GarageCond": "string",
      "GarageFinish": "string",
      "GarageQual": "string",
      "GarageType": "string",
      "GarageYrBlt": 0,
      "GrLivArea": 0,
      "HalfBath": 0,
      "Heating": "string",
      "HeatingQC": "string",
      "HouseStyle": "string",
      "Id": 0,
      "KitchenAbvGr": 0,
      "KitchenQual": "string",
      "LandContour": "string",
      "LandSlope": "string",
      "LotArea": 0,
      "LotConfig": "string",
      "LotFrontage": 0,
      "LotShape": "string",
      "LowQualFinSF": 0,
      "MSSubClass": 0,
      "MSZoning": "string",
      "MasVnrArea": 0,
      "MasVnrType": "string",
      "MiscFeature": "string",
      "MiscVal": 0,
      "MoSold": 0,
      "Neighborhood": "string",
      "OpenPorchSF": 0,
      "OverallCond": 0,
      "OverallQual": 0,
      "PavedDrive": "string",
      "PoolArea": 0,
      "PoolQC": "string",
      "RoofMatl": "string",
      "RoofStyle": "string",
      "SaleCondition": "string",
      "SaleType": "string",
      "ScreenPorch": 0,
      "Street": "string",
      "TotRmsAbvGrd": 0,
      "TotalBsmtSF": 0,
      "Utilities": "string",
      "WoodDeckSF": 0,
      "YearBuilt": 0,
      "YearRemodAdd": 0,
      "YrSold": 0,
      "FirstFlrSF": 0,
      "SecondFlrSF": 0,
      "ThreeSsnPortch": 0
    }
  ]






def make_prediction(*, input_data: t.Union[pd.DataFrame, dict]) -> dict:
# def make_prediction():
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    
    # data = pd.DataFrame(just_check)
    
    # print('\n\n\n', 'Checking for data validation')
    # print(data[data['LotFrontage']<=0])
    # print(data[data['FirstFlrSF']<=0])
    # print(data[data['GrLivArea']<=0])
    # print('\n\n\n')
    
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = _price_pipe.predict(
            X=validated_data[config.model_config.features]
        )

        results = {
            "predictions": [np.exp(pred) for pred in predictions],  # type: ignore
            "version": _version,
            "errors": errors,
        }
    return results


# make_prediction()