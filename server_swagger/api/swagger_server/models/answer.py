# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Answer(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, id: int=None, name: str=None, content: str=None):  # noqa: E501
		"""Answer - a model defined in Swagger

		:param id: The id of this Answer.  # noqa: E501
		:type id: int
		:param name: The name of this Answer.  # noqa: E501
		:type name: str
		:param content: The content of this Answer.  # noqa: E501
		:type content: str
		"""
		self.swagger_types = {
			'id': int,
			'name': str,
			'content': str
		}

		self.attribute_map = {
			'id': 'id',
			'name': 'name',
			'content': 'content'
		}

		self._id = id
		self._name = name
		self._content = content

	@classmethod
	def from_dict(cls, dikt) -> 'Answer':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The answer of this Answer.  # noqa: E501
		:rtype: Answer
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def id(self) -> int:
		"""Gets the id of this Answer.


		:return: The id of this Answer.
		:rtype: int
		"""
		return self._id

	@id.setter
	def id(self, id: int):
		"""Sets the id of this Answer.


		:param id: The id of this Answer.
		:type id: int
		"""

		self._id = id

	@property
	def name(self) -> str:
		"""Gets the name of this Answer.


		:return: The name of this Answer.
		:rtype: str
		"""
		return self._name

	@name.setter
	def name(self, name: str):
		"""Sets the name of this Answer.


		:param name: The name of this Answer.
		:type name: str
		"""

		self._name = name

	@property
	def content(self) -> str:
		"""Gets the content of this Answer.


		:return: The content of this Answer.
		:rtype: str
		"""
		return self._content

	@content.setter
	def content(self, content: str):
		"""Sets the content of this Answer.


		:param content: The content of this Answer.
		:type content: str
		"""

		self._content = content
