from akamai.edgeauth import EdgeAuth, EdgeAuthError
import requests # just for this example

ET_HOSTNAME = 'jdslivestream.akamaized-staging.net'
ET_ENCRYPTION_KEY = '08674676e4bc11e6ba7b240ba4a8e118'
DEFAULT_WINDOW_SECONDS = 500 # seconds


et = EdgeAuth(**{'key': ET_ENCRYPTION_KEY,
                  'window_seconds': DEFAULT_WINDOW_SECONDS, 'token_name':'hdnts'})

print("chk pt. a1")


#token = et.generate_url_token("/akamai/edgeauth")
token = et.generate_url_token("/*")
print("chk pt. a2")


#url = "http://{0}{1}".format(ET_HOSTNAME, "/akamai/edgeauth")
url = "http://{0}{1}".format(ET_HOSTNAME, "/hls/stream.m3u8")
print("url = {}".format(url))

print("et = {}".format(et))
print("chk pt. a3")


response = requests.get(url, cookies={et.token_name: token})
print("chk pt. a4")

print(response) # Maybe not 403

