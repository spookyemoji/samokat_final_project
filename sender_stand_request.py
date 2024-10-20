import requests
import conf
import data

def create_order():
    return requests.post(conf.SERVER_URL + conf.NEW_ORDER_PATH, json=data.create_order)

def get_order(track):
    return requests.get(conf.SERVER_URL + conf.GET_ORDER_PATH + track)