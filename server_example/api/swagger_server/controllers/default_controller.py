import connexion
import six

from swagger_server.models.configuration import Configuration  # noqa: E501
from swagger_server.models.dataset import Dataset  # noqa: E501
from swagger_server.models.dataset_metadata import DatasetMetadata  # noqa: E501
from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.model_metadata import ModelMetadata  # noqa: E501
from swagger_server.models.predict_input import PredictInput  # noqa: E501
from swagger_server.models.predict_results import PredictResults  # noqa: E501
from swagger_server.models.train import Train  # noqa: E501
from swagger_server.models.train_results import TrainResults  # noqa: E501
from swagger_server import util


def add_configuration(body):  # noqa: E501
	"""Add a new configuration

	 # noqa: E501

	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Configuration.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def add_dataset(body):  # noqa: E501
	"""Add a new dataset

	 # noqa: E501

	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Dataset.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def add_model(body):  # noqa: E501
	"""Add a new model

	 # noqa: E501

	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Model.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def get_configuration(configurationId):  # noqa: E501
	"""Get a Configuration

	 # noqa: E501

	:param configurationId: ID of model to get
	:type configurationId: int

	:rtype: Configuration
	"""
	return 'do some magic!'


def get_configurations():  # noqa: E501
	"""Get metadata about all configurations

	 # noqa: E501


	:rtype: List[Configuration]
	"""
	return 'do some magic!'


def get_data_set():  # noqa: E501
	"""Get all metadata

	 # noqa: E501


	:rtype: List[DatasetMetadata]
	"""
	return 'do some magic!'


def get_model(modelId):  # noqa: E501
	"""Get a Model

	 # noqa: E501

	:param modelId: ID of model to get
	:type modelId: int

	:rtype: Model
	"""
	print("coin")
	return 'do some magic!'


def get_models():  # noqa: E501
	"""Get all metadata about models available

	 # noqa: E501


	:rtype: List[ModelMetadata]
	"""
	print("coins")
	return 'do some magic!'


def predict_configuration(configurationId, body):  # noqa: E501
	"""predict using a configuration with the provided inputs

	 # noqa: E501

	:param configurationId: ID of model to get
	:type configurationId: int
	:param body: 
	:type body: dict | bytes

	:rtype: PredictResults
	"""
	if connexion.request.is_json:
		body = PredictInput.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def train_configuration(configurationId, body):  # noqa: E501
	"""train a given configuration with the provided parameters

	 # noqa: E501

	:param configurationId: ID of model to get
	:type configurationId: int
	:param body: 
	:type body: dict | bytes

	:rtype: TrainResults
	"""
	if connexion.request.is_json:
		body = Train.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def update_configuration(configurationId, body):  # noqa: E501
	"""Update configuration

	 # noqa: E501

	:param configurationId: ID of model to get
	:type configurationId: int
	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Configuration.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def update_dataset(body):  # noqa: E501
	"""Update dataset

	 # noqa: E501

	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Dataset.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def update_model(modelId, body):  # noqa: E501
	"""Update model

	 # noqa: E501

	:param modelId: ID of model to get
	:type modelId: int
	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Model.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
