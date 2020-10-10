import serial
import time
import struct

class NetMatrix:
    def __init__(self, config):
        self.port = serial.Serial(config["port"], config["baudRate"],timeout=2)

    def __del__(self):
        #self.port.write(b'\xaa\x00\x00\x00\x00\x00\x00\xbb')
        self.port.close()

    def stopAll(self):
        # self.port.close()
        # 复位到待接线状态
        pass

    def runcommand(self, cmd):# communication using serial port and how much string number will be read
        command= b'\xaa'+ cmd + b'\xbb'
        self.port.write(command)


    def arrset(self, arr):
        codes = [0,0,0,0]
        for i in range(4):
            for j in range(8):
                byteIdx = j // 2
                bitIdx = ( j % 2 ) * 4 + i
                if arr[i][j] == '1' :
                    codes[byteIdx] = codes[byteIdx] | ( 1<< bitIdx )
        self.port.write(b'\xaa\x00' +bytes(codes) + b'\x00\xbb')

    def relayset(self, cmd):# communication using serial port and how much string number will be read
        '''
        cmd: array[4] eg. ['11111111','00000001','10000000','01000000']
        cmd: array[4] eg. ['12','34','5','7']
        '''
        string = ''
        com = ''
        command =[]
        for counter in range (0,(len(cmd[0]))):
            for count in range(0,len(cmd)):
                string= string+(cmd[count][counter])
                com = bytes(string, encoding = "utf8")

            if counter %2 ==1:
                string = string[::-1]
                print(string)
                #struct.pack('B',)
                com = struct.pack('B',int(string,2))
                command.append(b'\xaa'+ com + b'\xbb')
                string = ''

        for i in range(0,4):
            print(command[i])
            self.port.write(command[i])
        #self.port.write(b'\xaa\x00\x01\x01\x00\x00\x00\xbb')


if __name__ == "__main__":
    # Unit test
    N = NetMatrix({"port": "COM9", "baudRate": 115200})
    # N.runcommand(b'\x00\x01\x01\x00\x00\x00')
    #input("Press ENTER to continue")
    N.arrset(['00000010','00000000','00000000','00000000'])
    #N.toCmd(['11111111','11111111','11111111','11111111'])

