import codecs

passwords_file = open("passwords.txt")
usernames_file = open("usernames.txt")

for username, password in zip(
    usernames_file.read().splitlines(),
    passwords_file.read().splitlines()
):
    if username == "cultiris":
        print(codecs.encode(password, "rot_13"))

passwords_file.close()
usernames_file.close()
