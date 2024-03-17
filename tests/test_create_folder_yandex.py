import responses
import pytest

from create_folder_yandex_disc import CreateFolderYandexDisc


# positive case

@responses.activate
def test_positive_create_folder():
    valid_json_answer = {
        "href": "https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FTestFolder",
        "method": "GET",
        "templated": False
    }

    responses.add(method=responses.PUT,
                  url='https://cloud-api.yandex.net/v1/disk/resources?path=TestFolder',
                  json=valid_json_answer,
                  status=201)

    create_folder_client = CreateFolderYandexDisc()
    res = create_folder_client.create_folder()
    assert res.status_code == 201


# negative cases

@responses.activate
@pytest.mark.parametrize('err_code', [400, 401, 403, 404, 406, 409, 423, 429, 503, 507])
def test_negative_status_code(err_code):
    valid_json_answer = {
        "message": "string",
        "description": "string",
        "error": "string"
    }

    responses.add(method=responses.PUT,
                  url='https://cloud-api.yandex.net/v1/disk/resources?path=TestFolder',
                  json=valid_json_answer,
                  status=err_code)

    create_folder_client = CreateFolderYandexDisc()
    res = create_folder_client.create_folder()
    assert res.status_code == err_code


@responses.activate
def test_status_code_413_create_folder():
    valid_json_answer = {
        "reason": "string",
        "description": "string",
        "limit": 0,
        "message": "string",
        "error": "string"
    }

    responses.add(method=responses.PUT,
                  url='https://cloud-api.yandex.net/v1/disk/resources?path=TestFolder',
                  json=valid_json_answer,
                  status=413)

    create_folder_client = CreateFolderYandexDisc()
    res = create_folder_client.create_folder()
    assert res.status_code == 413
