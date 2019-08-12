from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import UnexpectedAlertPresentException
from Histadrut_All_Tests import Global_Driver
from Histadrut_All_Tests import Login_Global
from Histadrut_All_Tests import ZeroBasker
from Histadrut_All_Tests import FillInPayment
from Histadrut_All_Tests import ContinuToPayment
from Histadrut_All_Tests import GoToUserHistory
from Histadrut_All_Tests import CancelOrder
from Histadrut_All_Tests import GiftCanceld
from Histadrut_All_Tests import Check_Canceled
from Histadrut_All_Tests import MainMnueChoose
from Histadrut_All_Tests import Region
from Histadrut_All_Tests import Atractions
from Histadrut_All_Tests import Choose_Attraction
from Histadrut_All_Tests import AddToBasket
from Histadrut_All_Tests import Choose_Quantity
from Histadrut_All_Tests import Eventim_Verify
import time
import unittest
#import HtmlTestRunner
import sys
import os
import sqlite3


browser = Global_Driver.getOrCreateWebdriver()
Login_Global.Make_Login()
ZeroBasker.ZeroBasket()
MainMnueChoose.Biluy_and_Pnay()
MainMnueChoose.HoverOnPage()
Atractions.EnterToAtraction()
Region.Tsafon()
Choose_Attraction.KayakimHaGoshrim()
Choose_Quantity.QuantityOneRegular()
AddToBasket.RegularAddToBasket()
time.sleep(2)
ContinuToPayment.ContinuToPayment()
FillInPayment.FillInPayement()
time.sleep(2)
GoToUserHistory.GoToUserHistory()
Eventim_Verify.VerifyOrder()
CancelOrder.PressCancelOrder()
Check_Canceled.IsCanseled()
try:
    GiftCanceld.CancelInGiftCardSyustem()
except:
    print("Test Failed")
finally:
    browser.close()
    browser.quit()
    print("Order Regular Variant Test Passed")







