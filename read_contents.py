import os


def Counter(address):
    counterNumber = 0
    for path in os.listdir(address):  # Counting the number of all files in folder.
        if os.path.isfile(os.path.join(address, path)):
            counterNumber += 1
    return counterNumber


def read_contents(address, index):  # Read contents of each email that is in a folder.
    # to find the number of all files that we have in each folder.
    addressList = address.split("/")
    listLength = len(addressList)
    fileNames = addressList[listLength - 1]  # Use the last part of the folder address to point to each email.
    email = open(address + '/' + fileNames + ' ' + '(' + str(index) + ')' + '.txt', 'r', encoding="UTF-8")
    text = email.readlines()
    return text
