from core.color import blue # Blue for Warnings
from core.color import red #Red For Errors
from core.color import green #Green for output
import requests
import re

def run(target):
    try:
        req = requests.get(target+'/joomla.xml', verify = False)
        if req.status_code == 404:
            req = requests.get(
                target+'/administrator/manifests/files/joomla.xml', verify = False)
        regex = '<version>(.+?)</version>'
        pattern = re.compile(regex)
        version = re.findall(pattern, req.text)
        version = ''.join(version)
        green("Version Found : " + version)
    except Exception as err:
        red(err)