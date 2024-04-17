# Detect date in String
# Using python-dateutil()
# Using re.search() + strptime()
import waybackpy # imported the waybackpy.

from waybackpy import WaybackMachineCDXServerAPI

import aifc
  
import re
from datetime import datetime

from dateutil import parser


import re


# Python code to find the URL from an input string
# Using the regular expression
#https://www.geeksforgeeks.org/python-check-url-string/  
def Find(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
      


#outfile = infile[:-4] + "-bak" + infile[-4:]
#doc.save(outfile)


lines = []
with open(r"C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\Python_delovni\gradiva\interd17_p2_sl_v1_r1.txt") as f:
    lines = f.readlines()

    #output 

f_out = open(r"C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\Python_delovni\gradiva\interd17_p2_sl_v1_r2.txt", 'w' )



count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')    
    # Driver Code
#    string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
    Urls = Find(line)
    if Urls:
        print("Urls: ", Urls[0])
        url= Urls[0]
        w_back = ''
    else:
        print("list is empty")
#    print("Urls: ", Find(line))
    # extracting date using inbuilt func.
    # searching string


    x = line.replace(". ", "-")  
    # searching string variata z oklepaji
    #a = [r'\(\d{2}-\d{2}-\d{4}\)', r'\(\d{2}-\d{1}-\d{4}\)', r'\(\d{1}-\d{1}-\d{4}\)', r'\(\d{1}-\d{2}-\d{4}\)']
    #match_str = re.search(r'\(\d{2}-\d{1}-\d{4}\)', x)#    a = [r'\d{2}-\d{2}-\d{4}' , r'\d{2}-\d{1}-\d{4}', r'\d{1}-\d{1}-\d{4}', r'\d{1}-\d{2}-\d{4}']

    # searching string brez oklepajev
    a = [r'\d{2}-\d{2}-\d{4}', r'\d{2}-\d{1}-\d{4}', r'\d{1}-\d{1}-\d{4}', r'\d{1}-\d{2}-\d{4}']
    match_str = re.search(r'\d{2}-\d{1}-\d{4}', x)#    a = [r'\d{2}-\d{2}-\d{4}' , r'\d{2}-\d{1}-\d{4}', r'\d{1}-\d{1}-\d{4}', r'\d{1}-\d{2}-\d{4}']
#    match_str = re.search(r'\d{2}-\d{1}-\d{4}', x)
    while a : # and not match_str:
        ai = (a.pop(-1))
        print(ai)
        m_str = re.search(ai, x)
        print(m_str)
        if  m_str: 
            match_str = m_str 
    #    match_str = re.search(a, x)

    if  match_str:     
        print(match_str)  
        # computed date
        # feeding format
        #varianta z oklepaji
        #res = datetime.strptime(match_str.group(), '(%d-%m-%Y)').date()
        #varianta brez oklepajev
        res = datetime.strptime(match_str.group(), '%d-%m-%Y').date()
        # printing result
        print("Computed date I : "+ str(res))
    else: 
        print('ni našel')  

#        url = "https://nova24tv.si/slovenija/poglejte-kako-se-po-porazu-prepirajo-10-stvari-ki-so-pri-kampanji-za-sle-narobe/"

    #********************wayback part (begin)

    if not Urls:
        # zapisuje out
        f_out.write(line)
#        f_out.write('\n')



    else: # Urls: če so urlji
        print("URLS: test wayback", Urls[0], url)
        user_agent = "Your-user-agent"

        

        try:
#           cdx_api = WaybackMachineCDXServerAPI(url, user_agent)  
            print("try ", Urls[0], url) 

            cdx = WaybackMachineCDXServerAPI(url=url, user_agent=user_agent)
        #izpis vseh instanc
        #snapshots = cdx.snapshots()#
        #for snapshot in snapshots:#
        #    print(snapshot)

            wayback = waybackpy.Url(url, user_agent) # created the waybackpy instance.
#            print(wayback.near(year=2020,month=12))

            if  not match_str:
                newest = cdx.newest()
#    print(newest)
#                print('newest :', newest.archive_url)
                w_back =  newest.archive_url
            else:
#                print('leto' , res.year , ' mesec', res.month, ' dan ', res.day)
#                print('near : ', wayback.near(year=res.year,month=res.month))
                w_back= wayback.near(year=res.year,month=res.month)
                #cdx_api.oldest()
            print('WaybackMachine stran ', w_back)
        #    oldest = cdx_api.oldest()
        #    print(oldest)
        #    print(oldest.archive_url)

        except  waybackpy.exceptions.ArchiveNotInAvailabilityAPIResponse: #waybackpy.exceptions.NoCDXRecordFound :
            w_back =  " WaybackMachine stran ne obstaja! "
            print(' WaybackMachine stran ne obstaja! ')
            archive = wayback.save() # saved the link to the internet archive
            print(archive.archive_url) #printed the URL. 
            w_back = archive.archive_url   

    #********************wayback part (end)
        l = line.strip() + " <" + str(w_back) + ">" 
        f_out.write(l) #line + " <" + str(w_back) + ">" )
#        f_out.write('\n')





# podvojeno od zgoraj
#    match_str = re.search(r'\d{2}. \d{2}. \d{4}', line)
    # computed date
    # feeding format
#    res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
    # printing result
#    print("Computed date : " + str(res))
# to doveč ker druga metoda za datum   
#    try:
#        res = parser.parse(line, fuzzy=True)
  
# printing result
#        print("Computed date : " + str(res)[:10])
#    except parser._parser.ParserError:
#        print("brez datuma : ", f'line {count}: {line}')

# Python3 code to demonstrate working of
# Detect date in String
# Using re.search() + strptime()
#import re
#from datetime import datetime
  
# initializing string
#test_str = "gfg at 2021-01-04"
  
# printing original string
#print("The original string is : " + str(test_str))
  
# searching string
#match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
  
# computed date
# feeding format
#res = datetime.strptime(match_str.group(), '%Y-%m-%d').date()
  
# printing result
#print("Computed date : " + str(res))



# Detect date in String
# Using python-dateutil()
  
# initializing string
#test_str = "gfg at 2021-01-04"
  
# printing original string
#print("The original string is : " + str(test_str))


#textdoc = load(r"C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\Python_delovni\gradiva")
#allparas = textdoc.getElementsByType(text.P)
#for i in range(len((allparas))):
#    a=teletype.extractText(allparas[i])
#    print(a)