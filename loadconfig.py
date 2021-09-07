import os, json

def loadParams(params_path=None):
    if not params_path:
        params_path = os.path.abspath(os.path.join(os.getcwd(), ""))+'/config.json'
    f = open(params_path,'r', encoding='UTF-8')
    params_data = json.load(f)
    return params_data

def loadReplacements(replacements_path=None):
    if not replacements_path:
        replacements_path = os.path.abspath(os.path.join(os.getcwd(), ""))+'/replacements.json'
    f = open(replacements_path,'r', encoding='UTF-8')
    replacements = json.load(f)
    return replacements

def loadBullshits(bullshits_path=None):
    if not bullshits_path:
        bullshits_path = os.path.abspath(os.path.join(os.getcwd(), ""))+'/bullshits.json'
    f = open(bullshits_path,'r', encoding='UTF-8')
    bullshits = json.load(f)
    return bullshits

def loadConfig():
    workpath = os.path.abspath(os.path.join(os.getcwd(), ""))
    params = loadParams(workpath+'/config.json')
    replacements = loadReplacements(workpath+'/replacements.json')
    bullshits = loadReplacements(workpath+'/bullshits.json')
    return params, replacements, bullshits

