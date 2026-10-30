import struct
a=float(input())
a=struct.unpack("f",struct.pack('f',a))[0]
print("%.5f" % a)
print("%.4f" % a)
print("%.3f" % a)
print("%.2f" % a)
print("%.1f" % a)
print("%.0f" % a)
