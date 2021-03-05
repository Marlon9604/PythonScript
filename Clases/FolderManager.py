import os
import shutil

class FolderManager():
    ''' Manejo de archivos y carpetas, creacion, validacion.'''
    _path = ""
    def __init__(self, path):
        '''Inicializa clase con la ruta base para la creacion de los objetos.'''
        self._path = path
    

    def ActualizarPath(self, cadena):
        '''Actualizacion ruta original con la carpeta de la DB correspondiente.'''
        self._path = self._path + '\\' + cadena

    def MakeFolder(self, folder):
        '''Creacion de carpetas.
            folder: carpeta a crear.
        '''
        if self.ValidateFolderExist(self._path, folder) == 0:
            os.mkdir(self._path + '\\' +  folder)

    def ProccesingFolders(self, folders):
        '''Creacion de carpetas con base a lista pasada por parametro.'''
        for folder in folders:
            self.MakeFolder(folder)

    def ValidateFolderExist(self, path, folder):
        '''Validacion existencia carpeta. 1 carpeta encontrada - 0 no.'''
        carpetas = os.listdir(path)
        existe = 0
        for item in carpetas:
            if item == folder:
                existe = 1

        return existe
        
    ## validar coincidencia de prefijos para ubicar un archivo
    def ValidateTarget(self, archivo, carpetas):
        '''Validar script para obtener folder destino
            archivo: ruta completa del archivo.
            carpetas: estructura de carpetas para la operacion.
        '''
        nombre = os.path.basename(archivo)
        for carpeta in carpetas:
            for prefijo in carpeta.get('prefijos'):
                if nombre.upper().startswith(prefijo.upper()):
                    return carpeta.get('nombre')
            
    def GetNameFile(self, archivo):
        '''Obtener nombre de archivo a partir de ruta completa.'''
        return os.path.basename(archivo)

    def CopyFiles(self, origen: str, destino: str):
        '''Copia de archivo: 
            origen: ruta origen.
            Destino: ruta destino
        '''
        shutil.copy(origen,destino)
    
    def RemoveSuf(self, sufijos, archivo: str):
        '''Quitar del nombre de archivo palabras clave.
            sufijos: coleccion de palabras clave.
            archivo: nombre del archivo.
        '''
        nombre = archivo
        for suf in sufijos:
            nombre = nombre.replace(suf, "")
        return nombre
