class iPhone6:
    def home(self):
        print('Home Button is pressed.')

class iPhoneX(iPhone6):
    def home(self):
        print('Home button is touched')

i6 = iPhone6()
iX = iPhoneX()

i6.home()
iX.home()