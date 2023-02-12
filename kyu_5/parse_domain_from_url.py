import fire
import re


def domain_name(url):
    url = url.startswith('www.') if 'www.' in url else url.split('//')
    # url.split('.').first
    print(url)


if __name__ == '__main__':
    fire.Fire(domain_name)
