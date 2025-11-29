# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QHeaderView
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction, molecular_weight

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
        self.widgetIndex = 0


        # setup window:

        self.ui.stackedWidget.setCurrentIndex(0)

        # connecting buttons:
        self.ui.load_btn.clicked.connect(self.load_sequence)

        # setup stack
        self.ui.info_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # setup selector
        self.ui.select_DNA.currentIndexChanged.connect(self.on_change_seq)

        # setup_base_table
        self.ui.base_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def on_change_seq(self, index):
        if index < 0:
            return
        if self.sequence is not None:
            self.update_info(self.sequence[index])
        return

    def load_sequence(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open FASTA", "", "FASTA Files (*.fasta *.fa *.txt)")
        if not path:
            return

        records = list(SeqIO.parse(path, "fasta"))
        self.sequence = records
        self.ui.select_DNA.clear()
        for r in records:
            self.ui.select_DNA.addItem(r.id)
        self.update_info(records[0])
        self.ui.stackedWidget.setCurrentIndex(1)

    def update_info(self, record):
        seq = str(record.seq)

        seq_type = "Unknown"
        if set(seq.upper()).issubset(set("ACGTUN")):
            seq_type =  "DNA/RNA"
        elif any(ch in "EFILPQZ" for ch in seq.upper()):
            seq_type =  "Protein"

        # Basic labels
        self.ui.id_label.setText(f"ID: {record.id}")
        self.ui.desc_label.setText(f"Description: {record.description}")
        self.ui.len_label.setText(f"Length: {len(seq)} bp")
        self.ui.type_label.setText(f"Type: {seq_type}")

        # GC content
        gc = gc_fraction(seq) * 100
        self.ui.gc_label.setText(f"GC%: {gc:.2f}")

        # AT/GC ratio
        A = seq.count("A")
        T = seq.count("T")
        G = seq.count("G")
        Cc = seq.count("C")
        atgc_ratio = (A + T) / (G + Cc + 0.0001)
        self.ui.atgc_label.setText(f"AT/GC Ratio: {atgc_ratio:.2f}")

        # Molecular weight
        try:
            mw = molecular_weight(seq, seq_type="DNA")
            self.ui.mw_label.setText(f"Molecular Weight: {mw:.2f} Da")
        except:
            self.ui.mw_label.setText("Molecular Weight: -")

        # Update composition table
        self.ui.base_table.item(0, 0).setText(f"{A}")
        self.ui.base_table.item(0, 1).setText(f"{T}")
        self.ui.base_table.item(0, 2).setText(f"{G}")
        self.ui.base_table.item(0, 3).setText(f"{Cc}")

        # Sequence viewer
        self.ui.sequence_view.setText(seq)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = bioInfo()
    widget.show()
    sys.exit(app.exec())
