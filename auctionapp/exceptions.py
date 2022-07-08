
from rest_framework.exceptions import APIException
class IdNotAvailable(APIException):
    default_detail = 'Specified id is not available'

class InvalidData(APIException):
    default_detail = 'Data is invalid'

class IdOrDateNotAvailable(APIException):
    default_detail = 'No Bids are available with specified product Id or Date'

class ProductNotAvailable(APIException):
    default_detail = 'Specified product is not available'
