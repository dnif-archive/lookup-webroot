## WEBROOT BRIGHTCLOUD® THREAT INTELLIGENCE   
 https://www.webroot.com/us/en/business/threat-intelligence

### Overview

Webroot is one of the largest privately held internet security organisations based in the United States with operations spanning across the globe. Webroot's BrightCloud Service helps network and security vendors augment their customer’s security by adding a dynamic service to their defences.
 
The BrightCloud Service is powered by the Webroot® Threat Intelligence Platform, which uses a big data architecture to provide the most comprehensive and accurate threat intelligence available today, including up-to-the-minute intelligence on IP addresses of emerging threats. This intelligence can be used to block traffic from TOR (the onion routing) nodes, proxies, botnets, and other malicious actors. This service also provides information such as historical and geolocation data to help security admins make better threat management decisions.

Given below, is a list of available services:

#### Web Classifications
Provides content classification for billions of webpages to keep users safe from online threats.

#### Web Reputation
Forecasts the security risk of visiting a website and enables administrators to fine tune their security settings. 

#### IP Reputation
Provides critical intelligence on high-risk IP addresses.

#### File Reputation
Provides a dynamic list of file reputation intelligence, such as required signatures for known malicious files and whitelisted files to stop the distribution of malware.

### PRE-REQUISITES to use Webroot (BRIGHTCLOUD THREAT INTELLIGENCE) and DNIF  
Outbound access required to resolve Webroot (BRIGHTCLOUD THREAT INTELLIGENCE) API

| Protocol   | Source IP  | Source Port  | Direction	 | Destination Domain | Destination Port  |  
|:------------- |:-------------|:-------------|:-------------|:-------------|:-------------|  
| TCP | DS,CR,A10 | Any | Egress	| github.com | 443 |
| TCP | DS,CR,A10 | Any | Egress	| brightcloud.com | 443 |

### Webroot (BRIGHTCLOUD THREAT INTELLIGENCE) lookup plugin functions
 
This section explains the details of the functions that can be used with the Webroot Brightcloud lookup plugin.

#### Reputation and popularity 
The reputation score classification for URL(s) and IP addresses is as given below

|Score Range       | Description  |
|:------------- |:-------------|
|  1 - 20 | High Risk |
| 21 – 40 | Suspicious |
| 41 – 60 | Moderate Risk |
| 61 – 80 | Low Risk |
| 81 – 100 | Trustworthy |

The popularity classification for URL(s) is as given below

|Popularity        | Description  |
|:------------- |:-------------|
| 1  | Site ranking is in top 100,000 sites |
| 2  | Site ranking is in top 1 million sites |
| 3  | Site ranking is in top 10 million sites |
| 4  | Site ranking lower than top 10 million sites |
| 5  | Unranked site |

For URL category description and IP blacklist reputation category, refer the links given below  
[IP blacklist reputation category](https://drive.google.com/file/d/1OW7pEC1CIBTHf0VSGBgYmFs8wVuxJ6W5/view?usp=sharing)  
[URL category descriptions](https://drive.google.com/file/d/1V9ML1yAmPBaSIC9nDxoH8M4_YtBVBq7v/view?usp=sharing)

#### Note

In all the functions explained below, the examples use an event store named **threatsample**.  
**This event store does not exist in DNIF by default**. However, it can be created/imported.


### get_url_info 
This function returns information about the reputation and content classification of the queried URL.
#### Input 
- URL        

#### Example
```
_fetch $Url from threatsample limit 1
>>_lookup webroot get_url_info $Url
```

#### Output 
The output of the query is as shown below
![get_urlinfo](https://user-images.githubusercontent.com/37173181/40767527-65864d5c-64d0-11e8-8883-62996b6dc470.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIa1cat      | A value of a1cat = 1 indicates that the entire authority (all paths) is of the same category. This enables more efficient caching |
| $BCTIReputation      | <ul><li>Reputation score of the queried URL</li><li> [Refer to the Reputation and popularity section](#reputation-and-popularity) for details on reputation score classification</li></ul> |
| $BCTILCP | Least common part of the queried URL |
| $BCTICategoryId | Positive integer representing the category ID |
| $BCTICategoryconfidence | Confidence score of the category assigned to this URL |
| $BCTIAPIStatus | API status code of the request |


###  get_url_repinfo

This function returns information about the reputation of the URL (for example country, popularity, age and so on).

#### Input 
- URL

#### Example
```
_fetch $Url from threatsample limit 1
>>_lookup webroot get_url_repinfo $Url
```

#### Output 
The output of the query is as shown below
![get_urlrepinfo](https://user-images.githubusercontent.com/37173181/41393970-bed98e50-6fc5-11e8-9cde-651451da9b41.jpg)

The output of the lookup call has the following structure (for the available data)

 | Fields        | Description  |
|:------------- |:-------------|
| $BCTIAge      | Number of months since Webroot (BrightCloud) has known about this authority |
| $BCTICountry | Two-letter country ID |
| $BCTIPopularity | <ul><li>Popularity category of the URL </li><li> [Refer to the Reputation and popularity section](#reputation-and-popularity) for details on reputation score classification</li></ul> |
| $BCTIReputation      | <ul><li>Reputation score of the queried URL</li><li> [Refer to the Reputation and popularity section](#reputation-and-popularity) for details on reputation score classification</li></ul> ||
| $BCTIThreatHistory | <ul><li>Number of times this site has had a security event/incident in the past 12 months</li><li>It is at least 1 for current security-compromised sites</li></ul> |
| $BCTIAPIStatus | API status code of the request |


### get_url_whoisinfo

This function returns summarized WHOIS information for the URL.

#### Input 
- URL 

#### Example
```
_fetch $Url from threatsample limit 1
>>_lookup webroot get_url_whoisinfo $Url
```
#### Output
Click [here](https://drive.google.com/file/d/11EvQPXkZAR1Xe39C0UWWwpvMSPHZZiJX/view?usp=sharing) to view the output of the above example. 

The output of the lookup call has the following structure (for the available data)  

 | Fields        | Description  |
|:------------- |:-------------|
| $BCTIAuditUpdateDate | Audit update date |
| $BCTIContactEmail | Email address of the URL’s contact person  |
| $BCTICreatedDate | Creation date of the URL’s domain  |
| $BCTIDomainName | Domain name|
| $BCTIExpiresDate | Expiry date of the URL’s domain  |
| $BCTINameServers | Associated nameservers’ details   |
| $BCTIRegistrantCity  | City of the registrant |
| $BCTIRegistrantCountry | Country of the registrant |
| $BCTIRegistrantEmail  | Email address of the registrant  |
| $BCTIRegistrantName  |  Name of the registrant  |
| $BCTIRegistrantOrganization  | Organization that the registrant belongs to  |
| $BCTIRegistrantPostalCode  | Postal code of the registrant  |
| $BCTIRegistrantState  | State of the registrant   |
| $BCTIRegistrantStreet  | Street of the registrant  |
| $BCTIRegistrantTelephone  | Telephone number of the registrant  |
| $BCTIRegistrarName  | Name of the registrar  |
| $BCTIStandardRegCreatedDate  | Creation date of the standard registry |
| $BCTIStandardRegExpiresDate | Expiry date of the standard registry  |
| $BCTIStandardRegUpdatedDate | Updation date of the standard registry  |
| $BCTIAPIStatus | API status code of the request |

### get_url_whoisinfofull

This function returns the  full (detailed) WHOIS information of the URL
#### Input 
- URL 
#### Example
```
_fetch $Url from threatsample limit 1
>>_lookup webroot get_url_whoisinfofull $Url
```
##### Output 

Click [here](https://drive.google.com/file/d/1Db5aht1vC3KyjnNr4F38HI1dCgFg33t_/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

 | Fields        | Description  |
|:------------- |:-------------|
| $BCTIAdministrativeContactCity | City of the administrative contact |
| $BCTIAdministrativeContactCountry | Country of the administrative contact|
| $BCTIAdministrativeContactEmail | Email address of the administrative contact |
| $BCTIAdministrativeContactFax | Fax number of the administrative contact |
| $BCTIAdministrativeContactFaxext | Fax extension number of the administrative contact |
| $BCTIAdministrativeContactName |  Name of the administrative contact|
| $BCTIAdministrativeContactOrganization | Organization that the administrative contact belongs to |
| $BCTIAdministrativeContactPostalCode | Postal code of the administrative contact |
| $BCTIAdministrativeContactState | State of the administrative contact |
| $BCTIAdministrativeContactStreet1 |  Street address line 1 of the administrative contact |
| $BCTIAdministrativeContactStreet2 |  Street address line 2 of the administrative contact |
| $BCTIAdministrativeContactStreet3 |  Street address line 3 of the administrative contact |
| $BCTIAdministrativeContactStreet4 |  Street address line 4 of the administrative contact |
| $BCTIAdministrativeContactTelephone |  Telephone number of the administrative contact |
| $BCTIAdministrativeContactTelephoneExt | Extension number of the administrative contact |
| $BCTIAuditUpdateDate | Audit update date |
| $BCTIContactEmail | Email address of the contact person |
| $BCTICreatedDate | Creation date of the URL’s domain  |
| $BCTIUpdatedDate | Updation date for the URL’s domain  |
| $BCTIExpiresDate | Expiry date of the URL’s domain |
| $BCTIDomainName | Domain name |
| $BCTINameServers | Associated nameservers’ details   |
| $BCTIRegistrantCity  | City of the registrant |
| $BCTIRegistrantCountry | Country of the registrant |
| $BCTIRegistrantEmail  | Email address of the registrant  |
| $BCTIRegistrantFax | Fax details of registrant |
| $BCTIRegistrantFaxext | Fax extension number of the registrant |
| $BCTIRegistrantName  |  Name of the registrant  |
| $BCTIRegistrantOrganization  | Organization that the registrant belongs to  |
| $BCTIRegistrantPostalCode  | Postal code of the registrant  |
| $BCTIRegistrantState  | State of the registrant   |
| $BCTIRegistrantStreet1  | Street address line 1 of the registrant  |
| $BCTIRegistrantStreet2  | Street address line 2 of the registrant  |
| $BCTIRegistrantStreet3  | Street address line 3 of the registrant  |
| $BCTIRegistrantStreet4  | Street address line 4 of the registrant  |
| $BCTIRegistrantTelephone  | Telephone number of the registrant  |
| $BCTIRegistrantTelephoneext  | Telephone extension number of the registrant   |
| $BCTIRegistrantPostalCode | Postal code of registrant |
| $BCTIWhoIsServer | Name of the WHOIS server |
| $BCTIRegistrarName  | Name of the Registrar  |
| $BCTIStandardRegCreatedDate  | Standard registry creation date |
| $BCTIStandardRegExpiresDate | Standard registry expiry date |
| $BCTIStandardRegUpdatedDate | Standard registry updation date  |
| $BCTIstatus | Status of the URL’s domain |
| $BCTIAPIStatus | API status code of the request |

### get_phishingscore

This function returns the phishing score of the object. As this is a synchronous call, the server waits for all the URIs to be processed before responding to the request.
#### Input 
- URL or IP address    
#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_phishingscore $SrcIP
```
#### Output 
The output of the query is as shown below  
![get_phishingscore](https://user-images.githubusercontent.com/37173181/41521924-b0e67cb6-72f1-11e8-8da4-cf85a5c188da.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIPhishScore   | <ul><li>Threat level returned by BCTI (between 1 and 100)</li><li>The higher the score, the higher is the probability that the URL is a phishing site</li></ul>|
| $BCTIPhishTarget  | Target of the phishing attack |
| $BCTIAPIStatus| API status code of the request |


### submit_phishquery 
This function returns a phish response ticket corresponding to the request. It asynchronously passes a URI (URL or IP address) as a parameter and gets a ticket as the response. This ticket can be stored and used  to get the actual phishing score later.

#### Input 
- URL or IP address

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot submit_phishquery $SrcIP
>>_store in_disk wbticket stack_replace
```
#### Output 
The output of the query is as shown below  
![get_submitphishquerywithstore](https://user-images.githubusercontent.com/37173181/41522871-8d827e6a-72f5-11e8-8610-1fa24f65d851.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIPhishRequestTicket  | Phish response ticket that can be used later to get the phishing score  |
| $BCTIAPIStatus| API status code of the request |

#### Note 
The $BCTIPhishRequestTicket returned by this function can be stored in DNIF  using the _store directive. 
This can be used later, with the get_phishqueryresponse function, to get the phishing score of the URI.
            
### get_phishqueryresponse 
This function returns the phishing score of a URI using the $BCTIPhishRequestTicket obtained earlier using the submit_phishquery function.

#### Input 
- Ticket number of the phishing request (string)

#### Example
```
_retrieve wbticket 
>>_lookup webroot get_phishqueryresponse $BCTIPhishRequestTicket
```
#### Output 
The output of the query is as shown below
![get_phishqueryresponse](https://user-images.githubusercontent.com/37173181/41523643-6421825c-72f8-11e8-9c9b-b9d122ddca45.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIPhishScore   | <ul><li>Threat level returned by BCTI (between 1 and 100)</li><li>The higher the score, the higher is the probability that the URL is a phishing site</li></ul> |
| $BCTIPhishTarget  | Target of phishing |
| $BCTIAPIStatus| API status code of the request |

#### Note 
Using the _retrieve directive in DNIF ,the stored ticket from the submit_phishquery endpoint is used as an input parameter to retrieve information from this endpoint.

### get_ip_info  
This function returns information about the reputation and content classification of the queried IP address
#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_ip_info $SrcIP

```
#### Output 
The output of the query is as shown below
![get_ip_info](https://user-images.githubusercontent.com/37173181/41530733-c4780f48-730e-11e8-90aa-31c1990e039a.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIIPInt    | Integer representation of the specified IP address |
| $BCTIIPStatus | <ul><li>Threat status of the IP address</li><li>1:  IP address is in the threat IP list</li><li>0: IP address is not in the threat IP list</li></ul> |
| $BCTICurrentReleaseDate | <ul><li>Date when the threat IP is removed from the Threat IP list</li><li>This field is empty if the IP address is no longer in the threat IP list.</li></ul> |
| $BCTIDomain | <ul><li>omain name corresponding to the IP address (as per the Webroot Master DB)</li><li>This field is empty if the unique domain name is not present in the Master DB</li></ul> |
| $BCTIDomainAge | <ul><li>Age of the unique domain name of the IP address (as per the Webroot Master DB) since the discovery of the domain by Webroot</li><li>This field is empty if the is not present in the Master DB</li></ul> |
| $BCTIFirstReleaseDate | Date when the IP address was released for the first time from the threat IP list |
| $BCTILastReleaseDate  | Date when the IP address was released for the last time from the threat IP list  |
| $BCTIThreatCount  | Number of times the IP address has appeared on the threat IP list  |
| $BCTIThreatMask  | <ul><li>Information on specific threat(s) associated with the requested IP address </li><li>The bit number corresponds with the Threat Mask category </li></ul>  |
| $BCTIReputation  | <ul><li>Reputation score (between 1 and 100) of this IP address</li><li> [Refer to the Reputation and popularity section](#reputation-and-popularity) for details on reputation score classification</li></ul> |
| $BCTIAPIStatus| API status code of the request |


### get_ip_geoinfo  
This function returns geographical information of the queried IP address.

#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_ip_geoinfo $SrcIP
```
#### Output


Click [here](https://drive.google.com/file/d/1KpBZxloQ3OT29lzb3H3TwJpuhATDFX8y/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIASN    | Autonomous system number of this IP address |
| $BCTICarrier | Carrier of this IP address |
| $BCTICity | City of this IP address |
| $BCTICountry | Country of this IP address |
| $BCTIRegion  | Region of this IP address  |
| $BCTIState  | State of this IP address  |
| $BCTILatitude | Latitude of this IP address  |
| $BCTILongitude | Longitude of this IP address |
| $BCTIOrganization  | Organization that this IP address belongs to  |
| $BCTISecondLevelDomain  | Second-level domain of this IP address |
| $BCTITopLevelDomain | Top-level domain of this IP address |
| $BCTIAPIStatus| API status code of the request |

### get_ip_threathistory
The function returns the threat history of the queried IP address.

#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_ip_threathistory $SrcIP
```

#### Output

Click [here](https://drive.google.com/file/d/1DoSttzPMvL2I7rpMSRWc3ZLPNz1Ll9tR/view?usp=sharing) to view the output of the above example.
The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIThreatTypes    | Different types of threats detected on specified IP address |
| $BCTIThreatCount | Count of detected threats on specified IP address |
| $BCTIAPIStatus| API status code of the request |

The report can also include additional fields depending on positive threat detections. For example, an IP address identified as a threat of type botnets would have the following field(s)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIThreatTypeBotnets | List of timestamps when the IP address was seen as a botnet  |


### get_ip_rephistory
This function returns the historic reputation score for the requested IP address. Prior to September 27, 2015 the reputation scoring was being rounded. Post that date, the reputation score can have decimal values. A new scoring history is recorded for an IP address only if the change in reputation score exceeds a preset threshold or, if there is a change in threat status (threat/non-threat).

#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_ip_rephistory $SrcIP
```
#### Output

Click [here](https://drive.google.com/file/d/1sV8Vhqe0AZhBkn26W7QU1nYeSe_aaovy/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIAverageReputation   | <ul><li>Decimal number representing the average reputation score of the IP address </li><li> [Refer to the Reputation and popularity section](#reputation-and-popularity) for details on reputation score classification</li></ul> |
| $BCTIHistoryCount | Number of times the IP address’ reputation score has been recorded |
| $BCTIMaxReputation | Highest recorded reputation score of the IP address |
| $BCTIMinReputation | Lowest recorded reputation score of the IP address |
| $BCTIReputationHighRisk | List of timestamps from when the IP address had a high risk reputation score  |
| $BCTIReputationSuspicious | List of timestamps from when the IP address had a suspicious reputation score  |
| $BCTIReputationTrustworthy | List of timestamps from when the IP address had a trustworthy reputation |
| $BCTIAPIStatus| API status code of the request |


### get_file_info
This function returns  information about a file based on its binary MD5 hash.

#### Input 
- MD5 hash (string)
#### Example
```
_fetch $Filehash from threatsample where $Filehash=ec8c89aa5e521572c74e2dd02a4daf78 limit 1
>>_lookup webroot get_file_info $Filehash
```
#### Output

Click [here](https://drive.google.com/file/d/1i50yeKcTShvKZC7Gu8K7cMwzpv6zzgTl/view?usp=sharing) to view the output of the above example.
The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIDeterminationDate   | Determination (classification) timestamp of this file |
| $BCTIDeterminationType | Determination type (Bad or Good) |
| $BCTIFileSize | File size in bytes |
| $BCTIFirstSeen | First time the MD5 was detected |
| $BCTIMalwareGroup | Malware group of the file |
| $BCTIMd5 | MD5 hash of the file |
| $BCTIPropagationCount | Scaled approximation of the propagation of the file |
| $BCTIAPIStatus| API status code of the request  |


### get_contextual_domainstats
This function returns extended contextual information for the domain. The response contains the counts of related entities (for example virtually hosted domains, sub-domains) grouped by different threat levels (0-4). 

#### Input 
- Domain name    

#### Example
```
_fetch $Domain from threatsample limit 1
>>_lookup webroot get_contextual_domainstats $Domain

```
#### Note 
The reputation score classification of a domain is as given below

| Reputation range       | Threat level |
|:------------- |:-------------|
|  1 - 20 | Level 0 |
| 21 – 40 | Level 1 |
| 41 – 60 | Level 2 |
| 61 – 80 | Level 3 |
| 81 – 100 | Level 4 |

#### Output

Click [here](https://drive.google.com/file/d/1ATqHzdvghvuYjAPJFxqBkVlLAIAirJVy/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTICommonRegistrantThreatLevel0 | Number of domains, at threat level 0, that share the same registrant information with this domain |
| $BCTICommonRegistrantThreatLevel1 | Number of domains, at threat level 1, that share the same registrant information with this domain |
| $BCTICommonRegistrantThreatLevel2 | Number of domains, at threat level 2, that share the same registrant information with this domain |
| $BCTICommonRegistrantThreatLevel3 | Number of domains, at threat level 3, that share the same registrant information with this domain  |
| $BCTICommonRegistrantThreatLevel4 | Number of domains, at threat level 4, that share the same registrant information with this domain |
| $BCTIVirtuallyHostedThreatLevel0 | Number of virtually hosted domains, at threat level 0, that share the same virtual host with this domain |
| $BCTIVirtuallyHostedThreatLevel1 | Number of virtually hosted domains, at threat level 1, that share the same virtual host with this domain |
| $BCTIVirtuallyHostedThreatLevel2| Number of virtually hosted domains, at threat level 2, that share the same virtual host with this domain |
| $BCTIVirtuallyHostedThreatLevel3| Number of virtually hosted domains, at threat level 3, that share the same virtual host with this domain |
| $BCTIVirtuallyHostedThreatLevel4| Number of virtually hosted domains, at threat level 4, that share the same virtual host with this domain |
| $BCTIHostingIPsThreatLevel0 | Number of IP addresses, at threat level 0, that host this domain |
| $BCTIHostingIPsThreatLevel1 | Number of IP addresses, at threat level 1, that host this domain |
| $BCTIHostingIPsThreatLevel2 | Number of IP addresses, at threat level 2, that host this domain |
| $BCTIHostingIPsThreatLevel3 | Number of IP addresses, at threat level 3, that host this domain |
| $BCTIHostingIPsThreatLevel4 | Number of IP addresses, at threat level 4, that host this domain |
| $BCTIHostedAppsThreatLevel0 | Number of mobile applications, at threat level 0, hosted on this domain |
| $BCTIHostedAppsThreatLevel1 | Number of mobile applications, at threat level 1, hosted on this domain |
| $BCTIHostedAppsThreatLevel2 | Number of mobile applications, at threat level 2, hosted on this domain |
| $BCTIHostedAppsThreatLevel3 | Number of mobile applications, at threat level 3, hosted on this domain |
| $BCTIHostedAppsThreatLevel4 | Number of mobile applications, at threat level 4, hosted on this domain |
| $BCTIHostedFilesThreatLevel0  | Number of files, at threat level 0, hosted on this domain |
| $BCTIHostedFilesThreatLevel1  | Number of files, at threat level 1, hosted on this domain |
| $BCTIHostedFilesThreatLevel2  | Number of files, at threat level 2, hosted on this domain |
| $BCTIHostedFilesThreatLevel3  | Number of files, at threat level 3, hosted on this domain |
| $BCTIHostedFilesThreatLevel4  | Number of files, at threat level 4, hosted on this domain |
| $BCTISubDomainsThreatLevel0  | Number of sub-domains, at threat level 0, under this domain  |
| $BCTISubDomainsThreatLevel1  | Number of sub-domains, at threat level 1, under this domain  |  
| $BCTISubDomainsThreatLevel2  | Number of sub-domains, at threat level 2, under this domain  |
| $BCTISubDomainsThreatLevel3  | Number of sub-domains, at threat level 3, under this domain  |
| $BCTISubDomainsThreatLevel4  | Number of sub-domains, at threat level 4, under this domain  |
| $BCTIAPIStatus| API status code of the request |



### get_contextual_ipstats
This function returns extended contextual information for the IP address. The response contains the counts of related entities grouped by different threat levels (0-4).

#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_contextual_ipstats $SrcIP
```
#### Note 
Reputation score classification

| Reputation range       | Threat level |
|:------------- |:-------------|
|  1 - 20 | Level 0 |
| 21 – 40 | Level 1 |
| 41 – 60 | Level 2 |
| 61 – 80 | Level 3 |
| 81 – 100 | Level 4 |

#### Output

Click [here](https://drive.google.com/file/d/1F6fBOk_ScCDu1Rh7_fdGnOElxRobGoqf/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIASNThreatLevel0 | Number of IP addresses, at threat level 0, that have the same ASN as this IP address |
| $BCTIASNThreatLevel1 | Number of IP addresses, at threat level 1, that have the same ASN as this IP address |
| $BCTIASNThreatLevel2 | Number of IP addresses, at threat level 2, that have the same ASN as this IP address |
| $BCTIASNThreatLevel3 | Number of IP addresses, at threat level 3, that have the same ASN as this IP address |
| $BCTIASNThreatLevel4 | Number of IP addresses, at threat level 4, that have the same ASN as this IP address |
| $BCTIHostedURLsThreatLevel0 | Number of virtually hosted domains, at threat level 0, that share the same virtual host with this IP address |
| $BCTIHostedURLsThreatLevel1 | Number of virtually hosted domains, at threat level 1, that share the same virtual host with this IP address |
| $BCTIHostedURLsThreatLevel2 | Number of virtually hosted domains, at threat level 2, that share the same virtual host with this IP address |
| $BCTIHostedURLsThreatLevel3 | Number of virtually hosted domains, at threat level 3, that share the same virtual host with this IP address |
| $BCTIHostedURLsThreatLevel4 | Number of virtually hosted domains, at threat level 4, that share the same virtual host with this IP address |
| $BCTIHostedAppsThreatLevel0 | Number of mobile applications, at threat level 0, hosted at this IP address |
| $BCTIHostedAppsThreatLevel1 | Number of mobile applications, at threat level 1, hosted at this IP address |
| $BCTIHostedAppsThreatLevel2 | Number of mobile applications, at threat level 2, hosted at this IP address |
| $BCTIHostedAppsThreatLevel3 | Number of mobile applications, at threat level 3, hosted at this IP address |
| $BCTIHostedAppsThreatLevel4 | Number of mobile applications, at threat level 4, hosted at this IP address |
| $BCTIHostedFilesThreatLevel0  | Number of files, at threat level 0, hosted at this IP address |
| $BCTIHostedFilesThreatLevel1  | Number of files, at threat level 1, hosted at this IP address |
| $BCTIHostedFilesThreatLevel2  | Number of files, at threat level 2, hosted at this IP address |
| $BCTIHostedFilesThreatLevel3  | Number of files, at threat level 3, hosted at this IP address |
| $BCTIHostedFilesThreatLevel4  | Number of files, at threat level 4, hosted at this IP address |
| $BCTIAPIStatus| API status code of the request |


### get_contextual_filestats
This function returns extended contextual information for the file represented by its MD5 string. The response contains the counts of related entities grouped by different threat levels (0-4). For example: the count of outbound ips, hosting ips, and so on.

#### Input 
- MD5 hash (string)

#### Example
```
_fetch $Filehash from threatsample where $Filehash=195a7ef654ca94d9aff5142d139f9486 limit 1
>>_lookup webroot get_contextual_filestats $Filehash
```
### Note 
The reputation score classification of a file hash is as given below

| Reputation range       | Threat level |
|:------------- |:-------------|
|  1 - 20 | Level 0 |
| 21 – 40 | Level 1 |
| 41 – 60 | Level 2 |
| 61 – 80 | Level 3 |
| 81 – 100 | Level 4 |


#### Output

Click [here](https://drive.google.com/file/d/1UTii1OjsCWiEtsZp6c7rcGvIpQlTiW6n/view?usp=sharing) to view the output of the above example.

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIHostingIPsThreatLevel0 | Number of IP addresses, at threat level 0, that host this file |
| $BCTIHostingIPsThreatLevel1 | Number of IP addresses, at threat level 1, that host this file |
| $BCTIHostingIPsThreatLevel2 | Number of IP addresses, at threat level 2, that host this file |
| $BCTIHostingIPsThreatLevel3 | Number of IP addresses, at threat level 3, that host this file |
| $BCTIHostingIPsThreatLevel4 | Number of IP addresses, at threat level 4, that host this file |
| $BCTIHostingURLsThreatLevel0 | Number of URL(s), at threat level 0, that host this file |
| $BCTIHostingURLsThreatLevel1 | Number of URL(s), at threat level 1, that host this file |
| $BCTIHostingURLsThreatLevel2 | Number of URL(s), at threat level 2, that host this file |
| $BCTIHostingURLsThreatLevel3 | Number of URL(s), at threat level 3, that host this file |
| $BCTIHostingURLsThreatLevel4 | Number of URL(s), at threat level 4, that host this file |
| $BCTIOutboundIPsThreatLevel0 | Number of IP addresses, at threat level 0, that this file connects to |
| $BCTIOutboundIPsThreatLevel1 | Number of IP addresses, at threat level 1, that this file connects to |
| $BCTIOutboundIPsThreatLevel2 | Number of IP addresses, at threat level 2, that this file connects to |
| $BCTIOutboundIPsThreatLevel3 | Number of IP addresses, at threat level 3, that this file connects to |
| $BCTIOutboundIPsThreatLevel4 | Number of IP addresses, at threat level 4, that this file connects to |
| $BCTIOutboundURLsThreatLevel0  | Number of URL(s), threat level 0, that this file connects to |
| $BCTIOutboundURLsThreatLevel1  | Number of URL(s), threat level 1, that this file connects to |
| $BCTIOutboundURLsThreatLevel2  | Number of URL(s), threat level 2, that this file connects to |
| $BCTIOutboundURLsThreatLevel3  | Number of URL(s), threat level 3, that this file connects to |
| $$BCTIOutboundURLsThreatLevel4 | Number of URL(s), threat level 4, that this file connects to |
| $BCTIAPIStatus| API status code of the request |


### get_ipthreatinsight
This function returns a list of incidents that cause an IP address to be flagged as malicious. The response contains
- The earliest time the incidents were observed, 
- The duration of  the incidents, 
- Whether the series of incidents was severe enough for the IP to be determined as a threat, 
- The specific type of threat(s) detected, and 
- Any additional, type-dependent details available for the IP address

#### Input 
- IP address 

#### Example
```
_fetch $SrcIP from threatsample limit 1
>>_lookup webroot get_ipthreatinsight $SrcIP
```

#### Output

The output of the query is as shown below
![GET IP THREATINSIGHT](https://user-images.githubusercontent.com/37173181/41598480-e534b7c4-73ed-11e8-9066-2e03f8951414.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIThreatType | Threat found on the queried IP address |
| $BCTIConvictedTime | List of timestamps when the file was convicted  |
| $BCTIHostType  | Hosting IP address (for example ZuesBot, Cnc)   |
| $BCTIHostedURLs  | List of hosting URL(s)  |
| $BCTIIPint  | Integer representation of the requested IP address  |
| $BCTIAPIStatus| API status code of the request |


### get_urlthreatinsight
This function returns a list of files (identified by their md5 hashes) hosted on URL(s) within a specified domain. The response contains the file's threat information, the URL's categorization and reputation information, and the time at which the correlation between the file and the URL was detected.

#### Input 
- URL

#### Example
```
_fetch $Url from threatsample limit 1
>>_lookup webroot get_urlthreatinsight $Url
```
#### Output
The output of the query is as shown below
![urlthreatinsight](https://user-images.githubusercontent.com/37173181/41605632-7546588e-73ff-11e8-88de-4ac122c39d29.jpg)

The output of the lookup call has the following structure (for the available data)

  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIMd5HashDetTypeG | List of hash(es) detected as good and hosted on the queried URL  |
| $BCTIMd5HashDetTypeB | List of hash(es) detected as bad and hosted on the queried URL |
| $BCTIMd5HashDetTypeNU | List of hash(es) detected as not determined and hosted on the queried URL  |
| $BCTIAPIStatus| API status code of the request |


### get_urlthreatinsight_md5
This function returns a list of URL(s) hosting a specified file (identified by its md5 hash). The response contains the file's threat information, the URL's categorization and reputation information, and the time at which the correlation between the file and the URL was detected.

#### Input 
- MD5 hash (string)   

#### Example
```
_fetch $Filehash from threatsample limit 1
>>_lookup webroot get_urlthreatinsight_md5 $Filehash
```

#### Output

Click [here](https://drive.google.com/file/d/1bLbX_P9Z7lEOVUJceM-dUq2icgWmMBMx/view?usp=sharing) to view the output of the above example.
The output of the lookup call has the following structure (for the available data)


  | Fields        | Description  |
|:------------- |:-------------|
| $BCTIDeterminationType | Determination type Possible values: b (bad), g (good) or nu (not determined) |
| $BCTIDeterminationDate | Determination (classification) time of the file  |
| $BCTIFileSize | File size in bytes | 
| $BCTIFirstSeen | Time when the file was last accessed | 
| $BCTIMalwareGroup | Type of malware exhibited by the file | 
| $BCTIFullSourceURL | Full URL (including path) found hosting the file |
| $BCTIPropagationCount  | Scaled approximation of the propagation of the file |
| $BCTIAPIStatus| API status code of the request |


### Using the WEBROOT (BRIGHTCLOUD THREAT INTELLIGENCE) API and DNIF  
The BRIGHTCLOUD THREAT INTELLIGENCE API is found on github at 

  https://github.com/dnif/lookup-webroot

### Getting started with WEBROOT (BRIGHTCLOUD THREAT INTELLIGENCE) API and DNIF

1. ####    Login to your Data Store, Correlator, and A10 containers.  
   [ACCESS DNIF CONTAINER VIA SSH](https://dnif.it/docs/guides/tutorials/access-dnif-container-via-ssh.html)
2. ####    Move to the `/dnif/<Deployment-key>/lookup_plugins` folder path.
```
$cd /dnif/CnxxxxxxxxxxxxV8/lookup_plugins/
```
3. ####   Clone using the following command  
```  
git clone https://github.com/dnif/lookup-webroot.git webroot
```
4. ####   4.Navigate to the `/dnif/<Deployment-key>/lookup_plugins/webroot/` folder path and open the dnifconfig.yml configuration file
  Replace the <Add_your_oemid_here>, <Add_your_deviceid_here>, <Add_your_uid_here> tags with your WEBROOT (BRIGHTCLOUD THREAT INTELLIGENCE) oemid, deviceid and uid respectively
  
```
lookup_plugin:
  BRIGHTCLOUD_OEMID: <Add_your_oemid_here>
  BRIGHTCLOUD_DEVICEID: <Add_your_deviceid_here>
  BRIGHTCLOUD_UID: <Add_your_uid_here>
  
```
