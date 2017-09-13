from distutils.core import setup
import telegram_nano

setup(
    name='telegram_nano',
    version=telegram_nano.__version__,
    packages=['telegram_nano'],
    install_requires=[telegram_nano.__na_required__],
    license='MIT',
    author='Pasha__kun',
    url='https://github.com/Pasha13666/telegram_nano',
    description='API bindings for telegram.org with nano_api'
)
