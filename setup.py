from setuptools import setup

REQUIRES = [
    'requests>=2.31.0',
    'structlog>=23.1.0',
    'allure-pytest>=2.13.2',
    'curlify>=2.2.1'
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
