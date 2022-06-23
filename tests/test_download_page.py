import tempfile
import requests_mock
import os
import pytest
from page_loader.download_page import download_page


@pytest.fixture()
def url():
    return 'http://my_site_url.com'


@pytest.fixture()
def content():
    return '<h1>Hello, Hexlet!</h1>'


@pytest.fixture()
def correct_name():
    return 'my-site-url-com.html'


def test_process_loader(url, content, correct_name):
    with requests_mock.Mocker() as resp:
        resp.get(url, text=content)

        with tempfile.TemporaryDirectory() as temp:
            correct_path = os.path.join(temp, correct_name)
            result_path = download_page('http://my_site_url.com', temp)

            with open(result_path, 'r') as file:
                received_file = file.read()
                assert received_file == content
            assert result_path == correct_path
