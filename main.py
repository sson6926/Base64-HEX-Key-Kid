import sys
import base64
import json

input = """fabfa7c70d3c6788b79288383e035ca4:5f7d4e70d0e1091c42f1d9b20f290cf2
4203a7c70d3c6788b79288383e035ca4:8551a53ece07341f7a77f9e90f9cbec7
4f07ebf80d3c6788b79288383e035ca4:212dc04765312850fa6668cdb67bb819
3b14eb105c3c6788b79288383e035ca4:84b897852cc90c220226d67c7c2c859a"""

# input = input("Nhap PSSH vua get duoc: ")
keys = []
for input1 in input.split("\n"):
  hex_keyid = input1.split(":")[0]
  hex_key = input1.split(":")[1]
  bin_keyid = bytes.fromhex(hex_keyid)
  bin_key = bytes.fromhex(hex_key)
  keyid_b64 = base64.b64encode(bin_keyid).decode().replace('=', '')
  key_b64 = base64.b64encode(bin_key).decode().replace('=', '')
  if not keyid_b64 or not key_b64:
      error_json = {"msg":"Invalid KidKey"}
      print(json.dumps(error_json))
      sys.exit(1)
  
  
  new_key  = {"kty": "oct", "k": key_b64, "kid": keyid_b64}
  keys.append(new_key)
license_json = {"keys": keys, "type": "temporary"}

print(json.dumps(license_json))
