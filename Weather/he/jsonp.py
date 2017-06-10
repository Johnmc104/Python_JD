#coding: utf- 8

import time
import hashlib
import hmac
import base64
from urllib import parse
from utils.const_value import UID, KEY, API
from utils.helper import getLocation


def getJsonpUrl(location):
    ts = int(time.time())  # 当前时间戳
    params = "ts={ts}&uid={uid}".format(ts=ts, uid=UID)  # 构造验证参数字符串

    key = bytes(KEY, 'UTF-8')
    raw = bytes(params, 'UTF-8')

    # 使用 HMAC-SHA1 方式，以 API 密钥（key）对上一步生成的参数字符串（raw）进行加密
    digester = hmac.new(key, raw, hashlib.sha1).digest()

    # 将上一步生成的加密结果用 base64 编码，并做一个 urlencode，得到签名sig
    signature = base64.encodestring(digester).rstrip()
    sig = parse.quote(signature.decode('utf8'))

    # 构造最终请求的 url
    url = API + "?location={}&".format(location) + \
        params + '&sig=' + sig + "&callback=?"
    return url

if __name__ == '__main__':
    location = getLocation()
    url = getJsonpUrl(location)
    print(url)
