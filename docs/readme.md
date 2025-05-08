## About the connector
Google Security Operations SOAR (Security Orchestration, Automation, and Response) is a cloud-native platform designed to help security teams detect, investigate, and respond to threats in real time.
<p>This document provides information about the Google SecOps SOAR Connector, which facilitates automated interactions, with a Google SecOps SOAR server using FortiSOAR&trade; playbooks. Add the Google SecOps SOAR Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Google SecOps SOAR.</p>

### Version information

Connector Version: 1.0.0

Authored By: Fortinet CSE

Contributor: Daehyeob Kim

Certified: No

## Installing the connector
<p>From FortiSOAR&trade; 7.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-google-secops-soar`

## Prerequisites to configuring the connector
- You must have the URL of Google SecOps SOAR server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Google SecOps SOAR server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Google SecOps SOAR</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td>Specify the URL of the Google SecOps SOAR server to connect and perform automated operations.<br>
<tr><td>API Key<br></td><td>API Key to access the Google SecOps SOAR endpoint to which you will connect and perform the automated operations.<br>
<tr><td>Verify SSL<br></td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set as True.<br></td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Execute an API Request<br></td><td>Sends an API request to an API endpoint based on specified HTTP method, endpoint, and other input parameters that you have specified, enabling flexible API interactions tailored to user needs.<br></td><td>generic_api_call <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Execute an API Request
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>HTTP Method<br></td><td>Select an HTTP action for the request. You can select from the following options:  

DELETE 

GET 

PATCH 

POST 

PUT 

HEAD 

OPTIONS 

TRACE<br>
</td></tr><tr><td>Endpoint<br></td><td>Specify the target API URL path for the request. For example, if the website is https://example.com and URL path is https://example.com/images/pic.jpg, the endpoint would be /images/pic.jpg.<br>
</td></tr><tr><td>Headers<br></td><td>Specify the headers for the request.<br>
</td></tr><tr><td>Query Parameters<br></td><td>(Optional) Specify any optional parameters to add to the URL and refine the request.<br>
</td></tr><tr><td>Request Payload<br></td><td>(Optional) Specify data, as JSON, to be sent as the request payload.<br>
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:
<code><br>{
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "result": "",
</code><code><br>&nbsp;&nbsp;&nbsp;&nbsp;    "api_data": ""
</code><code><br>}</code>
## Included playbooks
The `Sample - Google SecOps SOAR - 1.0.0` playbook collection comes bundled with the Google SecOps SOAR connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Google SecOps SOAR connector.

- Execute an API Request

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
