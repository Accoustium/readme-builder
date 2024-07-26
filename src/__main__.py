from folder_crawl.file import Config
from pathlib import Path


def main():
    config = Config(Path("."))
    print(config)


if __name__ == "__main__":
    main()
