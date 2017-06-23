import OBBase.server_state
import IceOBUtil.proxyUtil

obCenter = OBBase.server_state.OBCenter

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
