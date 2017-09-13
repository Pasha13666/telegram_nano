from distutils.core import setup

setup(
    name='telegram_nano',
    version='1.0',
    packages=['telegram_nano'],
    dependency_links=['git+https://github.com/Pasha13666/nano_api.git'],
    license='MIT',
    author='Pasha__kun',
    url='https://github.com/Pasha13666/telegram_nano',
    description='API bindings for telegram.org with nano_api'
)
