#creando mi propia excepcion personalizada
class MiExepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
        #Lanzando mi propia excepcion
        #raise MiExepcion("Jajaja, persona poco culta")
        
        #manejandola
        try:
            raise MiExepcion("Jajajaja, persona poco culta")
        except:
            print("como vas a cometer ese error?")