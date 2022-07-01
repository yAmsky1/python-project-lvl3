import tempfile
import requests_mock
import os
import pytest

from page_loader.download import download_page
from page_loader.name_formatter import get_name
from tests.file_reader import read_file


FILES_COUNT = 4
SITE_PATH = '/courses'
BASE_URL = 'https://ru.hexlet.io'
PAGE_FILES_DIR = 'ru-hexlet-io-courses_files'
MODE = {'IMAGE': 'rb', 'TEXT': 'r'}


@pytest.fixture()
def content():
    return read_file('tests/fixtures/file1.html', MODE.get('TEXT'))


@pytest.fixture()
def image():
    return read_file('tests/fixtures/nodejs.png', MODE.get('IMAGE'))


@pytest.fixture()
def style():
    return read_file('tests/fixtures/style.css', MODE.get('TEXT'))


@pytest.fixture()
def script():
    return read_file('tests/fixtures/script.js', MODE.get('TEXT'))


@pytest.fixture()
def html():
    return read_file('tests/fixtures/page_without_res.html', MODE.get('TEXT'))


@pytest.fixture()
def correct_names():
    return {
        'html': 'ru-hexlet-io-courses.html',
        'img': 'ru-hexlet-io-assets-professions-nodejs.png',
        'css': 'ru-hexlet-io-assets-application.css',
        'js': 'ru-hexlet-io-packs-js-runtime.js'
    }


def test_download_page_with_res(content, correct_names, image, style, script):

    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL + SITE_PATH, text=content)
        mock.get(BASE_URL + '/assets/professions/nodejs.png', content=image)
        mock.get(BASE_URL + '/assets/application.css', text=style)
        mock.get(BASE_URL + '/packs/js/runtime.js', text=script)

        with tempfile.TemporaryDirectory() as temp:

            correct_html = read_file('tests/fixtures/html_result.html', MODE.get('TEXT'))
            correct_path = os.path.join(temp, correct_names.get('html'))
            result_path = download_page(BASE_URL + SITE_PATH, temp)
            assert read_file(result_path, MODE.get('TEXT')) == correct_html
            assert result_path == correct_path

            image_path = os.path.join(temp, PAGE_FILES_DIR, correct_names.get('img'))
            image_name = get_name(BASE_URL + '/assets/professions/nodejs.png')
            assert image_name == correct_names.get('img')
            assert read_file(image_path, MODE.get('IMAGE')) == image

            css_path = os.path.join(temp, PAGE_FILES_DIR, correct_names.get('css'))
            css_name = get_name(BASE_URL + '/assets/application.css')
            assert read_file(css_path, MODE.get('TEXT')) == style
            assert css_name == correct_names.get('css')

            js_path = os.path.join(temp, PAGE_FILES_DIR, correct_names.get('js'))
            js_name = get_name('https://ru.hexlet.io/packs/js/runtime.js')
            assert read_file(js_path, MODE.get('TEXT'))
            assert js_name == correct_names.get('js')

            page_name, _ = os.path.splitext(get_name(BASE_URL + SITE_PATH))
            files_count = len(os.listdir(os.path.join(temp, page_name + '_files')))
            assert files_count == FILES_COUNT


def test_download_page_without_res(correct_names, html):
    with requests_mock.Mocker() as mock:
        mock.get(BASE_URL + SITE_PATH, text=html)
        with tempfile.TemporaryDirectory() as temp:
            page_path = download_page(BASE_URL + SITE_PATH, temp)
            correct_path = os.path.join(temp, correct_names.get('html'))
            assert read_file(page_path, MODE.get('TEXT')) == html
            assert page_path == correct_path


@pytest.mark.parametrize('url, exception', [
    ('ru.hexlet.io', 'WRONG ADDRESS!'),
    ('sptth://ru.hexlet.io', 'WRONG ADDRESS!'),
    ('https://fgjkhds.org/', 'CONNECTION ERROR!')
])
def test_download_with_errors(url,  exception):
    with tempfile.TemporaryDirectory() as temp:
        with pytest.raises(Exception):
            download_page(url, temp)
