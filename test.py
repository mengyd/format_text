from loadconfig import loadConfig
__params__, __replacements__ = loadConfig()

print(__replacements__)

keys = __replacements__.keys()
print(keys)
for i in keys:
    print(i)

p = "dsqdsq dsqd dzqds dsq ."

if p[-2] == ' ' and not p[-1].isalnum():
    p = p.rstrip(p[-2]+p[-1]) + p[-1]

print(p)