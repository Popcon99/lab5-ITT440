import socket

s=socket.socket()
print("Berjaya buat soket")

port= 8888

s.bind(('',port))
print("Yeayyy berjaya bind soket di port: " + str(port))
s.listen(5)
print("soket tengah tunggu client ni!")

while True:
	c,addr =s.accept()
	print("Dapat capaian dari: "+ str(addr))

	c.send(b'Terima kasih!')
	buffer = c.recv(1024)
	print(buffer)
c.close()


