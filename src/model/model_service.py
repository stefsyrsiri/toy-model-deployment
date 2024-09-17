# 1. pick up model
#   1.1. if config file exists, load the trained model
#   1.2. if config file DOES not exist -> train model to get it
# 2. make predictions

"""
This module provides functionality for managing an ML model.

It contains the ModelService class, which handles loading and using
a pre-trained ML model. The class offers methods to load a model
from a file, building it if it doesn't exist, and to make predictions
using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService:
    """
    A service class for managing the ML model.

    This class provides functionalities to load a ML model from
    a specified path, build it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.

    Methods:
        __init__: Constructor that initializes the ModelService.
        load_model: Loads the model from file or builds it if it doesn't exist.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelService with no model loaded."""
        self.model = None

    def load_model(self) -> None:
        """Load the model from a specified path, or build it if not exist."""
        model_path = Path(
            f'{model_settings.model_path}/'
            f'{model_settings.model_name}',
            )

        logger.info(
            f'checking the existence of '
            f'model config file at {model_path}',
            )

        if not model_path.exists():
            logger.info(
                f'model at {model_path} was not found -> '
                f'building {model_settings.model_name}',
                )
            build_model()

        logger.info(
            f'model {model_settings.model_name} exists! -> '
            f'loading model configuration file',
            )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_args: list) -> list:
        """
        Make a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a pickle file.

        Args:
            input_args (list): The input data for making a prediction.

        Returns:
            list: The prediction result from the model.
        """
        logger.info('making prediction!')
        return self.model.predict([input_args])
