#coding=utf-8

import objectbox.customlib.matlab
import objectbox.base

strPrxMap = { }

def fromOBElementPrxToSubClassPrx(elementPrx):
    _type = elementPrx.getType()
    prxUnCheckedCast = strPrxMap[_type]
    return prxUnCheckedCast(elementPrx)

def fromOBElementPrxToSubClassPrxByType(elementPrx,type_):
    prxUnCheckedCast = strPrxMap[type_]
    return prxUnCheckedCast(elementPrx)

def updatePrxFactory(name, factoryMethord):
    strPrxMap[name] = factoryMethord