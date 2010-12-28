import urllib2
import json
import urllib
import md5

### define the account specific information
# find the Access Key under preferences > User Advanced Options
accessKey = '{YOUR ACCESS KEY}'

vtigerserver = '{URL OF YOUR VTIGER SERVER}'

url = '%s/webservice.php' % vtigerserver

username = '{USERNAME}'


### let's set up the session
# get the token using 'getchallenge' operation
values = {'operation':'getchallenge','username': username }
data = urllib.urlencode(values)
req = urllib2.Request('%s?%s' % (url,data))
response = urllib2.urlopen(req).read()
token = json.loads(response)['result']['token']

# use the token to + accesskey to create the tokenized accessKey
key = md5.md5(token + accessKey)
tokenizedAccessKey = key.hexdigest()
values['accessKey'] = tokenizedAccessKey

# now that we have an accessKey tokenized, let's perform a login operation 
values['operation']  = 'login'
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
response = json.loads(response.read())

# set the sessionName
values['sessionName'] = response['result']['sessionName']

### now let's do stuff
# listtypes
values['operation'] = 'listtypes'
data = urllib.urlencode(values)
# added data a parameter here makes this a POST
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
print 'here are the available types'
print json.loads(response.read())

# find out about a particular vTiger Object Type
# we'll look at 'Contacts'
values['operation'] = 'describe'
values['elementType'] = 'Contacts'
data = urllib.urlencode(values)
# must be a get according to docs
# so we append data to url
req = urllib2.Request("%s?%s" % (url,data))
response = urllib2.urlopen(req)
print 'about contacts'
print values
print json.loads(response.read())
