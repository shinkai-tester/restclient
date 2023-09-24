from setuptools import setup

REQUIRES = [
    'requests',
    'structlog',
    'allure-pytest',
    'curlify'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/shinkai-tester/restclient.git',
    license='MIT',
    author='Aleksandra Klimantova',
    author_email='',
    install_requires=REQUIRES,
    description='Restclient with Allure and Logger'
)
