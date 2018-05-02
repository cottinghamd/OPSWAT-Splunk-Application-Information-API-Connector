# encoding = utf-8
def query_url(helper, hashvalue, apikey, themethod):
    import json
    import re, urllib
    from httplib2 import Http
    
    if not hashvalue or not apikey:
        helper.log_error('Some parameters are missing. Required items are apikey and url.')
        return

    uri = 'https://api.metadefender.com/v3/appinfo/''{}'.format(hashvalue)
    http = helper.build_http_connection(helper.proxy, timeout=30)
    data = {
    }
     #No headers needed in this case
    headers = {
    #'header1' : 'header_value'
    'Authorization' : 'apikey {}'.format(apikey)
    }

    resp_headers, content = http.request(uri, method=themethod,
                                     body=urllib.urlencode(data), headers=headers)
    if resp_headers.status not in (200, 201, 204, 404):
        helper.log_error('Failed to query api. url={}, HTTP Error={}, content={}'.format(hashvalue, resp_headers.status, content))
    else:

        helper.log_info('Raw URL Query {}, content={}'.format(hashvalue, content))
        contenttemp = json.loads(content)
        contenttemp['requested'] = hashvalue
        
        if 'data' in contenttemp:
            contenttemp['found'] = 'yes'
        else:
            contenttemp['found'] = 'no'
            
        content = json.dumps(contenttemp)
        return content
        

def process_event(helper, *args, **kwargs):
    helper.log_info("Alert action OPSWAT Application Information Lookup Started")
    
    #query the url from setup
    hashvalue = helper.get_param("hashvalue")
    helper.log_info("hashvalue={}".format(hashvalue))
    #query API Key alert action input
    apikey = helper.get_global_setting("apikey")
    index = helper.get_global_setting("index")
    host = helper.get_global_setting("host")
    source = helper.get_global_setting("source")
    sourcetype = helper.get_global_setting("sourcetype")
    apikey = helper.get_global_setting("apikey")
    #call the query URL REST Endpoint and pass the url and API token
    content = query_url(helper, hashvalue, apikey, 'GET')
    
    #write the response returned by Virus Total API to splunk index
    helper.addevent(content, sourcetype)
    helper.writeevents(index, host, source)
    return 0
