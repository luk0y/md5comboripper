import hashlib


found_hash=0
hash_count=0
combos=input("\nEnter the combos file name where the passwords are md5 encrypted : ")
file1=input("\nEnter the wordlist : ")
decrypted=open("decrypted.txt", "a+") 
print("\n")
with open(combos) as data:
    for encline in data:
        for character in encline:
            if(character==":"):
                str1= encline[encline.index(character)+1:-1]
                with open(file1) as data:
                    for line in data:
                        line=line[:-1]
                        str2 = hashlib.md5(line.encode())
                        str2 = str2.hexdigest()
                        if(str1==str2):
                             decrypted.write(encline[0:encline.index(character)]+":"+line+"\n")# Decrypted ones can be saved in decrypted.txt file
                             found_hash=found_hash+1
                             print(found_hash,"found")
                             break
        hash_count=hash_count+1
        if(hash_count%50==0):
            print("\n------------------------",hash_count,"hashes checked till you------------------------\n")
data.close()
combos.close()
file1.close()
decrypted.close()
#With lot of love @luk0y
