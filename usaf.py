# Simple python screen scraper to massively extract data from Universal Service Administrative Company's (USAC) Funding Request Data Retrieval Tool
# Loops throw all years and all available states and downloads data files

# importing libs
#import re
#import BeautifulSoup
#import csv
import mechanize
import cookielib
import cgi
import re

br = mechanize.Browser() #initalize mech

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
#br.set_all_readonly(False)

# Follows refresh 0 but not hangs on refresh > 0
#br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

response = br.open("http://www.slforms.universalservice.org/DRT/Default.aspx") #open link to USAC tool
br.select_form("aspnetForm") #form name
#br.select_form(nr=0)
#print br.form
#br.set_all_readonly(False)
#br.find_control("btnSearch").disabled = True

#for form in br.forms():
#       print form

# get all values for states and munis
# to eventually loop over them
#states = br.form.possible_items("ctl00$ContentPlaceHolder$ddlState")

print [form for form in br.forms()][0]

#for control in br.form.controls:
#    print control
#    print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

# Controls can be found by name
#control = br.form.find_control("controlname")

br.form.new_control('hidden', '__EVENTTARGET', {'value':''})
br.form.new_control('hidden', '__EVENTARGUMENT', {'value':''})
#br.form.fixup()


br["ctl00$ContentPlaceHolder$ddlFundingYear"] = ["2012"] # year 1998-2013 (required)
br["ctl00$ContentPlaceHolder$ddlState"] = ["AK"]# state abbreviation (required)

#filter specific
#br["ctl00$ContentPlaceHolder$BEN"] = [""]
#br["ctl00$ContentPlaceHolder$SPIN"] = [""]

#filter service type
#br["ctl00$ContentPlaceHolder$cblServiceType$0"] = ["on"] #telcom
#br["ctl00$ContentPlaceHolder$cblServiceType$1"] = ["on"] #internet access
#br["ctl00$ContentPlaceHolder$cblServiceType$2"] = ["on"] #internal connections
#br["ctl00$ContentPlaceHolder$cblServiceType$3"] = ["on"] #basic maintenance


#filter application type
#br["ctl00$ContentPlaceHolder$cblAppType$0"] = ["on"] #school
#br["ctl00$ContentPlaceHolder$cblAppType$1"] = ["on"] #school district
#br["ctl00$ContentPlaceHolder$cblAppType$2"] = ["on"] #library
#br["ctl00$ContentPlaceHolder$cblAppType$3"] = ["on"] #consortium
#br["ctl00$ContentPlaceHolder$cblAppType$4"] = ["on"] #statewide

#filter specifics
#br["ctl00$ContentPlaceHolder$AppNum471"] = [""]
#br["ctl00$ContentPlaceHolder$FRN"] = [""]
#br["ctl00$ContentPlaceHolder$WAVE_NO"] = [""]
#br["ctl00$ContentPlaceHolder$APPEALS_WAVE_NO"] = [""]
br["ctl00$ContentPlaceHolder$rblReportFormat"] = ["tsv"]

br["ctl00$ContentPlaceHolder$cbSelectDatapoints"] = ["on"] #"on" to select more data
#br["ctl00$ContentPlaceHolder$cbAll"] = ["on"] #"on" to select ALL data

#br["ctl00$ContentPlaceHolder$bSearch"] = ["Build Data File!"]
#br["ctl00$ContentPlaceHolder$bSearch"] = ["Create Standard Report"]

response = br.submit().read()
#response = br.submit(name="ctl00$ContentPlaceHolder$bSearch")
#print response
#print response.get_data()
#print response.info()

#request = br.click()
#for k,v in cgi.parse_qsl(request.get_data()):
#    print (k,v)
#response = br.open(request)
#html = response.read()
#print html

#loop thru states and years
#states = ["AL","AR","AS","AZ","CA","CO","CT","DC","DE","FL","GA","GU","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MP","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VA","VI","VT","WA","WI","WV","WY"]
#for year in range(1998,2014):
 # for state in states:
	#br["ctl00$ContentPlaceHolder$ddlFundingYear"] = [year] # year 1998-2013 (required)
	#br["ctl00$ContentPlaceHolder$ddlState"] = [state]# state abbreviation (required)

	#options and switches

	# filter format: tsv, excel, xml
	#br["ctl00$ContentPlaceHolder$rblReportFormat:"] = "tsv"

	#what data?
	#br["ctl00_ContentPlaceHolder_cbSelectDatapoints:] 
	#br["ctl00_ContentPlaceHolder_cbAll:"]

	#make it happen
	#br["ctl00$ContentPlaceHolder$bSearch:"] = "Build Data File!"

	#response = br.submit().read()
	#time.sleep(6) #wait to not kill things