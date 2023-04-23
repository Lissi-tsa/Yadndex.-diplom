import configuration
import requests
import data


# Функция создает новый заказ
def post_new_order(order_body):
    # При обращении к функции передают полный путь до документации, заголовки и параметры запроса
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)
# Переменной присваивается ответ на данный запрос


response = post_new_order(data.order_body)
# Сохранить ответ в формате json
response_json = response.json()
track = response_json["track"]
# сохранить track в словарь
track_no = {'t': track}


# Функция запрашивает track
def get_order_by_track():
    # При обращении к функции передают полный путь до документации, заголовки и параметры запроса
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params=track_no)


response_no = get_order_by_track()
