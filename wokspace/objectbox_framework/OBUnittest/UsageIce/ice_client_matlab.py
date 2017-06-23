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
            #print self.appName()+":invalid proxy"
            return 1

        matlabPrx = obCenter.getOBElementByName('Matlab')
        matlabPrx = IceOBUtil.proxyUtil.fromOBElementPrxToSubClassPrx(matlabPrx)

        import time
        matlabPrx.open()
        time.sleep(5)
        matlabPrx.executeCommand("cd 'D:\\'")
        time.sleep(5)
        matlabPrx.executeCommand("cd 'd:\\MATLAB\\R2011b'")
        time.sleep(5)
        matlabPrx.close()

        return 0

app = Client()
sys.exit(app.main(sys.argv, r"config.client"))





