# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.answer_metadata import AnswerMetadata  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
	"""DefaultController integration test stubs"""

	def test_get_answer(self):
		"""Test case for get_answer

		Get a Answer
		"""
		response = self.client.open(
			'/v1/answers/{answerId}'.format(answerId=789),
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_get_answers(self):
		"""Test case for get_answers

		Get all metadata about answers available
		"""
		response = self.client.open(
			'/v1/answers',
			method='GET')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_query_answer(self):
		"""Test case for query_answer

		query an answer
		"""
		body = Answer()
		response = self.client.open(
			'/v1/answers',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))

	def test_update_answer(self):
		"""Test case for update_answer

		Update answer
		"""
		body = Answer()
		response = self.client.open(
			'/v1/answers/{answerId}'.format(answerId=789),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
					   'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest
	unittest.main()
