
_strServantConstructorMap = {}

def createServant(name, type):
    contructor = _strServantConstructorMap[type]
    return contructor(name)

def updateServantFactory(name, constructor):
    _strServantConstructorMap[name] = constructor

