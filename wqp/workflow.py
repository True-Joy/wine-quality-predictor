import sys
import logging

from wqp.ml import build_wine_predictor_model
from wqp.evaluation import compute_model_metrics
from wqp.data_access import fetch_csv_data, build_train_test_sets

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('wqp.main')


def model_training_workflow(data_path: str):
    """
    This functions orchestrates the whole training script, as distinct steps:
    - fetching input data
    - splitting them into train and test datasets
    - definning the model
    - fitting the model on the training data
    - evaluating the model on the test data
    :param data_path: a string containing the location of the training data 

    """

    raise NotImplementedException()