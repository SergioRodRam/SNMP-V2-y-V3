# snmp-set-v2.py
# Modifica el valor de un objeto utilizando SNMP versión 2
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

#valor = OctetString("Router1")
if OID == '1.3.6.1.2.1.2.2.1.7' or OID == '1.3.6.1.2.1.2.2.1.7.1' or OID == '1.3.6.1.2.1.2.2.1.7.2' or OID == '1.3.6.1.2.1.2.2.1.7.3' or OID == '1.3.6.1.2.1.2.2.1.7.4':
   valor = Integer(argv[3])
else:
   valor = OctetString(argv[3])

iterador = setCmd(
    SnmpEngine(),
    CommunityData(cadena_comunidad, mpModel=1),
    UdpTransportTarget((ip,puerto)),
    ContextData(),
    ObjectType(ObjectIdentity(OID),valor))
despliega(iterador)
