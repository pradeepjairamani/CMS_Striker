from core.cms_detection import start
from core.args_loader import argsload
from core.color import blue # Blue for Warnings
from core.color import red #Red For Errors
from core.color import green #Green for output
import os
import importlib
import argparse
import getopt
import sys

def cms_scan():
   #interactive
   #normal
   #verbose
   args = argsload()
   target = args.target
   if args.force:
      if args.force.lower()[0] == "j":
         force = "Joomla"
      elif args.force.lower()[0] == "w":
         force = "Wordpress"
      elif args.force.lower()[0] == "d":
         force = "Drupal"
      else:
         red(" Wrong Choice : " + args.force)
         force = ""
         blue(" Using Automatic CMS detection")
   else:
      force = ""
   if target is not "":
      cms_found = (start(target, force))
      if cms_found == "":
         red ("\nCMS not Found, Try forcing")
      else:
         green("\n Target : "+target)
         green("CMS : " + cms_found)
         plugins = os.listdir("libs/"+cms_found)
         plugins.remove("__init__.py")
         plugins.remove("__init__.pyc")
         green("Plugins loaded : " + str(len(plugins))) 
         for plugin in plugins:
            engine = "libs." + cms_found + "." + plugin + ".engine"
            exploit = importlib.import_module(engine, ".")
            exploit.run(target)            

   else:
      red ("Please Enter Target")
   
if __name__ == '__main__':
   cms_scan()
