import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def setup_browser():
    # Setup the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_table_search(setup_browser):
    # Step 1: Navigate to the Browser web page
    driver = setup_browser
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    # Step 2: Type "New York" into the search box"
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()  # Clear any existing text
    search_box.send_keys("New York")  # Type the search term "New York"
    time.sleep(2)  # Wait for search results to load

    # Step 3: Validate the number of search results
    # Find all table rows
    rows = driver.find_elements(By.XPATH, "//table[@id='example']//tbody//tr")

    # Verify that there are exactly 5 results for "New York"
    assert len(rows) == 5, f"Expected 5 results but found {len(rows)}"

    print("Test Passed: Search results are correct.")


# if __name__ == "__main__":
#     pytest.main()
