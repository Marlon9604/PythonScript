## muchos agumentos

def ManejoVar(nombre: str, *args):
    print(nombre)
    if args != None and args != "unknowed":
        if len(args) > 0:
            print(args[0])
        else:
            print("sin argumentos")

def ManejoVarParametros(nombre: str, **argumentos):
    print(nombre)
    print(argumentos["p1"])


ManejoVar("jason", "argumento1", 2, None)
ManejoVar("nombre1")
ManejoVarParametros(nombre="jason", p1="argumento1", p2=2, p3=None)