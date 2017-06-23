import os, sys, time, traceback, threading, Ice
import objectbox.base as base
import objectbox.customlib.matlab as matlab
import OBBase.server_state

import IceOBUtil.proxyUtil as prxutil

import logging
obLogger = logging.getLogger('ObjectBox.Client')


class Client(Ice.Application):

    def run(self, args):
        obCenter = base.OBCenterPrx.checkedCast(self.communicator().propertyToProxy("RootElement.Proxy"))
        if not obCenter:
            obLogger.info(self.appName()+":invalid proxy")
            return 1

        obLogger.info(prxutil.strPrxMap)

        pythonPrx = obCenter.getOBElementByName('PythonRunner')
        pythonPrx = base.OBPythonRunnerPrx.uncheckedCast(pythonPrx)

        #pythonPrx.runPyFile('Scripts\\openMatlab.py')
        pythonPrx.runPyFile('Scripts\\helloWorld.py')
        info = obCenter.getOBContainerInfo()
        obLogger.info('\n'+info)

        gbVarBoxPrx = obCenter.getOBElementByName('GlobalVariableBox')
        gbVarBoxPrx = base.OBContainerPrx.uncheckedCast(gbVarBoxPrx)

        childGbvBoxPrx = gbVarBoxPrx.createOBElement('childVarBox','OBContainer')
        childGbvBoxPrx = base.OBContainerPrx.uncheckedCast(childGbvBoxPrx)

        childMatlab = gbVarBoxPrx.createOBElement('childMatlab','OBMatlab')
        childChildMatlab = childGbvBoxPrx.createOBElement('childMatlab','OBMatlab')

        info = obCenter.getOBContainerInfo()
        obLogger.info('\n'+info)

        return 0

app = Client()
sys.exit(app.main(sys.argv, r"config.client"))
