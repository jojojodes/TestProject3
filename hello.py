# A Python example program

import platform

def hello():
    print('Hello World!')
    print('I am running on: ', platform.platform())

    if __name__== '__main__':
        hello()
