import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)


def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION,
           params={"t": track_number})