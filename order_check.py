import sender_stand_request


def positive_assert():
    # В переменную сохраняется обновленное тело запроса на вывод информации о заказе по номеру
    order_by_track_response_body = sender_stand_request.get_order_by_track()
    # Проверка, что код ответа равен 200
    assert order_by_track_response_body.status_code == 200


# Тест  код ответа на запрос о выводе заказа по треку =200
def test_get_order_by_track_success_response():
    positive_assert()
# Тест PASSED