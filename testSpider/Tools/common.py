import  hashlib

def get_MD5(url):
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_MD5("http://jobbole.com".encode('utf-8')))

# 会报错的,Unicode-objects must be encoded before hashing
# 因为python3会自动转换编码为unicode

