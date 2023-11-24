# snmp-get-v2.py
# Obtiene un objeto utilizando SNMP versión 2
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
cadena_comunidad = 'prueba'
ip = argv[1] #'4.28.200.10'
puerto = 161
OID =argv[2] #'1.3.6.1.2.1.1.5.0' # nombre del host
iterador = getCmd(
    SnmpEngine(),
    CommunityData(cadena_comunidad, mpModel=1),
    UdpTransportTarget((ip,puerto)),
    ContextData(),
    ObjectType(ObjectIdentity(OID)))
despliega(iterador)
