import re

input = open("README.md", "r")


def cleanhtml(raw_html):
  cleanr = re.compile('<img.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

cleanedhtml = cleanhtml(input.read())

output =  open("README-striped.md", "w+")
output.write(cleanedhtml)
output.close()
