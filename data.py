import helper

class DataCreateCourier:
    list_registration = {
    "login": helper.fake_login(),
    "password": helper.fake_password(),
    "firstName": helper.fake_firstname()
}

class DataListOrders:
    list_order = {
    "firstName": helper.fake_firstname(),
    "lastName": helper.fake_lastname(),
    "address": "Kanoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Privet! Privet! Privet!"
    }
    color_scooter= [["BLACK"], ["GREY"], (["BLACK"], ["GREY"]), [""]]

class DataResponse:
    RESP_CREATE_COURIER_OK = {"ok": True}
    RESP_CREATE_COURIER_NO_LOGIN = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    RESP_CREATE_COURIER_REPEAT = {"code": 409, "message": "Этот логин уже используется"}
    RESP_GETTING_ORDERS_NO_ID = {"code": 400, "message":  "Недостаточно данных для поиска"}
    RESP_GETTING_ORDERS_NO_VALID ={"code": 404, "message": "Заказ не найден"}
    RESP_LOGIN_PASSWORD_NO_DATA = {"code": 400, "message":  "Недостаточно данных для входа"}
    RESP_LOGIN_PASSWORD_NO_VALID = {"code": 404, "message": "Учетная запись не найдена"}

class DataRegistration:
    registration_data = [
        {"password": helper.fake_password(),"firstname":helper.fake_firstname()},
        {"login": helper.fake_login(), "firstname":helper.fake_firstname()}]

class DataEnterNoValid:
    enter_data = [
        {"login": helper.fake_login(), "password": ""},
        {"login": "", "password": helper.fake_password()}]

class DataResponseData:
    RESPONSE_DATA_SUCCESS = "orders"
    RESPONSE_ID_ORDER = "track"