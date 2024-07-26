from src.folder_crawl import file
import pytest
from pathlib import Path


@pytest.fixture()
def file_path():
    return Path(".").cwd()


def test_is_config_available(file_path):
    return file.Config(file_path).exists()
