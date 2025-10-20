# Splunk Cloud Addon for Oracle Cloud Infrastructure (OCI)

## Table of Contents
1. [Overview](#arch)
1. [OCI Configuration](#oci-config)
1. [Splunk Cloud Addon Installation and Setup](#splunk-install)
1. [Prerequisites for Splunk Cloud Addon for OCI](#prereqs)
1. [Troubleshooting](#troubleshooting)
1. [Additional Resources](#resources)

## <a name="arch"></a>Overview 

Splunk Cloud Addon for Oracle Cloud Infrastructure

Splunk Cloud users can consume messages from the OCI Logging and Streaming service by authenticating using the Instance Principal feature in your Oracle Cloud Infrastructure deployment. Once connected, users can stream logs from resources in Oracle Cloud Infrastructure (OCI) to an existing or new Splunk Cloud environment.

![OCI Logging Plugin for Splunk Architecture](https://github.com/splunk/Splunk_Cloud_Addon_for_OCI/assets/77514808/643d12b8-c1f3-4444-9815-c1669bba9705)


## <a name="oci-config"></a>OCI Configuration 
### Step 1: Create a Stream
![OCI Stream Setup](https://github.com/splunk/Splunk_Cloud_Addon_for_OCI/assets/77514808/07259f61-fe1b-4d74-9e12-f9cc6183b13d)


Refer the screenshot and the points listed below to to create a stream for log data to be written to for Splunk to collect from.

1. Open the navigation menu. Under **Analytics**, click **Streaming**.
1. Click **Create Stream**.
1. Next, select *Stream Pool* or create a new one.
1. Fill in the Stream Name field with a friendly name for your stream such as *SIEMLogStream*
1. Provide a Retention time to meet your needs.
1. Provide a Number of Partitions, Total Write Rate, and Total Read Rate based on the amount of data you need to process.

### Step 2 (Optional): Enable a Service ex. VCN Flow Log

In this step, You will create a log group and configure an example log using Virtual Cloud Network (VCN) Flow Logs.
![Log Resource Setup](https://github.com/splunk/Splunk_Cloud_Addon_for_OCI/assets/77514808/4475506f-bafc-4a07-bb09-4a0a5219d2c3)


Refer the screenshot and the points listed below to complete Step 1.

1. Open the navigation menu on Oracle Cloud Infrastructure (OCI) console. Under Solutions and Platform, go to Logging, and click on Log Groups.
1. Click Create Log Group
    1. Choose the Compartment where you want to create log group
    1. Choose a Name and Description that can properly identify your log group
1. Click **Create**
1. Next click **Logs**. The Logs page is displayed.
1. Click **Enable Service Log**. The Enable Resource Log panel is displayed.
1. Under *Select Resource*, under **Resource Compartment**, choose a compartment you have permission to work in.
1. Select a service from the Service. For example: Virtual Cloud Network (subnet)
1. Select a resource:
    1. Under *Resource*, select a subnet.
1. Configure the log:
    1. In Log Category select a log category to specify the type of log to create. For this example, you will select Flow Logs (All records)
1. In **Log Name**, type a name for the log. For this example, name it as test-flowlog.
1. Click **Enable Log**.



### Step 3: Create a Service Connector in OCI Logging

Refer the screenshot and the points listed below to complete Step 3 to create a Service Connector in OCI Logging.
![Service Connector Setup](https://github.com/splunk/Splunk_Cloud_Addon_for_OCI/assets/77514808/9a51c329-051d-402f-8239-44c578afa2cf)


1. Open the navigation menu. Under Logging, click **Service Connectors**.
1. Choose the Compartment where you want to create the service connector.
1. Click **Create Connector**.
1. On the Create Service Connector page, fill in the settings as noted below:
    1. **Connector Name:** User-friendly name for the new service connector.
    1. **Description:** Optional identifier.
    1. **Resource Compartment:** The compartment where you want to store the new service connector.
1. Configure Service Connector:
    1. Select Source: Logging
    1. Select Target: Streaming
1. Under configure source connection (_Audit Logs):
    1. Compartment: Select the *(root)* compartment
    1. Log Group: Select *_Audit*
        1. Check: **Include _Audit in subcompartments** to collect all compartment logs 
1. Under configure source connection (Service Log):
    1. Click **++Another Log**
    1. Compartment: Select the compartment that contains your log group.
    1. Log Group: Select the log group created in step 1.
        1. Leave Blank to collect all Logs in the Log Group
        1. Logs: Select the log created in step 1 to collect the single service log.
1. Under configure target connection:
    1. **Compartment**: Select the compartment that contains your stream.
    1. **Stream**: Select the stream created in step 2.

1. If you do not have an inclusive IAM policy, you will see the following message:
    1. *Create default policy allowing this service connector to write to Streaming in compartment*
    1. To resolve this, click the Create button to the right, and it will automatically create a policy for you.

1. To finish the creation click the **Create** button on the left.

### Step 4: Access control

- The Splunk Cloud Addon for OCI supports access by instance principals to avoid storing long-lived tokens. Define a least-privilege policy as shown in the following example:
    1. Create a Dynamic Group with the Splunk Instance: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm
    2. Create an OCI IAM policy like the below
        Allow dynamic-group <Splunk_Dynamic_Group> to use stream-pull in compartment <compartment_of_stream>

## <a name="splunk-install"></a>OCI Configuration Splunk Cloud Addon Installation and Setup
### Step 1: Download the Splunk Cloud Addon for OCI

Download the Splunk Cloud Addon for OCI from [https://splunkbase.com](https://splunkbase.splunk.com/app/7021)

### Step 2: Install the Splunk Cloud Addon on the Splunk Heavy Forwarder (v8 or greater)

Directions: https://docs.splunk.com/Documentation/AddOns/released/Overview/Singleserverinstall

1. Click Install app from file.
1. Locate the downloaded file and click Upload.
1. If Splunk Enterprise prompts you to restart, do so.
1. Verify that the add-on appears in the list of apps and add-ons. You can also find it on the server at $SPLUNK_HOME/etc/apps/<Name_of_add-on>.

### Step 3: Setup the Splunk Cloud Addon in Splunk Cloud

1. On the Splunk console, navigate to **Settings** then **Data Inputs**
1. Click on **OCI Logging Cloud**
1. Click **New** *Refer the screenshot and the points listed below to complete Step 3*

![Splunk OCI Logging Data Input](https://github.com/splunk/Splunk_Cloud_Addon_for_OCI/assets/77514808/a8ba2e19-93fd-45e7-87d2-74b459b1132a)


4. Configure the stream specific information from the information under OCI Configuration or https://docs.oracle.com/en/solutions/logs-stream-splunk/index.html:
    - OCI Logging Stream
        - Input Name - Unique name for the input
        - Stream OCID - OCID of the Stream ex. ocid1.stream.oc1.i.......
        - Stream Endpoint - Endpoint of the Stream ex. https://cell-1.streaming.<regin>.oci.oraclecloud.com
        - OCI Region - OCI region the stream is in ex. us-ashburn-1 (https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm)
    - OCI Authentication Credentials
        - Splunk Cloud Addon uses Instance Principal in OCI Configuration → Step 4: Access Control
            Select Use Instance Principal.  This means the heavy forwarder must be running in OCI.
                
    - More Settings
        - **Worker Processes** - number of partitions in the OCI Stream created in OCI Configuration → Step 2: Create
        - **Message Limit** - number of messages limit default is 10000
        - **Retry Interval** - number of seconds to sleep after getting a backoff request - default is 90 seconds
        - **HTTPS Proxy** - Proxy server information ex. *http://myproxy:port*
        - **Index** - Index for use with the OCI (Oracle Cloud Infrastructure) App for Splunk: https://splunkbase.splunk.com/app/5289/ 
5. Click **Next**


## <a name="preqs"></a>Prerequisites for Splunk Cloud Addon for OCI
### **Supported Systems**: Linux
### **Splunk Version**: 8 or above
### **Deployment Models**: ###
- Customer owned Splunk Heavy Forwarder running on an OCI Compute Instance (Instance Principal authentications) forwarding to:
    - Splunk Cloud

## <a name="troubleshooting"></a>Troubleshooting
- When trying to install the Splunk Cloud Addon for OCI get following: **"Error connecting to /services/apps/local: The read operation timed out"** 
    - Please follow the instructions here [https://community.splunk.com/t5/All-Apps-and-Add-ons/install-add-on-Error-connecting-to-services-apps-local-The-read/m-p/490613](https://community.splunk.com/t5/All-Apps-and-Add-ons/install-add-on-Error-connecting-to-services-apps-local-The-read/m-p/490613)
        ```
        and increase the following timeout in the web.conf
        [settings]
        splunkdConnectionTimeout = 600 
        ```
- Check your Splunk python3 version `$SPLUNK_HOME/bin/python3 --version` is python 3.7.11 or below
-  'Search and Reporting" and search for the following `index=_internal error oci`
    - Authentication Error will appear here
    - Ignore UI related issues


## <a name="resources"></a>Additional Resources
- Visualization App for OCI (Oracle Cloud Infrastructure) App for Splunk: [https://splunkbase.splunk.com/app/5289/](https://splunkbase.splunk.com/app/5289/)

## <a name="licenses"></a>License
Copyright 2024 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, 
software distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
