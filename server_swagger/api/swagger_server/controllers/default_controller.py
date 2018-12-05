import connexion
import six

from swagger_server.models.answer import Answer  # noqa: E501
from swagger_server.models.answer_metadata import AnswerMetadata  # noqa: E501
from swagger_server import util


def get_answer(answerId):  # noqa: E501
	"""Get a Answer

	 # noqa: E501

	:param answerId: ID of answer to get
	:type answerId: int

	:rtype: Answer
	"""
	return 'do some magic!'


def get_answers():  # noqa: E501
	"""Get all metadata about answers available

	 # noqa: E501


	:rtype: List[AnswerMetadata]
	"""
	return 'do some magic!'


def query_answer(body):  # noqa: E501
	"""query an answer

	 # noqa: E501

	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	answer = 'Attention ce flim n\'est pas un flim sur le cyclimse'
	if connexion.request.is_json:
		body = Answer.from_dict(connexion.request.get_json())  # noqa: E501
		question = body.content
		question = question.replace('_',' ')
		print(question)
		if 'l\'homme le plus classe du monde' in question :
			answer = 'Georges Abitbol'
		if 'dernières paroles' in question :
			answer = 'Monde de merde !'
		print(answer)
	# return 'do some magic!'
	return answer

def update_answer(answerId, body):  # noqa: E501
	"""Update answer

	 # noqa: E501

	:param answerId: ID of answer to get
	:type answerId: int
	:param body: 
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = Answer.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
