# coding=utf-8
import unittest
from selenium import webdriver
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from BeautifulReport import BeautifulReport


def new_file(test_dir):
	lists = oa.listdir(test_dir)
	print(lists)
	lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    file_path = os.path.join(test_dir, lists[-1])
    return file_path
