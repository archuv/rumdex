#

import os,sys,subprocess
def main():
    #print "Install mysql......."
    #subprocess.call(["zypper","install","mysql-community-server"])
    #subprocess.call(["reboot"])
    #subprocess.call(["zypper","install","postfix","postfix-mysql","mysql-community server"])
    #subprocess.call(["systemctl","enable","mysql.service"])
    #subprocess.call(["systemctl","start","mysql.service"])
    #subprocess.call(["rcmysql","reload"])
    subprocess.call(["mysql","secure","installation"])
    #print "Installing apache2......"
    #subprocess.call(["zypper","install","apache2"])
    #subprocess.call(["systemctl","enable","apache2.service"])
    #subprocess.call(["rcapache2","reload"])
    #print "Installing php5........"
    #subprocess.call(["zypper","install","apache2-mod_php-5"])
    #subproces.call(["rcapache2","reload"])
    #file_info_php = open('/srv/www/htdocs/info.php', 'w')
    #info_code = '<?php\nphpinfo();\n?>'
    #file_info_php.write(info_code)
    #subprocess.call(["rcapache2","reload"])
    #print "Installing phpMyAdmin........."
    #subprocess.call(["zyppper","install","phpMyAdmin"])
    #subprocess.call(["rcapache2","reload"])
    #subprocess.call(["a2enmod","rewrite"])
    #print "Virtual host creating........."
    #f_in = open('/etc/apache2/listen.conf').read()
    #text = f_in.replace('#NameVirtualHost *:80', 'NameVirtualHost *:80')
    #f_out = open('/etc/apache2/listen.conf', 'w').write(text)
#def testmatch():


if  __name__ ==  "__main__":
   main()
   #stestmatch()
