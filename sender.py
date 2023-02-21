import os,socket,time
from tkinter import filedialog as fd

skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
skt.bind((socket.gethostname(), 11111))
skt.listen(5)
print("Host Name : ",skt.getsockname())
client,addr = skt.accept()
print("Connection established...")
filename = fd.askopenfilename()
file_name = os.path.basename(filename)
file_size = os.path.getsize(filename)

client.send(file_name.encode())
client.send(str(file_size).encode())

with open(filename, "rb") as file:
    c=0
    start_time = time.time()
    while c<= file_size:
        data =file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c += len(data)
    end_time = time.time()

print((file_name),": file is transfered successfully...")
print("Estimated time for transfering file : ",end_time - start_time)
print("Your file is sent to respective directory...")
skt.close()


