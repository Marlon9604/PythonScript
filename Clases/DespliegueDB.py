import LecturaYaml as leer
import LecturaXml as xmlPropio
import sys
import FolderManager as fol
from termcolor import colored, cprint
import io
import colorama

class DespliegueDB:
    '''
        organizacion de scripts para despliegue
    '''
    def main(self, args):
        print('Inicio procesamiento scripts')
        # inicializacion del manejador de color
        colorama.init() 
        ## impresion con color
        ## './Clases/Configuracion.xml'
        ## "OSI.Migracion.Sophia.LB"
        ## 'C:\\Users\\javendanob\\Source\\Repos\\SostenibilidadSophia\\OSI.Migracion.Sophia.LB'
        ## "./Clases/nombre.yaml"
        ## 'd:\\Temp'

        ##"C:\\Users\\javendanob\\Source\\Repos\\TutorialPython\\Clases\\Configuracion.xml" "OSI.Migracion.Sophia.LB" "C:\\Users\\javendanob\\Source\\Repos\\SostenibilidadSophia\\OSI.Migracion.Sophia.LB" "C:\Users\javendanob\Source\Repos\TutorialPython\Clases\nombre.yaml" "d:\\Temp"
        if args != None and args != "unknowed":

            if len(args) < 5:
                cprint("Se deben especificar los siguientes parametros:", "red")
                cprint("Ruta del XMl de configuracion. $(Build.SourcesDirectory)\\Deploy\\ObtenerDB\\Configuracion.xml", "red")
                cprint("Seccion de ruta del TFS a cambiar. $/Sostenibilidad/Dev", "red")
                cprint("Seccion de ruta del directorio local. $(Build.SourcesDirectory)", "red")
                cprint("Ruta del yaml con el listado de componentes.", "red")
                cprint("Ruta Files destino", "red")
            else:
                try:
                    print("Lectura Yaml")
                    ## leer yaml
                    dic = leer.LeerYaml(args[3])
                    ## cambiar path de los archivos
                    pathSource = args[1]
                    pathTarget = args[2]
                    
                    for x in dic:
                        dic[x] = str(dic.get(x)).replace(pathSource, pathTarget).replace("/", "\\")
                    
                    print('Creacion carpetas')
                    ## obtener estructura xml
                    estructuraXml = xmlPropio.LeerXml(args[0])  
                    mFolder = fol.FolderManager(args[4])
                    ## crear carpetas
                    root = estructuraXml.get('nombreDb')
                    mFolder.MakeFolder(root)
                    mFolder.ActualizarPath(root)
                    carpetas = estructuraXml.get('carpetas')                    
                    foldersMake = []
                    for item in carpetas:
                        foldersMake.append(item.get('nombre')) 

                    mFolder.ProccesingFolders(foldersMake)
                    print("Archivo procesados")
                    ## identificar el tipo
                    for y in dic:
                        #print(y) ## numeracion de archivo
                        nombre = mFolder.RemoveSuf(estructuraXml.get('caracteres'), dic.get(y))
                        #print(nombre)
                        rta = mFolder.ValidateTarget(nombre, carpetas)
                        #print(rta) ## nombre de carpeta
                        nombreCarperaDestino = args[4] + "\\" + root + "\\"  + rta
                        nombreArchivoDestino = mFolder.GetNameFile(dic.get(y))
                        nombreDestino = nombreCarperaDestino + "\\" + str(y) + "." + nombreArchivoDestino
                        
                        ## copiar archivos a carpetas
                        mFolder.CopyFiles(dic.get(y),nombreDestino)
                        cprint(nombreDestino, "green")

                except Exception as err:
                    cprint(err, "red")
                    cprint('Proceso Fallido', 'red')
                    #raise ValueError('Proceso Fallido')
                finally:
                    pass

if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv[1:]))
    DespliegueDB().main(sys.argv[1:])
