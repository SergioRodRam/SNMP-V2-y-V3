# snmp-bulk-v3.py
# Obtiene un sub-árbol de objetos utilizando SNMP versión 3
# Carlos Pineda Guerrero. 2022
from pysnmp.hlapi import *
from sys import argv

def despliega(iterador):
    while True:
        try:
            errorIndication, errorStatus, errorIndex, varBinds = next(iterador)
            if not errorIndication and not errorStatus:
                for varBind in varBinds:
                    print(varBind)
            else:
                print("Error:",errorStatus)
        except StopIteration:
            return
ip = argv[1] #'4.28.200.10'
puerto = 161
OID =argv[2] #'1.3.6.1.2.1.2.2.1.2' # interfaces
iterador = bulkCmd(
    SnmpEngine(),
    UsmUserData('usuario',authKey='password123',authProtocol=usmHMACSHAAuthProtocol,privKey='password123',privProtocol=usmAesCfb128Protocol),
    UdpTransportTarget((ip,puerto)),
    ContextData(),
    0, #// nonRepeaters
    25, #// maxRepetitions
    ObjectType(ObjectIdentity(OID)),
    lexicographicMode=False)
despliega(iterador)
