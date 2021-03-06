from pack.pack_manager import TestManager
import pytest
from multiprocessing import Pool

driver_infos = [
    ["localhost:5555", "test_case/test_bid.py"],
    # ["192.168.6.89:6666", "test_case/test_bid.py"]
]
def run_parallel(driver_info):
    pytest.main([driver_info[1],
                 f"--cmdopt={driver_info[0]}", "--alluredir",
                 f"./report/allure_result",])

def pytest_start():
    with Pool(len(driver_infos)) as pool:
        pool.map(run_parallel, driver_infos)
        pool.close()
        pool.join()

if __name__ == '__main__':
    pytest_start()
    manager = TestManager()
    manager.generate_report()
