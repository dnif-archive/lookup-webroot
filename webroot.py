import requests
import yaml
import requests
import datetime
import os
import json
import sys


path = os.environ["WORKDIR"]

with open(path + "/lookup_plugins/webroot/dnifconfig.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    oemid = cfg['lookup_plugin']['WEBROOT_OEMID']
    deviceid = cfg['lookup_plugin']['WEBROOT_DEVICEID']
    uid = cfg['lookup_plugin']['WEBROOT_UID']


def get_url_info(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getinfo?url='+params+cred+'&reputation=1')
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                tmp_dct = {}
                for dt in json_response['results']:
                    tmp_dct.update(dt['queries']['getinfo'])
            except Exception:
                    pass
            try:
                if tmp_dct['a1cat'] != '':
                    i['$BCTIa1cat'] = tmp_dct['a1cat']
            except Exception:
                pass
            try:
                if tmp_dct['reputation'] != '':
                    i['$BCTIReputation'] = tmp_dct['reputation']
            except Exception:
                pass
            try:
                if tmp_dct['lcp'] != '':
                    i['$BCTILCP'] = tmp_dct['lcp']
            except Exception:
                pass
            try:
                for ct in tmp_dct['cats']:
                    if ct['catid'] != '':
                        i['$BCTICategoryId']=ct['catid']
                    if ct['conf'] != '':
                        i['$BCTICategoryconfidence']=ct['conf']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def get_url_repinfo(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getrepinfo?url='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                tmp_dct={}
                for dt in json_response['results']:
                    tmp_dct.update(dt['queries']['getrepinfo'])
            except Exception:
                pass
            try:
                if tmp_dct['age'] != '':
                    i['$BCTIAge']=tmp_dct['age']
            except Exception:
                pass
            try:
                if tmp_dct['country'] != '':
                    i['$BCTICountry']=tmp_dct['country']
            except Exception:
                pass
            try:
                if tmp_dct['popularity'] != '':
                    i['$BCTIPopularity']=tmp_dct['popularity']
            except Exception:
                pass
            try:
                if tmp_dct['reputation'] != '':
                    i['$BCTIReputation']=tmp_dct['reputation']
            except Exception:
                pass
            try:
                if tmp_dct['threathistory'] != '':
                    i['$BCTIThreatHistory']=tmp_dct['threathistory']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def get_url_whoisinfo(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getwhoisinfo?url='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst ={}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getwhoisinfo'])
            except Exception:
                pass
            try:
                if lst['audit_auditupdateddate'] != '':
                    i['$BCTIAuditUpdateDate']=lst['audit_auditupdateddate']
            except Exception:
                pass
            try:
                if lst['contactemail'] != '':
                    i['$BCTIContactEmail']=lst['contactemail']
            except Exception:
                pass
            try:
                if lst['createddate'] != '':
                    i['$BCTICreatedDate']=lst['createddate']
            except Exception:
                pass
            try:
                if lst['domainname'] != '':
                    i['$BCTIDomainName']=lst['domainname']
            except Exception:
                pass
            try:
                if lst['expiresdate'] != '':
                    i['$BCTIExpiresDate']=lst['expiresdate']
            except Exception:
                pass
            try:
                if lst['nameservers'] != '':
                    i['$BCTINameServers'] = lst['nameservers']
            except Exception:
                pass
            try:
                if lst['registrant_city'] != '':
                    i['$BCTIRegistrantCity'] = lst['registrant_city']
            except Exception:
                pass
            try:
                if lst['registrant_country'] != '':
                    i['$BCTIRegistrantCountry'] = lst['registrant_country']
            except Exception:
                pass
            try:
                if lst['registrant_email'] != '':
                    i['$BCTIRegistrantEmail'] = lst['registrant_email']
            except Exception:
                pass
            try:
                if lst['registrant_name'] != '':
                    i['$BCTIRegistrantName'] = lst['registrant_name']
            except Exception:
                pass
            try:
                if lst['registrant_organization'] != '':
                    i['$BCTIRegistrantOrganization'] = lst['registrant_organization']
            except Exception:
                pass
            try:
                if lst['registrant_postalcode'] != '':
                    i['$BCTIRegistrantPostalCode'] = lst['registrant_postalcode']
            except Exception:
                pass
            try:
                if lst['registrant_state'] != '':
                    i['$BCTIRegistrantState'] = lst['registrant_state']
            except Exception:
                pass
            try:
                if lst['registrant_street1'] != '':
                    i['$BCTIRegistrantStreet'] = lst['registrant_street1']
            except Exception:
                pass
            try:
                if lst['registrant_telephone'] != '':
                    i['$BCTIRegistrantTelephone'] = lst['registrant_telephone']
            except Exception:
                pass
            try:
                if lst['registrarname'] != '':
                    i['$BCTIRegistrarName'] = lst['registrarname']
            except Exception:
                pass
            try:
                if lst['standardregcreateddate'] != '':
                    i['$BCTIStandardRegCreatedDate'] = lst['standardregcreateddate']
            except Exception:
                pass
            try:
                if lst['standardregexpiresdate'] != '':
                    i['$BCTIStandardRegExpiresDate'] = lst['standardregexpiresdate']
            except Exception:
                pass
            try:
                if lst['standardregupdateddate'] != '':
                    i['$BCTIStandardRegUpdatedDate'] = lst['standardregupdateddate']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def get_url_whoisinfofull(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getwhoisinfofull?url='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst ={}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getwhoisinfofull'])
            except Exception:
                pass
            try:
                if lst['administrativecontact_city']!='':
                    i['$BCTIAdministrativeContactCity']=lst['administrativecontact_city']
            except Exception:
                pass
            try:
                if lst['administrativecontact_country'] != '':
                    i['$BCTIAdministrativeContactCountry']=lst['administrativecontact_country']
            except Exception:
                pass
            try:
                if lst['administrativecontact_email'] != '':
                    i['$BCTIAdministrativeContactEmail']=lst['administrativecontact_email']
            except Exception:
                pass
            try:
                if lst['administrativecontact_fax'] != '':
                    i['$BCTIAdministrativeContactFax']=lst['administrativecontact_fax']
            except Exception:
                pass
            try:
                if lst['administrativecontact_faxext'] != '':
                    i['$BCTIAdministrativeContactFaxext']=lst['administrativecontact_faxext']
            except Exception:
                pass
            try:
                if lst['administrativecontact_name'] != '':
                    i['$BCTIAdministrativeContactName']=lst['administrativecontact_name']
            except Exception:
                pass
            try:
                if lst['administrativecontact_organization'] != '':
                    i['$BCTIAdministrativeContactOrganization']=lst['administrativecontact_organization']
            except Exception:
                pass
            try:
                if lst['administrativecontact_postalcode'] != '':
                    i['$BCTIAdministrativeContactPostalCode']=lst['administrativecontact_postalcode']
            except Exception:
                pass
            try:
                if lst['administrativecontact_state'] != '':
                    i['$BCTIAdministrativeContactState']=lst['administrativecontact_state']
            except Exception:
                pass
            try:
                if lst['administrativecontact_street1'] != '':
                    i['$BCTIAdministrativeContactStreet1']=lst['administrativecontact_street1']
            except Exception:
                pass
            try:
                if lst['administrativecontact_street2'] != '':
                    i['$BCTIAdministrativeContactStreet2']=lst['administrativecontact_street2']
            except Exception:
                pass
            try:
                if lst['administrativecontact_street3'] != '':
                    i['$BCTIAdministrativeContactStreet3']=lst['administrativecontact_street3']
            except Exception:
                pass
            try:
                if lst['administrativecontact_street4'] != '':
                    i['$BCTIAdministrativeContactStreet4']=lst['administrativecontact_street4']
            except Exception:
                pass
            try:
                if lst['administrativecontact_telephone'] != '':
                    i['$BCTIAdministrativeContactTelephone']=lst['administrativecontact_telephone']
            except Exception:
                pass
            try:
                if lst['administrativecontact_telephoneext'] != '':
                    i['$BCTIAdministrativeContactTelephone'] = lst['administrativecontact_telephoneext']
            except Exception:
                pass
            try:
                if lst['audit_auditupdateddate'] != '':
                    i['$BCTIAuditUpdatedDate'] = lst['audit_auditupdateddate']
            except Exception:
                pass
            try:
                if lst['contactemail'] != '':
                    i['$BCTIContactEmail'] = lst['contactemail']
            except Exception:
                pass
            try:
                if lst['createddate'] != '':
                    i['$BCTICreatedDate'] = lst['createddate']
            except Exception:
                pass
            try:
                if lst['domainname'] != '':
                    i['$BCTIDomainName'] = lst['domainname']
            except Exception:
                pass
            try:
                if lst['expiresdate'] != '':
                    i['$BCTIExpiresDate'] = lst['expiresdate']
            except Exception:
                pass
            try:
                if lst['nameservers'] != '':
                    i['$BCTINameServers'] = lst['nameservers']
            except Exception:
                pass
            try:
                if lst['registrant_city'] != '':
                    i['$BCTIRegistrantCity'] = lst['registrant_city']
            except Exception:
                pass
            try:
                if lst['registrant_country'] != '':
                    i['$BCTIRegistrantCountry'] = lst['registrant_country']
            except Exception:
                pass
            try:
                if lst['registrant_email'] != '':
                    i['$BCTIRegistrantEmail'] = lst['registrant_email']
            except Exception:
                pass
            try:
                if lst['registrant_fax'] != '':
                    i['$BCTIRegistrantFax'] = lst['registrant_fax']
            except Exception:
                pass
            try:
                if lst['registrant_faxext'] != '':
                    i['$BCTIRegistrantFaxext'] = lst['registrant_faxext']
            except Exception:
                pass
            try:
                if lst['registrant_name'] != '':
                    i['$BCTIRegistrantName'] = lst['registrant_name']
            except Exception:
                pass
            try:
                if lst['registrant_organization'] != '':
                    i['$BCTIRegistrantOrganization'] = lst['registrant_organization']
            except Exception:
                pass
            try:
                if lst['registrant_postalcode'] != '':
                    i['$BCTIRegistrantPostalCode'] = lst['registrant_postalcode']
            except Exception:
                pass
            try:
                if lst['registrant_state'] != '':
                    i['$BCTIRegistrantState'] = lst['registrant_state']
            except Exception:
                pass
            try:
                if lst['registrant_street1'] != '':
                    i['$BCTIRegistrantStreet1'] = lst['registrant_street1']
            except Exception:
                pass
            try:
                if lst['registrant_street2'] != '':
                    i['$BCTIRegistrantStreet2'] = lst['registrant_street2']
            except Exception:
                pass
            try:
                if lst['registrant_street3'] != '':
                    i['$BCTIRegistrantStreet3'] = lst['registrant_street3']
            except Exception:
                pass
            try:
                if lst['registrant_street4'] != '':
                    i['$BCTIRegistrantStreet4'] = lst['registrant_street4']
            except Exception:
                pass
            try:
                if lst['registrant_telephone'] != '':
                    i['$BCTIRegistrantTelephone'] = lst['registrant_telephone']
            except Exception:
                pass
            try:
                if lst['registrant_telephoneext'] != '':
                    i['$BCTIRegistrantTelephoneext'] = lst['registrant_telephoneext']
            except Exception:
                pass
            try:
                if lst['registrarname'] != '':
                    i['$BCTIRegistrarName'] = lst['registrarname']
            except Exception:
                pass
            try:
                if lst['standardregcreateddate'] != '':
                    i['$BCTIStandardRegCreatedDate'] = lst['standardregcreateddate']
            except Exception:
                pass
            try:
                if lst['standardregexpiresdate'] != '':
                    i['$BCTIStandardRegExpiresDate'] = lst['standardregexpiresdate']
            except Exception:
                pass
            try:
                if lst['standardregupdateddate'] != '':
                    i['$BCTIStandardRegUpdatedDate'] = lst['standardregupdateddate']
            except Exception:
                pass
            try:
                if lst['status'] != '':
                    i['$BCTIstatus'] = lst['status']
            except Exception:
                pass
            try:
                if lst['updateddate'] != '':
                    i['$BCTIUpdatedDate'] = lst['updateddate']
            except Exception:
                pass
            try:
                if lst['whoisserver'] != '':
                    i['$BCTIWhoIsServer'] = lst['whoisserver']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def get_url_catlist(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0//url/getcatlist'+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst ={}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getwhoisinfofull'])
            except Exception:
                pass
            try:
                i['$BCTIAdministrativeContactCity']=lst['administrativecontact_city']
            except Exception:
                pass
            try:
                i['$BCTIAdministrativeContactCountry']=lst['administrativecontact_country']
            except Exception:
                pass
            try:
                i['$BCTIAdministrativeContactEmail']=lst['administrativecontact_email']
            except Exception:
                pass
            try:
                if lst['administrativecontact_fax']!='':
                    i['$BCTIAdministrativeContactFax']=lst['administrativecontact_fax']
            except Exception:
                pass
            try:
                i['$BCTIExpiresDate']=lst['expiresdate']
            except Exception:
                pass
            try:
                i['$BCTINameServers'] = lst['nameservers']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantCity'] = lst['registrant_city']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantCountry'] = lst['registrant_country']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantEmail'] = lst['registrant_email']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantName'] = lst['registrant_name']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantOrganization'] = lst['registrant_organization']
            except Exception:
                pass
            try:
                if lst['registrant_postalcode'] != '':
                    i['$BCTIRegistrantPostalCode'] = lst['registrant_postalcode']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantState'] = lst['registrant_state']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantStreet'] = lst['registrant_street1']
            except Exception:
                pass
            try:
                i['$BCTIRegistrantTelephone'] = lst['registrant_telephone']
            except Exception:
                pass
            try:
                i['$BCTIRegistrarName'] = lst['registrarname']
            except Exception:
                pass
            try:
                i['$BCTIRegistrarName'] = lst['registrarname']
            except Exception:
                pass
            try:
                i['$BCTIRegistrarName'] = lst['registrarname']
            except Exception:
                pass
            try:
                i['$BCTIStandardRegCreatedDate'] = lst['standardregcreateddate']
            except Exception:
                pass
            try:
                i['$BCTIStandardRegExpiresDate'] = lst['standardregexpiresdate']
            except Exception:
                pass
            try:
                i['$BCTIStandardRegUpdatedDate'] = lst['standardregupdateddate']
            except Exception:
                pass
            try:
                i['$BCTIStatus']=json_response['status']
            except Exception:
                pass
    return json_response


def get_phishingscore(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getphishscore?url='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getphishscore'])
            except Exception:
                pass
            try:
                if lst['score']!='':
                    i['$BCTIPhishScore']=lst['score']
                if lst['target']!='':
                    i['$BCTIPhishTarget']=lst['target']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def submit_phishquery(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/submitphishquery?url='+params+cred+'&reputation=1')
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['submitphishquery'])
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
            try:
                i['$BCTIPhishRequestTicket']=lst['phishrequestticket']
            except Exception:
                pass

    return inward_array


def get_phishqueryresponse(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/url/getphishqueryresponse?url='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getphishscore'])
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
            try:
                if lst['score'] !='':
                    i['$BCTIPhishScore']=lst['score']
            except Exception:
                pass
            try:
                if lst['target']!='':
                    i['$BCTIPhishTarget']=lst['target']
            except Exception:
                pass
    return inward_array


def get_ip_info(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getinfo?ip='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getinfo'])
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
            try:
                i['$BCTIIPStatus']=lst['ip_status']
            except Exception:
                pass
            try:
                i['$BCTIIPInt']=lst['ipint']
            except Exception:
                pass
            try:
                cr_dt = datetime.datetime.utcfromtimestamp(lst['current_release_date']).strftime('%Y-%m-%d %H:%M:%S')
                i['$BCTICurrentReleaseDate']=cr_dt
            except Exception:
                pass
            try:
                if str(i[var_array[0]])!=lst['domain']:
                    i['$BCTIDomain'] = lst['domain']
            except Exception:
                pass
            try:
                if str(i[var_array[0]]) != lst['domain']:
                    i['$BCTIDomainAge'] = lst['domain_age']
            except Exception:
                pass
            try:
                fr_dt = datetime.datetime.utcfromtimestamp(lst['first_release_date']).strftime('%Y-%m-%d %H:%M:%S')
                i['$BCTIFirstReleaseDate'] = fr_dt
            except Exception:
                pass
            try:
                lst_dt = datetime.datetime.utcfromtimestamp(lst['last_release_date']).strftime('%Y-%m-%d %H:%M:%S')
                i['$BCTILastReleaseDate'] = lst_dt
            except Exception:
                pass
            try:
                i['$BCTIThreatCount'] = lst['threat_count']
            except Exception:
                pass
            try:
                i['$BCTIThreatMask'] = lst['threat_mask']
            except Exception:
                pass
            try:
                i['$BCTIReputation']=lst['reputation']
            except Exception:
                pass
    return inward_array

def get_ip_geoinfo(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getgeoinfo?ip='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getgeoinfo'])
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
            try:
                if lst['asn']!='':
                    i['$BCTIASN']=lst['asn']
            except Exception:
                pass
            try:
                if lst['carrier']!='':
                    i['$BCTICarrier']=lst['carrier']
            except Exception:
                pass
            try:
                if lst['city']!='':
                    i['$BCTICity']=lst['city']
            except Exception:
                pass
            try:
                if lst['country']!='':
                    i['$BCTICountry']=lst['country']
            except Exception:
                pass
            try:
                if lst['latitude']!='':
                    i['$BCTILatitude']=lst['latitude']
            except Exception:
                pass
            try:
                if lst['longitude']!='':
                    i['$BCTILongitude']=lst['longitude']
            except Exception:
                pass
            try:
                if lst['organization']!='':
                    i['$BCTIOrganization']=lst['organization']
            except Exception:
                pass
            try:
                if lst['region']!='':
                    i['$BCTIRegion']=lst['region']
            except Exception:
                pass
            try:
                if lst['sld']!='':
                    i['$BCTISecondLevelDomain']=lst['sld']
            except Exception:
                pass
            try:
                if lst['state']!='':
                    i['$BCTIState']=lst['state']
            except Exception:
                pass
            try:
                if lst['tld']!='':
                    i['$BCTITopLevelDomain']=lst['tld']
            except Exception:
                pass
    return inward_array


def get_ip_threatlist(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getthreatlist'+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
    return json_response


def get_ip_threathistory2(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getthreathistory?ip='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getthreathistory'])
                #ci = datetime.datetime.utcfromtimestamp(int(dt['extended']['time'])).strftime('%Y-%m-%d %H:%M:%S')
                threat_tags=[]
                for cnt in range(0,len(lst['history'])):
                    if lst['history'][cnt]['is_threat']==1:
                        a= lst['history'][cnt]['threat_types']
                        a=''.join(a)
                        threat_tags.append(a)
                i['$BCTIThreatTypes']= list(set(threat_tags))
            except Exception:
                pass
            try:
                i['$BCTIThreatCount']=lst['threat_count']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array



def get_ip_threathistory(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getthreathistory?ip='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getthreathistory'])
                threat_tags=[]
                tmp_dict = {}
                nt_dict={}
                for cnt in range(0, len(lst['history'])):
                    if lst['history'][cnt]['is_threat'] == 1:
                        a = lst['history'][cnt]['threat_types']
                        a = ''.join(a)
                        a= str(a).title()
                        a = a.replace(' ', '')
                        threat_tags.append(a)
                        kname =a
                        ci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        tmp_dict.setdefault(kname, [])
                        tmp_dict[kname].append(ci)
                    elif lst['history'][cnt]['is_threat'] == 0:
                        kname="NotCategorized"
                        c2 = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        nt_dict.setdefault(kname, [])
                        nt_dict[kname].append(c2)
                for b in tmp_dict.keys():
                    i['$BCTIThreatType' + str(b)] = tmp_dict[b]

                for c in nt_dict.keys():
                    i['$BCTIThreatType'+ str(c)]= nt_dict[c]

                i['$BCTIThreatTypes'] = list(set(threat_tags))
            except Exception:
                pass
            try:
                i['$BCTIThreatCount']=lst['threat_count']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass

    return inward_array


def get_ip_rephistory(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ip/getrephistory?ip='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getrephistory'])
            except Exception:
                pass
            try:
                hrisk_dict = {}
                suspicious_dict ={}
                mrisk_dict={}
                lrisk_dict={}
                trusty_dict={}
                for cnt in range(0, len(lst['history'])):
                    if lst['history'][cnt]['reputation'] >= 1 and lst['history'][cnt]['reputation']<=20:
                        hkname ="HighRisk"
                        hci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        hrisk_dict.setdefault(hkname, [])
                        hrisk_dict[hkname].append(hci)
                    elif lst['history'][cnt]['reputation'] >= 21 and lst['history'][cnt]['reputation'] <= 40:
                        skname = "Suspicious"
                        sci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        suspicious_dict.setdefault(skname, [])
                        suspicious_dict[skname].append(sci)
                    elif lst['history'][cnt]['reputation'] >= 41 and lst['history'][cnt]['reputation'] <= 60:
                        mkname = "ModerateRisk"
                        mci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        mrisk_dict.setdefault(mkname, [])
                        mrisk_dict[mkname].append(mci)
                    elif lst['history'][cnt]['reputation'] >= 61 and lst['history'][cnt]['reputation'] <= 80:
                        lkname = "LowRisk"
                        lci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        lrisk_dict.setdefault(lkname, [])
                        lrisk_dict[lkname].append(lci)
                    elif lst['history'][cnt]['reputation'] >= 81 and lst['history'][cnt]['reputation'] <= 100:
                        tkname = "Trustworthy"
                        ci = datetime.datetime.utcfromtimestamp(int(lst['history'][cnt]['ts'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        trusty_dict.setdefault(tkname, [])
                        trusty_dict[tkname].append(ci)
                for h in hrisk_dict.keys():
                    i['$BCTIReputation' + str(h)] = hrisk_dict[h]

                for s in suspicious_dict.keys():
                    i['$BCTIReputation'+ str(s)]= suspicious_dict[s]

                for m in mrisk_dict.keys():
                    i['$BCTIReputation' + str(m)] = mrisk_dict[m]

                for l in lrisk_dict.keys():
                    i['$BCTIReputation' + str(l)] = lrisk_dict[l]

                for t in trusty_dict.keys():
                    i['$BCTIReputation' + str(t)] = trusty_dict[t]
            except Exception:
                pass
            try:
                i['$BCTIAverageReputation']=lst['avg_reputation']
            except Exception:
                pass
            try:
                i['$BCTIHistoryCount'] = lst['history_count']
            except Exception:
                pass
            try:
                i['$BCTIMaxReputation']=lst['max_reputation']
            except Exception:
                pass
            try:
                i['$BCTIMinReputation']=lst['min_reputation']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus']=json_response['status']
            except Exception:
                pass
    return inward_array


def get_file_info(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/file/getinfo?file='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getinfo'])
            except Exception:
                pass
            try:
                i['$BCTIDeterminationType']=lst['det']
            except Exception:
                pass
            try:
                i['$BCTIDeterminationDate']=datetime.datetime.utcfromtimestamp(int(lst['detdate'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
            except Exception:
                pass
            try:
                i['$BCTIFileSize']=lst['filesize']
            except Exception:
                pass
            try:
                i['$BCTIFirstSeen']=datetime.datetime.utcfromtimestamp(int(lst['fseen'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
            except Exception:
                pass
            try:
                i['$BCTIMalwareGroup']=lst['malwaregroup']
            except Exception:
                pass
            try:
                i['$BCTIMd5'] = lst['md5']
            except Exception:
                pass
            try:
                i['$BCTIPropagationCount'] = lst['pccount']
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
    return inward_array


def get_contextual_domainstats(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/cdb/geturlstats2?cdb='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['geturlstats2'])
            except Exception:
                pass
            try:
                if lst['common_registrant'] !=None:
                    cr_lst=lst['common_registrant']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTICommonRegistrantThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosted_apps'] !=None:
                    cr_lst=lst['hosted_apps']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostedAppsThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosted_files'] !=None:
                    cr_lst=lst['hosted_files']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostedFilesThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosting_ips'] !=None:
                    cr_lst=lst['hosting_ips']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostingIPsThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['sub_domains'] !=None:
                    cr_lst=lst['sub_domains']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTISubDomainsThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['virtuallyhosted'] !=None:
                    cr_lst=lst['virtuallyhosted']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIVirtuallyHostedThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
    return inward_array


def get_contextual_ipstats(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/cdb/getipstats2?cdb='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getipstats2'])
            except Exception:
                pass
            try:
                if lst['asn'] !=None:
                    cr_lst=lst['asn']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIASNThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosted_apps'] !=None:
                    cr_lst=lst['hosted_apps']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostedAppsThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosted_files'] !=None:
                    cr_lst=lst['hosted_files']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostedFilesThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosted_urls'] !=None:
                    cr_lst=lst['hosted_urls']
                    for cr in range(0,len(cr_lst)):
                        if cr_lst[cr]>0:
                            i['$BCTIHostedURLsThreatLevel'+str(cr)]=cr_lst[cr]
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
    return inward_array


def get_contextual_filestats(inward_array, var_array):
    for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/cdb/getfilestats2?cdb='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getfilestats2'])
            except Exception:
                pass
            try:
                if lst['hosting_ips'] != None:
                    cr_lst = lst['hosting_ips']
                    for cr in range(0, len(cr_lst)):
                        if cr_lst[cr] > 0:
                            i['$BCTIHostingIPsThreatLevel' + str(cr)] = cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['hosting_urls'] != None:
                    cr_lst = lst['hosting_urls']
                    for cr in range(0, len(cr_lst)):
                        if cr_lst[cr] > 0:
                            i['$BCTIHostingURLsThreatLevel' + str(cr)] = cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['outbound_ips'] != None:
                    cr_lst = lst['outbound_ips']
                    for cr in range(0, len(cr_lst)):
                        if cr_lst[cr] > 0:
                            i['$BCTIOutboundIPsThreatLevel' + str(cr)] = cr_lst[cr]
            except Exception:
                pass
            try:
                if lst['outbound_urls'] != None:
                    cr_lst = lst['outbound_urls']
                    for cr in range(0, len(cr_lst)):
                        if cr_lst[cr] > 0:
                            i['$BCTIOutboundURLsThreatLevel' + str(cr)] = cr_lst[cr]
            except Exception:
                pass
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
    return inward_array


def get_urlthreatinsight(inward_array, var_array):
            for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/urlthreatinsight/getmd5bysourceurl?value='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getmd5bysourceurl'])
            except Exception:
                pass
            try:
                gdhash=[]
                bdhash=[]
                ndhash=[]
             
                for dt in lst['hosted_md5s']:
                    if dt['det']=='G':
                        gdhash.append(dt['md5'])
                    elif dt['det']=='B':
                        bdhash.append(dt['md5'])
                    else:
                        ndhash.append(dt['md5'])
                if len(gdhash)>0:
                    i['$BCTIMd5HashDetTypeG']=list(set(gdhash))
                elif len(bdhash)>0:
                    i['$BCTIMd5HashDetTypeB']=list(set(bdhash))
                elif len(ndhash) > 0:
                    i['$BCTIMd5HashDetTypeNU'] = list(set(ndhash))
            except Exception:
                pass
    return inward_array



def get_urlthreatinsight_md5(inward_array, var_array):
        for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/urlthreatinsight/getsourceurlofmd5?value='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getsourceurlofmd5'])
            except Exception:
                pass
            try:
                if lst['det']!='':
                    i['$BCTIDeterminationType'] = lst['det']
            except Exception:
                pass
            try:
                if lst['detdate']!='':
                    i['$BCTIDeterminationDate'] = datetime.datetime.utcfromtimestamp(int(lst['detdate'])).strftime(
                    '%Y-%m-%d %H:%M:%S')
            except Exception:
                pass
            try:
                if lst['filesize']!='':
                    i['$BCTIFileSize'] = lst['filesize']
            except Exception:
                pass
            try:
                if lst['fseen'] != '':
                    i['$BCTIFirstSeen'] = datetime.datetime.utcfromtimestamp(int(lst['fseen'])).strftime(
                    '%Y-%m-%d %H:%M:%S')
            except Exception:
                pass
            try:
                if lst['malwaregroup'] !='':
                    i['$BCTIMalwareGroup'] = lst['malwaregroup']
            except Exception:
                pass
            try:
                fsrc_url=[]
                if lst['md5s']!=[]:
                    for dt in lst['md5s']:
                        fsrc_url.append(dt['full_source_url'])
                if fsrc_url!=[]:
                    i['$BCTIFullSourceURL']=list(set(fsrc_url))
            except Exception:
                pass
            try:
                if lst['pccount']!='':
                    i['$BCTIPropagationCount'] = lst['pccount']
            except Exception:
                pass
    return inward_array


# def get_urlthreatinsight_urlhistory(inward_array, var_array):
#     for i in inward_array:
#         if var_array[0] in i:
#             params = str(i[var_array[0]])
#             cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
#             try:
#                 response = requests.get('https://api.bcti.brightcloud.com/1.0/urlthreatinsight/geturlhistory?value='+params+cred)
#                 json_response = response.json()
#             except Exception, e:
#                 print 'Api Request Error %s' %e
#     return json_response


def get_ipthreatinsight(inward_array, var_array):
        for i in inward_array:
        if var_array[0] in i:
            params = str(i[var_array[0]])
            cred = "&oemid="+oemid+"&deviceid="+deviceid+"&uid="+uid
            try:
                response = requests.get('https://api.bcti.brightcloud.com/1.0/ipthreatinsight/getipevidence?value='+params+cred)
                json_response = response.json()
            except Exception, e:
                print 'Api Request Error %s' %e
            try:
                i['$BCTIAPIStatus'] = json_response['status']
            except Exception:
                pass
            try:
                lst = {}
                for dt in json_response['results']:
                    lst.update(dt['queries']['getipevidence'])
            except Exception:
                pass
            try:
                if lst['evidence']!=None:
                    tpe=[]
                    for thtype in lst['evidence']:
                        for dt in thtype['incidents']:
                            tpe.append(dt['threat_type'])

                    i['$BCTIThreatType']=list(set(tpe))
                else:
                    i['$BCTIIPEvidence']="none"
            except Exception:
                pass
            try:
                if lst['evidence']!=None:
                    ctime=[]
                    for con in lst['evidence']:
                        ci = datetime.datetime.utcfromtimestamp(int(con['convicted_time'])).strftime(
                            '%Y-%m-%d %H:%M:%S')
                        ctime.append(ci)

                    i['$BCTIConvictedTime']=list(set(ctime))
            except Exception:
                pass
            try:
                if lst['evidence']!=None:
                    hs_url = []
                    hs_type=[]
                    data=[]
                    for thtype in lst['evidence']:
                        for dt in thtype['incidents']:
                             data.append(dt['details'])
                    for cnt in data:
                       if 'hosted_urls' in cnt:
                            a=cnt['hosted_urls']
                            a=''.join(a)
                            hs_url.append(a)
                       if 'host_type' in cnt:
                            b=cnt['host_type']
                            b=''.join(b)
                            hs_type.append(b)
                if hs_type!=[]:
                    i['$BCTIHostType'] = list(set(hs_type))
                if hs_url !=[]:
                    i['$BCTIHostedURLs']=list(set(hs_url))
            except Exception:
                pass
            try:
                if lst['ipint']!=None and lst['ipint']!='':
                    i['$BCTIIPint']=lst['ipint']
            except Exception:
                pass
    return inward_array

