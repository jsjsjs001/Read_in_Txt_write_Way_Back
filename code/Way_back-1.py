#start: administrator: Anaconda Prompt 
# conda update -n base -c defaults conda

# Installers
#conda install
#    noarch  v3.0.6
#To install this package with conda run: ##
#conda install -c conda-forge waybackpy 
#https://github-wiki-see.page/m/akamhy/waybackpy/wiki/Python-package-docs

#the file “requirements.txt” lists these dependencies, please run “pip install -r requirements.txt” as the first
#step. See https://pip.pypa.io/en/stable/user_guide/#ensuring-repeatability for further instructions on creating
#and using the “requirements.txt” file.

import waybackpy # imported the waybackpy.

from waybackpy import WaybackMachineCDXServerAPI


url = "https://siol.net/novice/slovenija/poslanci-sprejeli-sporno-novole-zakona-o-tujcih-451503"
user_agent = "Your-user-agent"

#cdx = WaybackMachineCDXServerAPI(url=url, user_agent=user_agent)
#izpis vseh instanc
#snapshots = cdx.snapshots()#
#for snapshot in snapshots:#
#    print(snapshot)


wayback = waybackpy.Url(url, user_agent) # created the waybackpy instance.
try:
 #   cdx_api = WaybackMachineCDXServerAPI(url, user_agent)    
#   cdx_api.newest()
    newest = wayback.newest()
#    print(newest)
    print(newest.archive_url)
#    oldest = cdx_api.oldest()
#    print(oldest)
#    print(oldest.archive_url)
    print(wayback.near(year=2017,month=12))
except  waybackpy.exceptions.ArchiveNotInAvailabilityAPIResponse: #waybackpy.exceptions.NoCDXRecordFound :
    print(' WaybackMachine stran ne obstaja! ')
    archive = wayback.save() # saved the link to the internet archive
    print(archive.archive_url) #printed the URL.

# https://medium.com/analytics-vidhya/the-wayback-machine-scraper-63238f6abb66
# primer: https://www.holisticseo.digital/python-seo/internet-archive/ 
# https://www.holisticseo.digital/python-seo/internet-archive/
# vsc github integration
#https://pypi.org/project/waybackpy/
#https://archive.org/help/wayback_api.php 
#https://archive.org/services/docs/api/internetarchive/
#https://www.google.com/search?client=firefox-b-d&q=examples+waybackpy 
# https://www.pythonprogramming.in/natural-language-processing-in-python.html

######################################______________ 
##
#https://www.holisticseo.digital/python-seo/internet-archive/
#https://archive.org/services/docs/api/internetarchive/
#https://medium.com/analytics-vidhya/the-wayback-machine-scraper-63238f6abb66
#https://pypi.org/project/waybackpy/
#
