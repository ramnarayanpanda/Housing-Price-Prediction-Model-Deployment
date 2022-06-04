import typing as t
from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from regression_model import __version__ as _version
from regression_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: str) -> pd.DataFrame:
    # print('\n\n', f"file name: {DATASET_DIR}/{file_name}", '\n\n')
    dataframe = pd.read_csv(Path(f"{DATASET_DIR}/{file_name}"))
    dataframe["MSSubClass"] = dataframe["MSSubClass"].astype("O")

    # rename variables with numbers to avoid syntax error later
    transformed = dataframe.rename(columns=config.model_config.variables_to_rename)
    return transformed


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    """Persist the pipeline.
    Saves the versioned model, and overwrites any previous saved models.
    This ensures that when the pacakge is published,
    there is only one trained model that can be called"""

    # Prepare versioned save file name
    save_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
    save_path = TRAINED_MODEL_DIR / save_file_name

    remove_old_pipelines(files_to_keep=[save_file_name])
    joblib.dump(pipeline_to_persist, save_path)


def load_pipeline(*, file_name: str) -> Pipeline:
    """Load a persisted Pipeline"""

    file_path = TRAINED_MODEL_DIR / file_name
    trained_model = joblib.load(filename=file_path)
    return trained_model


def remove_old_pipelines(*, files_to_keep: t.List[str]) -> None:
    """Remove old pipelines.
    This is to ensure there is a simple one-to-one mapping
    between the package version and the model version to be imported
    and used by other applications."""
    do_not_delete = files_to_keep + ["__init__.py"]
    for model_file in TRAINED_MODEL_DIR.iterdir():
        if model_file.name not in do_not_delete:
            model_file.unlink()


# pytest will run all the modules inside a direc which starts with  "test"
# Features of "pytest"
# Detailed info on failing assert statements (no need to remember self.assert*names)
# Auto discover of test modules and functions (modules start with the prefix test)
# Modular fixtures for managing small or parameterized long lived test resources.
# Can run unittest (including trial) and nose test test suites out of te box
# ------------- Backward compatible ------------


# Fixtures:
# Eg: Suppose you have a database, you are trying to connect to it and check the employees id,
# so you can write a different functions for each employee, where you can connect to databse and check id
# But this code will repetitive and as for each employee you are trying to connect to the DB the connection time is costly
# To avoid this you can use things like, make a global variable and store the connection and cusrsor to the DB in those global variables
# This is the traditional way of doing this.

# But with fixtures you can do the same thing with out maintaining gloabl variables
# if you dont mention scope='module' then the fixture will call every time you want to check
# @pytest.fixtures(scope='module)
# def connect_db():
#     con = db.connect()
#     cur = db.cursor()
#     return cur
#
# def toms_id_check(connect_db):
#     assert connect_db('select id from tab where name='Tom') == 123
#
# def pams_id_check(connect_db):
#     assert connect_db('select id from tab where name='Pam') == 789


# Another eg with fixtures:
