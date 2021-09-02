from loadconfig import loadConfig
__params__, __replacements__ = loadConfig()

print(__replacements__)

keys = __replacements__.keys()
print(keys)
for i in keys:
    print(i)