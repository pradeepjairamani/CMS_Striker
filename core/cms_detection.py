from core.color import red
from core.color import blue
import sys

def start(target, cms_name):
            if cms_name is not "":
               return cms_name
            import requests
            import random
            user_agent_list = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.5) Gecko/20060719 Firefox/1.5.0.5",
            "Googlebot/2.1 ( http://www.googlebot.com/bot.html)",
            "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Ubuntu/10.04"
            " Chromium/9.0.595.0 Chrome/9.0.595.0 Safari/534.13",
            "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)",
            "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
            "Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620",
            "Debian APT-HTTP/1.3 (0.8.10.3)",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Googlebot/2.1 (+http://www.googlebot.com/bot.html)",
            "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
            "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; "
            "http://help.yahoo.com/help/us/shop/merchant/)"]
            req_url = target + "/N0WH3R3.php"
            req_joomla_url = target + "/configuration.php"           
            req_wordpress_url = target + "/wp-config.php"
            req_drupal_url = target + "/sites/default/settings.php"
            try:
               user_agent = {'User-agent': random.choice(user_agent_list)}
               req = requests.get(req_url, timeout=10, headers=user_agent,  verify = False)
               code_for_404 = req.text
               user_agent = {'User-agent': random.choice(user_agent_list)}
               req_wordpress = requests.get(req_wordpress_url, timeout=10, headers=user_agent, verify = False)
               user_agent = {'User-agent': random.choice(user_agent_list)}
               req_joomla = requests.get(req_joomla_url, timeout=10, headers=user_agent, verify = False)
               user_agent = {'User-agent': random.choice(user_agent_list)}
               req_drupal = requests.get(req_drupal_url, timeout=10, headers=user_agent, verify = False)
            except requests.exceptions.RequestException as e: 
               red("Requests cannot be completed, Check your internet connection or website")
               sys.exit(0)
            if req_wordpress.text != code_for_404 or req_wordpress.status_code == 403:
                return "Wordpress"
            elif req_drupal.status_code != code_for_404 or req_drupal.status_code == 403:
                return "Drupal"
            elif req_joomla.status_code != code_for_404 or req_joomla.status_code == 403:
                return "Joomla"
            else:
                red ("Error CMS not found, Try Forcing")
                sys.exit(0)
