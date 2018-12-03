# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.configuration import Configuration  # noqa: E501
from swagger_server.models.dataset import Dataset  # noqa: E501
from swagger_server.models.dataset_metadata import DatasetMetadata  # noqa: E501
from swagger_server.models.model import Model  # noqa: E501
from swagger_server.models.model_metadata import ModelMetadata  # noqa: E501
from swagger_server.models.predict_input import PredictInput  # noqa: E501
from swagger_server.models.predict_results import PredictResults  # noqa: E501
from swagger_server.models.train import Train  # noqa: E501
from swagger_server.models.train_results import TrainResults  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
	"""DefaultController integration test stubs"""

	def test_add_configuration(self):
		"""Test case for add_configuration

		Add a new configuration
		"""
		body = Configuration()
		response = self.client.open(
			'/v1/configuration',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_add_dataset(self):
		"""Test case for add_dataset

		Add a new dataset
		"""
		body = Dataset()
		response = self.client.open(
			'/v1/data',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_add_model(self):
		"""Test case for add_model

		Add a new model
		"""
		body = Model()
		response = self.client.open(
			'/v1/models',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_configuration(self):
		"""Test case for get_configuration

		Get a Configuration
		"""
		response = self.client.open(
			'/v1/configuration/{configurationId}'.format(configurationId=789),
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_configurations(self):
		"""Test case for get_configurations

		Get metadata about all configurations
		"""
		response = self.client.open(
			'/v1/configuration',
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_data_set(self):
		"""Test case for get_data_set

		Get all metadata
		"""
		response = self.client.open(
			'/v1/data',
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_model(self):
		"""Test case for get_model

		Get a Model
		"""
		response = self.client.open(
			'/v1/models/{modelId}'.format(modelId=789),
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_models(self):
		"""Test case for get_models

		Get all metadata about models available
		"""
		response = self.client.open(
			'/v1/models',
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_predict_configuration(self):
		"""Test case for predict_configuration

		predict using a configuration with the provided inputs
		"""
		body = PredictInput()
		response = self.client.open(
			'/v1/configuration/{configurationId}/predict'.format(configurationId=789),
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_train_configuration(self):
		"""Test case for train_configuration

		train a given configuration with the provided parameters
		"""
		body = Train()
		response = self.client.open(
			'/v1/configuration/{configurationId}/train'.format(configurationId=789),
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_update_configuration(self):
		"""Test case for update_configuration

		Update configuration
		"""
		body = Configuration()
		response = self.client.open(
			'/v1/configuration/{configurationId}'.format(configurationId=789),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_update_dataset(self):
		"""Test case for update_dataset

		Update dataset
		"""
		body = Dataset()
		response = self.client.open(
			'/v1/data',
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_update_model(self):
		"""Test case for update_model

		Update model
		"""
		body = Model()
		response = self.client.open(
			'/v1/models/{modelId}'.format(modelId=789),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest
	unittest.main()
