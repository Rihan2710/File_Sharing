import os,socket,time

host = input("Enter Host Name: ")
skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    skt.connect((host,11111))
    print("Connected Successfully...")
except:
    print("Unable to connect")
    exit(0)
file_name=skt.recv(100).decode()
file_size=skt.recv(100).decode()

with open("./Receiver/" + file_name,"wb") as file:
    c = 0
    start_time = time.time()
    while c <= int(file_size):
        data = skt.recv(1024)
        if not (data):
            break
        file.write(data)
        c+=len(data)
    end_time = time.time()
print((file_name),": file received successfully...")
print("Estimated time for receiving file : ",end_time - start_time)
print("Your file is received in (rec) folder...")
skt.close()
        
