from const import link


def isList(var):
    return isinstance(var, list)


def arrToParam(arr):
    str = ''
    for e in arr:
        e = e.replace(' ', '%20')
        str = f"{str}{e}+"
    
    # remove last +, and return
    return str[:-1]


def getUrl(params):
    url = f'{link}?'
    
    for key in params:
        # get value
        val = params[key]
        
        # if multiple args the param
        if isList(val):
            val = arrToParam(val)

        # set param
        param = f'{key}={val}&'
            
        # append to url
        url = f'{url}{param}'
    
    # remove last &, and return
    return url[:-1]