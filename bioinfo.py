# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_bioInfo

class bioInfo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_bioInfo()
        self.ui.setupUi(self)

        # initialization of variables
        self.sequence = None


        # connecting buttons:
        self.ui.load_btn.clicked.connect(self.load_sequence)

    def load_sequence(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open FASTA", "", "FASTA Files (*.fasta *.fa *.txt)")
        if not path:
            return

        record = SeqIO.read(path, "fasta")
        self.sequence = str(record.seq)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = bioInfo()
    widget.show()
    sys.exit(app.exec())
