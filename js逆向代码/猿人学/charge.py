import json
def str_to_dict(s):
    dicts = "{\n"
    lists = s.split('\n')
    listss = ['\"'+list.strip().replace(':','\":\"',1).replace(' ','')+'\"' for list in lists ]
    for listi in listss:
        dicts+='\t\t'+listi+','+'\n'
        # print(listi+'\n')
    dicts+='}'
    # print(dict(dicts))
    return dicts
if __name__ == '__main__':
    strs = '''isflag: true
selectedProjectIndex: 1'''
    print(str_to_dict(strs))