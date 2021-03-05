## librerias
import sys
from ruamel.yaml import YAML


def LeerYaml(nombre: str):
    ''' Lectura de archivo yaml basado en las siguientes estructuras
        script
            - file: 
                id: 302, 
                name: ******.sql

        o

        scripts:
        - file: {id: 302, name: ****.sql}

        nombre: ruta del archivo yaml a consultar.
    '''

    try:
        file_object  = open(nombre, "r")
        yaml = YAML()
        code = yaml.load(file_object)
        filesToProcess = {}

        
        for item in code['scripts']:
            idd = item.mlget('file').mlget('id')
            name = item.mlget('file').mlget('name')
            filesToProcess[idd] = name

        #ordenamiento del diccionario
        clon = {}
        for x in sorted(filesToProcess):
            clon[x] = filesToProcess.get(x)
                
        return clon

    except Exception:
        print(sys.exc_info())
        raise ValueError('Error procesando Yaml')
    finally:
        ## cierre ed archivo
        file_object.close() 