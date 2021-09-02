import os, json

def loadParams(params_path):
    f = open(params_path,'r', encoding='UTF-8')
    params_data = json.load(f)
    return params_data

def loadReplacements(replacements_path):
    f = open(replacements_path,'r', encoding='UTF-8')
    replacements = json.load(f)
    return replacements

def loadConfig():
    workpath = os.path.abspath(os.path.join(os.getcwd(), ""))
    params = loadParams(workpath+'/config.json')
    replacements = loadReplacements(workpath+'/replacements.json')
    return params, replacements

