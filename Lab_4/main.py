from lib_requests import run_requests
from lib_colorama import run_colorama
from lib_numpy import run_numpy
from lib_pandas import run_pandas
from lib_pillow import run_pillow
from lib_matplotlib import run_matplotlib
from lib_bs4 import run_bs4
from lib_jinja2 import run_jinja2
from lib_pytz import run_pytz
from lib_qrcode import run_qrcode

from lib_math import run_math
from lib_random import run_random
from lib_datetime import run_datetime
from lib_os import run_os
from lib_json import run_json

def main():
    print("ЗАПУСК ЗОВНІШНІХ БІБЛІОТЕК")
    run_requests()
    run_colorama()
    run_numpy()
    run_pandas()
    run_pillow()
    run_matplotlib()
    run_bs4()
    run_jinja2()
    run_pytz()
    run_qrcode()
    
    print("\nЗАПУСК ВБУДОВАНИХ БІБЛІОТЕК")
    run_math()
    run_random()
    run_datetime()
    run_os()
    run_json()
    print("\nУрааааааа")

if __name__ == "__main__":
    main()
