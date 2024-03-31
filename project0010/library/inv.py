import configparser
import sys
 

def read_inventory(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    inventory = {}

    for section in config.sections():
        inventory[section] = {}
        for key, value in config.items(section):
            inventory[section][key] = value

    return inventory

if __name__ == "__main__":
    filename = 'inventory.ini'
    inventory = read_inventory(filename)
    n = len(sys.argv)
    print("Total arguments passed:", n)

    servertype = "\"noserver\""
    process=False
    print("customlist:")
    for input in sys.argv:
        for section, items in inventory.items():
            for key, value in items.items():
                # print(key)
                # print("-----------------")
                if key.split()[0] == input:
                    if section=="web":
                        servertype="\"CHAT SERVER\""
                        process=True
                    if section=="app":
                        servertype="\"ODOO SERVER\""
                        process=True
                    if section=="db":
                        servertype="\"PG SERVER\""
                        process=True
                    if process:
                        temp=value.split()
                        temp1=temp[1].split("=")
                        print("{",end=" ")
                        print("name:",end="")
                        print(servertype,end=" ")
                        print("ip:",end="")
                        print(temp[0],end=" ")
                        print("user:",end="")
                        print(temp1[1],end=" ")
                        print("}")
                        # servertype = "\"noserver\""
                        process=False