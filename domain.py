from urllib.parse import urlparse


#get domain name
def get_domain_name(url):
    try :
        result = get_sub_domain_name(url).split('.')
#        print(result)
        return result[-2] + '.' + result[-1]
    except:
        return ''

#Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


#print (get_domain_name(input(str())))