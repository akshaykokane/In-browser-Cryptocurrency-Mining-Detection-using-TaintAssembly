import os

i = 0
with open("depthallminerstart.txt") as f:
    for line in f:
        print(i)
        i = i+1
        print(line)
        line=line.rstrip("\n\t")


        os.system(
            "out/Default/chrome --no-sandbox --js-flags=\"--wasm_taint  --taint_full_log --taint_log=/home/akshay/workspace2/logs/taint.log\" "+line+" &sleep 1; kill $!")
        str2="mv /home/akshay/workspace2/logs/taint.log /home/akshay/workspace2/logs/"+str(i)+".log"
        str2.rstrip("\t\n")
        os.system(str2)
        os.system("rm /home/akshay/workspace2/logs/taint.log")



