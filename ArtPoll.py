class ArtPoll:
    def __init__(self, data):
        self.id = data[:8]
        opCodeLo = data[8]
        opCodeHi = data[9]
        self.opCode = int.from_bytes(opCodeHi+opCodeLo, byteorder="big")
        protVerHi = data[10]
        protVerLo = data[11]
        self.protVer = int.from_bytes(protVerHi+protVerLo, byteorder="big")
        self.talkToMe = data[12]
        self.priority = data[13]

        self.valid = False
        self.validate()



    def validate(self):#TODO: Fix validation of the package data
        self.valid = True