Str = "this is string example....wow!!!"
Str = Str.encode("utf-8",'replace')

print("Encoded String: " , Str)
print("Decoded String: " + Str.decode('utf-8','replace'))
