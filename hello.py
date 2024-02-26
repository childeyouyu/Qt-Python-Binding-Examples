# /usr/bin/env python
import sys

from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

hello = QLabel("hello Qt")
hello.show()
x, y, w, h = 200, 200, 100, 100
hello.setGeometry(x, y, w, h)

sys.exit(app.exec())
