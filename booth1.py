import sys
from PyQt5 import uic, QtWidgets
from bitwise import *

qtCreatorFile = "untitled.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class aplication(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn1.clicked.connect(self.main)

    def main(self):
        print("This program excecutes Booth's multiplication algorithm.\n")
        print("The formula it's going to calculate is:  M * R = ?")
        print("Input the bit length of first variable M: ", end="")
        mlen = int(self.b.toPlainText())
        print("Input the bit length of second variable R: ", end="")

       #mlen = int(input())

        print("Input the number of first variable M: ", end="")
        m = int(self.x.toPlainText())
        if m < 0:
            m = TwoComp(("{0:0%db}" % mlen).format(m))  # Calculate the two's complement number of m
        else:
            m = ("{0:0%db}" % mlen).format(m)  # Convert to bits and assign directly

        print("Input the number of second variable R: ", end="")
        r = int(self.y.toPlainText())
        if r < 0:
            r = TwoComp(("{0:0%db}" % mlen).format(r))
        else:
            r = ("{0:0%db}" % mlen).format(r)

        ilen = mlen + mlen + 1  # The common length of internal variables
        a = m + GenZeroStr(mlen + 1)  # A: place M in leftmost position. Fill the left bits with 0.
        s = TwoComp(m) + GenZeroStr(mlen + 1)  # S: place negative M in leftmost position.
        p = GenZeroStr(mlen) + r + "0"  # P: place R by rightmost 0.

        for i in range(mlen):  # Do operation mlen times
            op = p[-2:]
            print("    " + "The last 2 bits of p are: %s" % "".join(op))
            if op == "10":
                p = BitAdd(p, s, len(p))
            elif op == "01":
                p = BitAdd(p, a, len(p))
            elif op == "00":
                print("    ")
            elif op == "11":
                print("    ")

            p = BitShift(p, 1)
            self.r.setText("    " + "P = %s\n" % p)

        p = p[:-1]
        self.r.setText("The answer is: %s" % p)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = aplication()
    window.show()
    sys.exit(app.exec_())
