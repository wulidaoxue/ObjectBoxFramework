import logging
obLogger = logging.getLogger('ObjectBox.Client')
def fun1():
    global obLogger
    obLogger.info("hello")

def fun2():
    global obLogger
    obLogger.info("hello")

fun1()
fun2()