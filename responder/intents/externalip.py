
# Marcel Timm, RhinoDevel, 2022jul17

import urllib.request

def exec(params):
    # TODO: Add a time out (and a time out response text)!
    #
    external_ip = urllib.request.urlopen('https://ident.me').read().decode(
        'utf8')
    
    return 'Die externe Eipi Adresse ist %s' % external_ip.replace(
        '.', ' Punkt ')
