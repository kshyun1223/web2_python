#!python
 
import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
 
os.remove('data/'+pageId)

print("Location: index.py")
print()