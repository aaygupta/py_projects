from openpyxl import load_workbook
import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess

path = os.path.dirname(os.path.realpath(__file__))
wb = load_workbook(path + '/assets/Salary Slip Template.xlsx')
sheet = wb['Pay Slip']

month = sheet['F9']
name = sheet['E11']
gender = sheet['E12']
pan = sheet['E13']
aadhaar = sheet['E14']
uan = sheet['E15']

ecode = sheet['H11']
doj = sheet['H12']
department = sheet['H13']
designation = sheet['H14']
account = sheet['H15']

sheet['F9'] = 'January'
wb.save('sample.xlsx')