import hashlib
count=0
count2=0
combos=input("\nEnter the combos file name where the passwords are md5 encrypted : ")
file1=input("\nEnter the wordlist : ")
decrypted=open("decrypted.txt", "a+") 
print("\n")
with open(combos) as data:
    for encline in data:
        for ch in encline:
            if(ch==":"):
                str1= encline[encline.index(ch)+1:-1]
                with open(file1) as data:
                    for line in data:
                        line=line[:-1]
                        str2 = hashlib.md5(line.encode())
                        str2 = str2.hexdigest()
                        if(str1==str2):
                             decrypted.write(encline[0:encline.index(ch)]+":"+line+"\n")# Decrypted ones can be saved in decrypted.txt file
                             count=count+1
                             print(count,"found")
                             break
        count2=count2+1
        if(count2%50==0):
            print("\n------------------------",count2,"hashes checked till you------------------------\n")
data.close()
combos.close()
file1.close()
decrypted.close()
#With lot of love @luk0y
