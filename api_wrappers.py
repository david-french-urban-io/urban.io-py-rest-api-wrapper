import requests


def default_readings_params():
	return {
		"size":1000
	}

class Endpoints:
	def __init__(self, email, token):
		self.headers = {
			"X-User-Email":email, 
			"X-User-Token":token, 
			"Content-Type":'application/json'
		}
	


class PublicRESTEndpoints(Endpoints):

	URL_TEMPLATE_DATASTREAMS_BY_LOCATION = "https://iot-rest-prod.urbani.se/api/v1/location/{location_id}/datastreams"
	URL_TEMPLATE_DATASTREAM_READINGS = "https://iot-rest-prod.urbani.se/api/v1/datastream/{datastream_id}/readings"
	URL_TEMPLATE_CUSTOMER_ALERTS = "https://iot-rest-prod.urbani.se/api/v1/customer/{customer_id}/alerts"
	URL_TEMPLATE_DS_ALERTS = "https://iot-rest-prod.urbani.se/api/v1/datastream/{datastream_id}/alerts" 
	URL_TEMPLATE_LOCATION_ALERTS = "https://iot-rest-prod.urbani.se/api/v1/location/{location_id}/alerts"
	URL_TEMPLATE_OPERATOR_ALERTS = "https://iot-rest-prod.urbani.se/api/v1/operator/{operator_id}/alerts"


	def request_decorator(fn):
		'''
		Expects fn to be a function/method that return a request response
		'''
		def inner(*args, **kwargs):
			request_response = fn(*args, **kwargs)
			#TODO - add error handling based on response codes
			return request_response.json()
		return inner

	@request_decorator
	def get_datastreams_by_location_ext(self, location_id):
		url = self.URL_TEMPLATE_DATASTREAMS_BY_LOCATION.format(location_id=location_id)
		response = requests.get(url, headers=self.headers)
		return response

	@request_decorator
	def get_datastream_readings(self, datastream_id, params = default_readings_params()):
		url = self.URL_TEMPLATE_DATASTREAM_READINGS.format(datastream_id=datastream_id)
		response = requests.get(url, headers=self.headers, params=params)
		return response


	@request_decorator
	def get_customer_alerts(self, customer_id, params = {}):
		url = self.URL_TEMPLATE_CUSTOMER_ALERTS.format(customer_id=customer_id)
		response = requests.get(url, headers=self.headers, params=params)
		return response
	
	@request_decorator
	def get_datastream_alerts(self, datastream_id, params = {}):
		url = self.URL_TEMPLATE_DS_ALERTS.format(datastream_id=datastream_id)
		response = requests.get(url, headers=self.headers, params=params)
		return response.json()

	@request_decorator
	def get_location_alerts(self, location_id, params = {}):
		url = self.URL_TEMPLATE_LOCATION_ALERTS.format(location_id=location_id)
		response = requests.get(url, headers=self.headers, params=params)
		return response.json()

	@request_decorator
	def get_operator_alerts(self, operator_id, params = {}):
		url = self.URL_TEMPLATE_OPERATOR_ALERTS.format(operator_id=operator_id)
		response = requests.get(url, headers=self.headers, params=params)
		return response.json()