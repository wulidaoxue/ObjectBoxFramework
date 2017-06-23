import objectbox.base as base
import Ice
import uuid
import weakref
import OBBase.server_state as gbss
import IceOBUtil.proxyUtil as prxutil
import IceOBUtil.servantUtil as svtutil



class OBElementDefaultServantLocator(Ice.ServantLocator):
    def locate(self, c, cookie=None):
        uuid_ = c.id.name
        obElementI = gbss.OBCenter.iGetOBElement(uuid_)
        return obElementI

    def finished(self, c, servant, cookie):
        pass

    def deactivate(self, category):
        pass



class OBElementI(base.OBElement):
    def __init__(self):
        self._category = 'OBElement'
        self._type = 'OBElement'
        self._name = ""
        self._desc = "empty desc"
        self._parent = None
        self._uuid = str(uuid.uuid1())
        self._listeners = []
        if gbss.OBCenter!=None:
            self._listeners.append(gbss.OBCenter)
            gbss.OBCenter.iAddOBElement(self)

    def __str__(self):
        resultStr = self._type+':'+self._name+' ('+self._desc+')'
        return resultStr

    #not ice interface
    def iGetIdentity(self):
        _id = Ice.Identity()
        _id.name = self._uuid
        _id.category = self._category
        return _id

    #not ice interface
    def iGetPrx(self):
        _id = self.iGetIdentity()
        _prx = gbss.FrameWorkAdapter.createProxy(_id)
        _prx = prxutil.fromOBElementPrxToSubClassPrxByType(_prx, self._type)
        return _prx

    def getName(self, current=None):
        return self._name

    def setName(self, newName, current=None):
        self._name = newName

    def getDescription(self, newDesc, current=None):
        return self._desc

    def setDescription(self, newDesc, current=None):
        self._desc = newDesc

    def getUuid(self, current=None):
        return self._uuid

    def getType(self, current=None):
        return self._type

    def getParent(self, current=None):
        if self._parent != None:
            self._parent.iGetPrx()
        else:
            return None

    def setParent(self, parentPrx, current=None):
        if parentPrx!=None:
            uuid_ = parentPrx.ice_getIdentity().name
            obElementI = gbss.OBCenter.iGetOBElement(uuid_)
            if self._parent!=None:
                self._parent.removeChild(self)
            self._parent = obElementI
        else:
            self._parent = None

    def registerObserver(self, newObserver, current=None):
        self._listeners.append(newObserver)

    def removeObserver(self, oldObserver, current=None):
        self._listeners.remove(oldObserver)

    def notifyObservers(self, diffInfo, current=None):
        for listener in self._listeners:
            listener.updateBySubject(self,diffInfo)

    def updateBySubject(self, subject, diffInfo, current=None):
        pass



class OBContainerI(base.OBContainer, OBElementI):
    def __init__(self, name=''):
        OBElementI.__init__(self)
        self._name = name
        self._children = []
        self._type = 'OBContainer'
        self._objectFullNamedReferences = weakref.WeakValueDictionary()

    def __str__(self):
        resultStr = self._type+':'+self._name+' ('+self._desc+')'+'\n'
        for child in self._children:
            for line in str(child).splitlines():
                resultStr += '\t'+line+'\n'
        return resultStr

    def getChildren(self, current=None):
        result = []
        for child in self._children:
            result.append(child.iGetPrx())
        return result

    #path example: container1.container2.obelement1
    def getOBElementByName(self, name, current=None):
        pathList = name.split('.')
        tempi = self
        for nametemp in pathList:
            tempi = tempi._objectFullNamedReferences[nametemp]
        elePrx = tempi.iGetPrx()
        return elePrx

    def createOBElement(self, name, type, current=None):
        servantI = svtutil.createServant(name, type)
        servantI._parent = self
        self._children.append(servantI)
        self._objectFullNamedReferences[name] = servantI
        return servantI.iGetPrx()

    #need think more
    def removeChild(self, childPrx, current=None):
        uuid_ = childPrx.ice_getIdentity().name
        childObElementI = gbss.OBCenter.iGetOBElement(uuid_)
        #childObElementI.setParent(None)
        self._children.remove(childObElementI)
        #todo remove
        self._objectFullNamedReferences

    def getOBContainerInfo(self, current=None):
        # resultStr = ''
        # for key in self._objectFullNamedReferences.keys():
        #     resultStr += str(self._objectFullNamedReferences[key]) + '\n'
        resultStr = OBContainerI.__str__(self)
        return resultStr



class OBCenterI(base.OBCenter, OBContainerI):
    def __init__(self):
        OBContainerI.__init__(self,{})
        self._objectUuidReferences = weakref.WeakValueDictionary()
        self._root = None
        self._name = 'OBCenter'
        self._type = 'OBCenter'

    #not ice interface
    #only OBCenter override the methrod, because it's special
    def iGetIdentity(self):
        _id = Ice.Identity()
        _id.name = self._name
        _id.category = self._category
        return _id

    #not ice interface
    def iAddOBElement(self, elementi):
        _uuid = elementi.getUuid()
        self._objectUuidReferences[_uuid] = elementi

    #not ice interface
    def iGetOBElement(self, uuid_):
        return self._objectUuidReferences[uuid_]


class OBPythonRunnerI(base.OBPythonRunner, OBElementI):
    def __init__(self,name=''):
        OBElementI.__init__(self)
        self._name = name
        self._type = 'OBPythonRunner'

    def __str__(self):
        return OBElementI.__str__(self)

    def runPyFile(self, pyFilePath, current=None):
        exec(open(pyFilePath).read())
        #exec(open("./filename").read())
        #execfile(pyFilePath)

    def getCwd(self, current=None):
        import os
        return os.getcwd()

svtutil.updateServantFactory('OBElement',OBElementI)
svtutil.updateServantFactory('OBCenter',OBCenterI)
svtutil.updateServantFactory('OBPythonRunner',OBPythonRunnerI)
svtutil.updateServantFactory('OBContainer',OBContainerI)

prxutil.updatePrxFactory('OBElement', base.OBElementPrx.uncheckedCast)
prxutil.updatePrxFactory('OBCenter', base.OBCenterPrx.uncheckedCast)
prxutil.updatePrxFactory('OBPythonRunner', base.OBPythonRunnerPrx.uncheckedCast)
prxutil.updatePrxFactory('OBContainer', base.OBContainerPrx.uncheckedCast)


