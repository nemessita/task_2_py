# bir dict var
# proqram qur sorushsun Daxil edin 1 Keys 2 Values
# 1 - e basilanda dictdeki keysleri yazdirsin
# 2 - e basilanda dictdeki valueleri yazdirsin

# error mesaji bos olanda melumat daxil etmediniz

my_dict = {"london": "gb", 
           "tokyo": "jp", 
           "baku": "az",
           "moscow": "ru",
           "berlin": "ge",

           }
           

choice = input("Daxil edin 1 Keys 2 Values\n")

if choice == "1":
    print("KEY-ler:")
    for key in my_dict.keys():
        print(key)
elif choice == "2":
    print("VALUE-ler:")
    for value in my_dict.values():
        print(value)
else:
    print("Melumat daxil etmediniz")