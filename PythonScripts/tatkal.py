__author__ = 'narendra'



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import os
import unittest, time, re

####################################################################

# LOGIN DATA TO BE ENTERED BY USER

username = "username"
password = "password"
from_station = "Source" #eg: KANPUR CENTRAL - CNB
to_station = "Destination" #eg: MUMBAI CST - CSTM
journey_date = "Journey Date" #eg: 26-12-2015

# PASSENGER DETAILS

#Eg: passenger1 = ['Akshay Dixit', '25', 'Male', 'MIDDLE']
passenger1 = ['', '', '', '']
passenger2 = ['', '', '', '']
passenger3 = ['', '', '', '']
passenger4 = ['', '', '', '']
mobile_number = "xxxxxxxxxx"

# PAYMENT DETAILS FOR INDIAN BANK DEBIT CARD (FASTEST)
# MODIFY SCRIPT FOR YOUR PAYMENT DETAILS

card_number = "xxxxxxxxxxxxxx"
expiry_date = ['x', 'xxxx']
name_on_card = "Xxxxx Xxxxx"
pin = "xxxx"

###################################################################

class Irctcfinal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.irctc.co.in/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_irctcfinal(self):
        driver = self.driver
        driver.get(self.base_url + "/eticketing/loginHome.jsf")
        driver.find_element_by_id("usernameId").clear()
        driver.find_element_by_id("usernameId").send_keys(username)
        driver.find_element_by_name("j_password").clear()
        driver.find_element_by_name("j_password").send_keys(password)
        driver.find_element_by_name("j_captcha").clear()
        try:
            drive = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "jpform:fromStation")))
        finally:
            drive.clear()


        driver.find_element_by_id("jpform:fromStation").send_keys(from_station)
        driver.find_element_by_id("jpform:toStation").clear()
        driver.find_element_by_id("jpform:toStation").send_keys(to_station)
        driver.find_element_by_id("jpform:journeyDateInputDate").send_keys(journey_date)
        driver.find_element_by_id("jpform:jpsubmit").click()
        driver.find_elements_by_css_selector("input[type='radio'][value='CK']")[0].click()

        # THIS MODULE TO BE ENABLED ACCORDING TO TATKAL TICKET TIMING ONLY
		# Modify according to your time

        c = "Time to book your ticket"
        localtime = time.asctime( time.localtime(time.time()) )
        while(localtime != "Fri May 25 11:00:05 2016"):
            localtime = time.asctime( time.localtime(time.time()) )
        print c

		# MODIFY ACCORDING TO YOUR COACH PREFERENCE & TRAIN NUMBER

        driver.find_element_by_id("cllink-12533-SL-3").click()

        driver.find_element_by_xpath("(//a[contains(text(),'Book Now')])[2]").click()

        driver.find_element_by_xpath("//td[2]/input").clear()
        driver.find_element_by_xpath("//td[2]/input").send_keys(passenger1[0])
        driver.find_element_by_id("addPassengerForm:psdetail:0:psgnAge").clear()
        driver.find_element_by_id("addPassengerForm:psdetail:0:psgnAge").send_keys(passenger1[1])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:0:psgnGender")).select_by_visible_text(passenger1[2])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:0:berthChoice")).select_by_visible_text(passenger1[3])
        '''
        UNCOMMENT ACCORDING TO REQUIRED NUMBER OF PASSENGERS

        driver.find_element_by_xpath("//tr[2]/td[2]/input").clear()
        driver.find_element_by_xpath("//tr[2]/td[2]/input").send_keys(passenger2[0])
        driver.find_element_by_id("addPassengerForm:psdetail:1:psgnAge").clear()
        driver.find_element_by_id("addPassengerForm:psdetail:1:psgnAge").send_keys(passenger2[1])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:1:psgnGender")).select_by_visible_text(passenger2[2])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:1:berthChoice")).select_by_visible_text(passenger2[3])
        driver.find_element_by_xpath("//tr[3]/td[2]/input").clear()
        driver.find_element_by_xpath("//tr[3]/td[2]/input").send_keys(passenger3[0])
        driver.find_element_by_id("addPassengerForm:psdetail:2:psgnAge").clear()
        driver.find_element_by_id("addPassengerForm:psdetail:2:psgnAge").send_keys(passenger3[1])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:2:psgnGender")).select_by_visible_text(passenger3[2])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:2:berthChoice")).select_by_visible_text(passenger3[3])
        driver.find_element_by_xpath("//tr[4]/td[2]/input").clear()
        driver.find_element_by_xpath("//tr[4]/td[2]/input").send_keys(passenger4[0])
        driver.find_element_by_id("addPassengerForm:psdetail:3:psgnAge").clear()
        driver.find_element_by_id("addPassengerForm:psdetail:3:psgnAge").send_keys(passenger4[1])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:3:psgnGender")).select_by_visible_text(passenger4[2])
        Select(driver.find_element_by_id("addPassengerForm:psdetail:3:berthChoice")).select_by_visible_text(passenger4[3])
        '''
        driver.find_element_by_id("addPassengerForm:mobileNo").clear()
        driver.find_element_by_id("addPassengerForm:mobileNo").send_keys(mobile_number)

        driver.find_element_by_id("j_captcha").clear()
        try:
            element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "DEBIT_CARD")))
        finally:
            element.click()

        driver.find_element_by_xpath("//div[4]/table/tbody/tr/td/table/tbody/tr/td[3]/input").click()
        driver.find_element_by_id("validate").click()
        driver.find_element_by_id("debit").click()
        driver.find_element_by_name("Ecom_Payment_Card_Number").click()
        driver.find_element_by_name("Ecom_Payment_Card_Number").click()
        driver.find_element_by_name("Ecom_Payment_Card_Number").clear()
        driver.find_element_by_name("Ecom_Payment_Card_Number").send_keys(card_number)
        Select(driver.find_element_by_name("Ecom_Payment_Card_ExpDate_Month")).select_by_visible_text(expiry_date[0])
        Select(driver.find_element_by_name("Ecom_Payment_Card_ExpDate_Year")).select_by_visible_text(expiry_date[1])
        driver.find_element_by_name("Ecom_Payment_Card_Name").click()
        driver.find_element_by_name("Ecom_Payment_Card_Name").clear()
        driver.find_element_by_name("Ecom_Payment_Card_Name").send_keys(name_on_card)
        driver.find_element_by_name("Ecom_Payment_Pin").clear()
        driver.find_element_by_name("Ecom_Payment_Pin").send_keys(pin)
        driver.find_element_by_id("SubmitBtn").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()