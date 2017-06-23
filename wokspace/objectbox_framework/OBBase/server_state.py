import logging
import sys

obLogger = logging.getLogger('ObjectBox')
obLogger.setLevel(logging.DEBUG)
_consoleHandler = logging.StreamHandler(sys.stdout)
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_consoleHandler.setFormatter(_formatter)
obLogger.addHandler(_consoleHandler)

FrameWorkAdapter = None
OBCenter = None

def AddOBElementToFrameWorkAdapter(obElement):
    _prx = FrameWorkAdapter.add(obElement, obElement.iGetIdentity())
    return _prx


