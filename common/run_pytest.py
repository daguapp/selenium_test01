import os
from time import sleep
from allure_pytest import plugin as allure_plugin
import pytest
from time import sleep
if __name__ == '__main__':
    pytest.main()
    sleep(2)
    os.system("'allure generate ./caseobject/temp -o ./report --clean'")