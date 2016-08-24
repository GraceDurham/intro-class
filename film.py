from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

for film in json_obj:
	if film["release_year"] == "2000":
		print film["title"]
