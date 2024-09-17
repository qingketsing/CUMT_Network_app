import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class app:
    def run(self):
        driver = webdriver.Edge()

        driver.get('http://10.2.5.251/')
        input_elements = driver.find_elements(By.CLASS_NAME, "edit_lobo_cell")
        time.sleep(1)
        input = []
        with open('config.txt', 'r') as file:
            line = file.readline()
            line = line.strip('\n')
            while line:
                input.append(line)
                line = file.readline()
                line = line.strip('\n')


        for i in range(2):
            input_elements[i + 1].send_keys(input[i])
        input_element2 = driver.find_element(By.NAME, "ISP_select")
        Select(input_element2).select_by_index(int(input[2]))
        driver.execute_script("arguments[0].click()", input_elements[0])
        driver.quit()


if __name__ == "__main__":
    app = app()
    app.run()



