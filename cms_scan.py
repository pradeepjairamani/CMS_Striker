from libs.cms_detection import start
import os
import importlib

def cms_scan():
   #interactive
   #Force CMS
   #no exploitdb
   #normal
   #install searchsploit only
   target = "http://www.poornima.edu.in"
   if target is not "":
      cms_found = (start(target, "Wordpress"))
      if cms_found == "":
         print ("CMS not Found, Try forcing")
      else:
         plugins = os.listdir("libs/"+cms_found)
         print "Plugins loaded : " + str(len(plugins)) 
         for plugin in plugins:
            engine = "libs." + cms_found + "." + plugin + ".engine"
            print(engine)
            #exploit = importlib.import_module(engine, ".")
            #exploit.run(target)            

   else:
      print ("Please Enter Target")
   
if __name__ == '__main__':
   cms_scan()
