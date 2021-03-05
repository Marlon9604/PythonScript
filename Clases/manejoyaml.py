## librerias
import sys
from ruamel.yaml import YAML

inp = """\
# example
name:
  # details
  family: Smith   # very common
  given: Alice    # one of the siblings
  os:
    - Windows 7
    - linux Ubuntu
    - macOs X
"""
def LeerArchivo():

    with open("./texto.yaml", "r+") as file_object:
        yaml = YAML()
        code = yaml.load(file_object)
        code['name']['given'] = 'Bob'

        ##ontener informacion del  yaml cargado
        print (code['name']['family'])
        print (code['name']['os'])

        ## os
        for item in code['name']['os']:
            print (f"presentando {item} os") ## formateo de texto con interpolacion

        ## modifica el texto leido -- genera nuevo yaml
        yaml.dump(code, sys.stdout)

        ## cierre ed archivo
        ##file_object.close()

    print("fin")

if __name__ == '__main__':
    print("inicio de")
    LeerArchivo();