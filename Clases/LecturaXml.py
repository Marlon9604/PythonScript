import xml.etree.ElementTree as ET



def LeerXml(nombre: str):
    tree = ET.parse(nombre)
    root = tree.getroot()
    InformacionConfig = {}
    for child in root.iter('db'):
        name = child.get('name')
        filtro = child.get('filtro')
        InformacionConfig['nombreDb'] = name
        InformacionConfig['proyectoDb'] = filtro
        caracterColeccion = []
        InformacionCC = []
        caract = child.find('caracteres')
        carpetas = child.find('carpetas')
        for carac in caract.iter('caracter'):
            caracterColeccion.append(carac.text)

        InformacionConfig['caracteres'] = caracterColeccion
        for carp in carpetas.iter('carpeta'):
            informacionCarpeta = {}
            prefijoColeccion = []
            idCarpeta = carp.get('id')
            nombreCarpeta = carp.get('name')
            ordenCarpeta = carp.get('order')
            informacionCarpeta['id'] = idCarpeta
            informacionCarpeta['nombre'] = nombreCarpeta
            informacionCarpeta['orden'] = ordenCarpeta

            for car in carp.iter('prefijo'):
                prefijoColeccion.append(car.text)
            
            for car in carp.iter('sufijo'):
                prefijoColeccion.append(car.text)

            informacionCarpeta['prefijos'] = prefijoColeccion
            InformacionCC.append(informacionCarpeta)
            
        InformacionConfig['carpetas'] = InformacionCC
        
    return InformacionConfig