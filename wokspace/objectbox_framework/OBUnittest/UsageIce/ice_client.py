import os, sys, time, traceback, threading, Ice
import objectbox.base
import objectbox.customlib.matlab
import OBBase.server_state
import IceOBUtil.proxyUtil
import logging
obLogger = logging.getLogger('ObjectBox.Client')

class Client(Ice.Application):

    def run(self, args):
        obCenter = objectbox.base.OBCenterPrx.checkedCast(self.communicator().propertyToProxy("RootElement.Proxy"))
        if not obCenter:
            print self.appName()+":invalid proxy"
            return 1
        name = obCenter.getName()
        names = obCenter.getAllNames()
        obLogger.info(">>>>"+name)
        obLogger.info(">>>>"+str(names))
        matlabPrx = obCenter.getOBElementByName('Matlab')
        pythonPrx = obCenter.getOBElementByName('PythonRunner')
        obLogger.info(matlabPrx)
        obLogger.info(pythonPrx)
        obLogger.info(matlabPrx.getType())
        obLogger.info(pythonPrx.getType())
        matlabPrx = IceOBUtil.proxyUtil.fromOBElementPrxToSubClassPrx(matlabPrx)
        pythonPrx = IceOBUtil.proxyUtil.fromOBElementPrxToSubClassPrx(pythonPrx)
        cwd = pythonPrx.getCwd()
        obLogger.info(cwd)
        return 0

app = Client()
sys.exit(app.main(sys.argv, r"config.client"))
