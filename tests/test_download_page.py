import tempfile
import requests_mock
import os
import pytest
from page_loader.download import download_page
from page_loader.name_formatter import get_file_name


FILES_COUNT = 4
SITE_PATH = '/courses'
URL = 'https://ru.hexlet.io'
SITE_FILES_DIR = 'ru-hexlet-io-courses_files'


@pytest.fixture()
def content():
    with open('tests/fixtures/file1.html', 'r') as text:
        content = text.read()
    return content


@pytest.fixture()
def image():
    with open('tests/fixtures/nodejs.png', 'rb') as img:
        image = img.read()
    return image


@pytest.fixture()
def correct_names():
    return {
        'html': 'ru-hexlet-io-courses.html',
        'img': 'ru-hexlet-io-assets-professions-nodejs.png',
        'css': 'ru-hexlet-io-assets-application.css',
        'js': 'ru-hexlet-io-packs-js-runtime.js'
    }


def read_file(file_path):
    with open(file_path, 'r') as data:
        correct_data = data.read()
    return correct_data


def test_process_loader(content, correct_names, image):

    with requests_mock.Mocker() as resp:
        resp.get(URL + SITE_PATH, text=content)
        resp.get(URL + '/assets/professions/nodejs.png', content=image)
        resp.get(URL + '/assets/application.css', text=read_file('tests/fixtures/style.css'))
        resp.get(URL + '/packs/js/runtime.js', text=read_file('tests/fixtures/script.js'))
        with tempfile.TemporaryDirectory() as temp:
            correct_html = read_file('tests/fixtures/html_result.html')
            correct_path = os.path.join(temp, correct_names.get('html'))
            result_path = download_page(URL + SITE_PATH, temp)
            image_path = os.path.join(temp, SITE_FILES_DIR, correct_names.get('img'))
            css_path = os.path.join(temp, SITE_FILES_DIR, correct_names.get('css'))
            image_name = get_file_name(URL + '/assets/professions/nodejs.png')
            css_name = get_file_name(URL + '/assets/application.css')
            assert read_file(result_path) == correct_html
            assert read_file(css_path) == read_file('tests/fixtures/style.css')
            files_count = len(os.listdir(os.path.join(temp, os.path.splitext(get_file_name(URL+SITE_PATH))[0] + '_files')))
            assert files_count == FILES_COUNT
            with open(os.path.join(image_path), 'rb') as image_file:
                received_image = image_file.read()
                assert received_image == image
            assert css_name == correct_names.get('css')
            assert image_name == correct_names.get('img')
            assert result_path == correct_path
