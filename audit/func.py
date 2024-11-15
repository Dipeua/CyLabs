import requests
import socket
import whois
import dns.resolver
import datetime
import tldextract

def checkIfDomainIsValid(domain):
    ext = tldextract.extract(domain)
    if ext.domain and ext.suffix:
        try:
            socket.gethostbyname(domain)
            return True
        except socket.error:
            return False
    else:
        return False
    
def getIpv4Address(domain):
    try:
        ip_addresses = socket.getaddrinfo(domain, None, socket.AF_INET)
        ipv4_address = ip_addresses[0][4][0]
        return ipv4_address
    except socket.gaierror as e:
        print(f"Error: {e}")
        return None

def getDomainInfos(domain):
    try:
        dns_servers = dns.resolver.resolve(domain, 'NS')
        dns_servers = [str(server) for server in dns_servers]
    except dns.resolver.NoAnswer:
        dns_servers = None

    try:
        domain_info = whois.whois(domain)
        status = domain_info.status
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date
    except whois.parser.PywhoisError:
        status = None
        creation_date = None
        expiration_date = None

    if isinstance(creation_date, list):
        creation_date = creation_date[0]
    if isinstance(expiration_date, list):
        expiration_date = expiration_date[0]

    if isinstance(creation_date, datetime.datetime):
        creation_date = creation_date.strftime('%Y-%m-%d')
    if isinstance(expiration_date, datetime.datetime):
        expiration_date = expiration_date.strftime('%Y-%m-%d')

    return {
        'domain': domain,
        'ip': getIpv4Address(domain),
        'status': status,
        'creation_date': creation_date,
        'expiration_date': expiration_date,
        'dns_servers': dns_servers,        
    }

uris_found = []
wordlists = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt'
def foundURIs(domain, wordlist):
    responseWordlist = requests.get(wordlist)
    if responseWordlist.status_code == 200:
        words_list = responseWordlist.text.splitlines()
        for word in words_list:
            responseTarget = requests.get(domain + word)
            if responseTarget.status_code == 200:
                uris_found.append(responseTarget.domain)


class Vulnerability():
    def __init__(self, service, version):
        self.exploitdb_api = ""

    def getVersion(self):
        pass

