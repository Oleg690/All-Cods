import os

for file in os.listdir("D:\\Server - Copy Minecraft\\cgi-bin"):
    if file.startswith("test"):
        exFile = os.path.join("D:\\Server - Copy Minecraft\\cgi-bin", file)
        exec(open(exFile).read())