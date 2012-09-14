class Singleton:
    __single = None
    def __init__( self ):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self  

def getIstance( x = Singleton ):
    try:
        single = x()
    except Singleton, s:
        single = s
    return single 
