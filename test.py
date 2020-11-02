from IPython import embed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from msedge.selenium_tools import Edge, EdgeOptions
from PIL import Image
import numpy as np
import argparse, random, time, pytesseract, lxml

def main():
    try:
        print("ウェブドライバーを立ち上げています・・・")
        port = str(args.port[0])
        load_delay_time = args.load_delay_time[0]
        options = EdgeOptions()
        options.use_chromium = True
        driver = Edge(options = options)
        driver.maximize_window()

        if len(port) != 4:	
            print("入力した番号は4桁ではないです。4桁のポート番号を記入してください。")
            quit()

        print("ページを開いています・・・")
        driver.get(f"http://127.0.0.1:{port}")
        print(f"ページの読み込みのため{str(load_delay_time)}秒待機します・・・")

        for i in range(load_delay_time,0,-1):
            time.sleep(1)
            print(f"終わるまで{i}秒")

        print("Interactive Pythonコンソールを立ち上げています・・・")
        
        soup = BeautifulSoup(driver.page_source, features="lxml")
        #Define web elements to be tested as dictionary where element ids are the keys.
        test_element_ids = {
            "dtFilter": {
                "tag":
                "select",
                "click_el_xpath":
                "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div/div/div"
            },
            "maxAmount": {
                "tag":"input",
            },
            "maxSigma": {
                "tag":"input",
            },
            "pl": {
                "tag":"select",
                "click_el_xpath":
                "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div[5]/div/div/div"
            },
            "reason": {
                "tag":"select",
                "click_el_xpath":
                "/html/body/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div[6]/div/div/div/div[1]"
            }
        }
        for test_el_id in test_element_ids:
            test_el = test_element_ids[test_el_id]
            if test_el["tag"] == "select":
                el = driver.find_element_by_xpath(test_el["click_el_xpath"])
                el.click()
                soup = BeautifulSoup(driver.page_source, features="lxml")                
                select_items = [tag.text for tag in soup.find(id=test_el_id).find_next_sibling().select("div.option")]
                print(f"number of items in select box: {len(select_items)}")
                for select_item in select_items:
                    click_el = driver.find_element_by_css_selector(f"[data-value='{select_item}']")
                    el.click()
                    click_el.click()
                    time.sleep(5)
            elif test_el["tag"] == "input":
                test_round = 1
                while test_round < 6:
                    test_input_number = int(random.random()*random.choice([10,100,1000,10000,
                    100000,1000000,10000000,10000000,100000000]))
                    el = driver.find_element_by_id(test_el_id)
                    el.clear()
                    el.click()
                    el.send_keys(test_input_number)
                    time.sleep(5)
                    test_round += 1
                el.clear()
                el.send_keys(0)
    except Exception as e:
        print(f"(EXCEPT) An error occurred: {str(e)} Attempting to enter debug mode at point of error.")
        embed()
    finally:
        print("プログラムが正常終了しました。ウェブドライバーを終了します。お疲れ様でした。")
        embed()
        driver.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="vv", description="Automates GLAD viewer validation.")
    parser.add_argument("port", help="specify port number of browser to be tested",
                        nargs=1, type=int, action="store")
    parser.add_argument("load_delay_time", help="set the number of seconds to"
                        + "wait before executing test actions. the slower"
                        + "your machine, the longer you should make the delay"
                        + "(usually between 10-30 seconds).",
                        nargs=1, type=int, action="store")
    args = parser.parse_args()
    main()