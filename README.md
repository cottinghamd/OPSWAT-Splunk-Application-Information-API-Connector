# OPSWAT-Splunk-Application-Information-API-Connector
This Add-On Provides 'Drag and Drop' integration between Splunk and v3 of the OPSWAT Application Information public API.

Information about the OPSWAT Application Information public API can be found here: 
https://www.opswat.com/products/metadefender/application-and-threat-intelligence-platform
https://onlinehelp.opswat.com/mdcloud/Application_Information_Lookup.html

Simply pass a MD5/SHA1/SHA256 hash to this application from a triggered alert and the handler will query the OPSWAT Application Information API and write a result to the index you have specified.

You must have an OPSWAT API key to use this Add-On and this Add-On must be configured after installation.

Note: This application is a community developed application and is not affiliated with OPSWAT. This was made to help the Splunk community easily integrate with the OPSWAT public API. 

This Add-On Requires Splunk CIM to be installed for operation: https://splunkbase.splunk.com/app/1621/
