from core.color import blue # Blue for Warnings
from core.color import red #Red For Errors
from core.color import green #Green for output
import requests
import re

def run(target):
    try:
        r = requests.get(target, verify = False) 
        r2 = requests.get(target+'/administrator/', verify = False)
        web_template = ''.join(set(re.findall("/templates/(.+?)/", r.text, re.IGNORECASE)))
        admin_template = ''.join(set(re.findall("/administrator/templates/(.+?)/", r2.text, re.IGNORECASE)))
        if web_template is not "":
            green("Web Template Found : " + web_template)
        if admin_template is not "":
            green("Admin Template Found : " + admin_template)
    except Exception as err:
        red("Error Occured: " + err)