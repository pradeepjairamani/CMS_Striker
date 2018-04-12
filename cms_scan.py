from core.cms_detection import start
from core.color import blue # Blue for Warnings
from core.color import red #Red For Errors
from core.color import green #Green for output
import os
import importlib
import argparse


def cms_scan():
   #interactive
   #Force CMS
   #no exploitdb
   #normal
   #install searchsploit only
   #verbose
   parser = argparse.ArgumentParser()
   parser.add_argument("-t", help="Target Goes here")
   args = parser.parse_args()
   #print args
   target = args.t
   green(target)
   #target = "http://www.poornima.edu.in"
   if target is not "":
      cms_found = (start(target, "Wordpress"))
      if cms_found == "":
         red ("CMS not Found, Try forcing")
      else:
         plugins = os.listdir("libs/"+cms_found)
         plugins.remove("__init__.py")
         plugins.remove("__init__.pyc")
         green("Plugins loaded : " + str(len(plugins))) 
         for plugin in plugins:
            engine = "libs." + cms_found + "." + plugin + ".engine"
            #green(engine)
            exploit = importlib.import_module(engine, ".")
            exploit.run(target)            

   else:
      red ("Please Enter Target")
   
if __name__ == '__main__':
   cms_scan()
