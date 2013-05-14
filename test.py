#

import os,sys,subprocess
def main():
    print "Install mysql......."
    #subprocess.call(["zypper","install","mysql-community-server])
    #subprocess.call(["zypper","install","postfix","postfix-mysql","mysql-community server"])
    #subprocess.call(["systemctl","enable","mysql.service"])
    #subprocess.call(["rcmysql","reload"])
    #subprocess.call(["mysql","secure","installation"])
    print "Installing apache2......"
    #subprocess.call(["zypper","install","apache2"])
    #subprocess.call(["systemctl","enable","apache2.service"])
    #subprocess.call(["rcapache2","reload"])
    print "Installing php5........"
    #subprocess.call(["zypper","install","apache2-mod_php-5"])
    #subproces.call(["rcapache2","reload"])
def testmatch():
    file_info_php=open('/srv/www/htdocs/info.php', 'w')  
    
if __name__ == "__main__":
     main()
     testmatch()
