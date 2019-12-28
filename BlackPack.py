#!/usr/bin/env python3
import sys, os, shutil, glob
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui import main
from ui import progress
from os import path as p
from subprocess import getoutput
from time import sleep
 
 
class MainWizard(QWizard):
    changeProgress = pyqtSignal(int, str)
    exitSignal = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super(MainWizard, self).__init__(*args, **kwargs)
        
        self.MainWizard = main.Ui_BlackPackWizard()
        self.MainWizard.setupUi(self)
    
        self.MainWizard.pkgname.textChanged.connect(self.setPkgname)
        self.MainWizard.pushButton.clicked.connect(self.browse1File)
        self.MainWizard.toolButton.clicked.connect(self.browse2File)
        self.MainWizard.pushButton_8.clicked.connect(self.browse3File)
        self.MainWizard.pushButton_2.clicked.connect(self.addFile)
        self.MainWizard.pushButton_9.clicked.connect(self.addFolder)
        self.MainWizard.pushButton_6.clicked.connect(self.addPkg)
        self.MainWizard.pushButton_5.clicked.connect(self.removePkg)
        self.MainWizard.pushButton_7.clicked.connect(self.cleanPkg)
        self.MainWizard.pushButton_3.clicked.connect(self.removeFolder)
        self.MainWizard.pushButton_4.clicked.connect(self.cleanFolder)
        
        self.MainWizard.pkgname_2.textEdited.connect(self.updateDesktopSection)
        self.MainWizard.pkgversion_2.textEdited.connect(self.updateDesktopSection)
        self.MainWizard.pkgrelease_2.textEdited.connect(self.updateDesktopSection)
        self.MainWizard.pkgsummary_2.textEdited.connect(self.updateDesktopSection)
        self.MainWizard.checkBox.clicked.connect(self.updateDesktopSection)
        self.MainWizard.pkgrelease_3.textEdited.connect(self.updateDesktopSection)
        
        self.MainWizard.pushButton_10.clicked.connect(self.addSource)
        self.MainWizard.pushButton_11.clicked.connect(self.removeSource)
        self.MainWizard.pushButton_12.clicked.connect(self.removeAllSources)
        self.MainWizard.toolButton_2.clicked.connect(self.searchSource)
        
        self.accepted.connect(self.runBuild)
    
        self.changeProgress.connect(self.changeProgressInDialog)
        self.exitSignal.connect(self.allDone)
    
    def removeSource(self):
        item = self.MainWizard.listWidget_3.currentRow()
        self.MainWizard.listWidget_3.takeItem(item)
        
    def removeAllSources(self):
        deleteconfirmation = QMessageBox.critical(self.parent(), "Delete row", "Really delete the all selected packages?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            self.MainWizard.listWidget_3.clear()
            return None
        else:
            return None
        
    def searchSource(self):
        dialog = QFileDialog()
        sourcepath, tmp= dialog.getOpenFileName(self, 'Open Tarball source', p.expanduser("~"),"Tarball sources (*.tar.gz)")
        self.MainWizard.lineEdit_10.setText(sourcepath)
    
    def addSource(self):
        sourcepath = self.MainWizard.lineEdit_10.text()
        if not sourcepath:
            self.searchSource()
        if p.isfile(sourcepath) and sourcepath[-7:] == ".tar.gz":
            self.MainWizard.listWidget_3.addItem(sourcepath)
        
    @pyqtSlot(str)
    def allDone(self, log):
        arch = self.MainWizard.comboBox_3.currentText()
        try:
            for rpm in glob.glob(p.join(p.expanduser("~"), "rpmbuild/RPMS", arch, "*.rpm")):
                if p.exists(rpm):
                    print("All done, rpm is in: " + rpm)
            saveto, rpmtype = QFileDialog.getSaveFileName(self, 'Save RPM ...', p.basename(rpm), ("RedHat Package File (*.rpm)"))
            saveto = str(saveto)
            if saveto:
                shutil.move(rpm, saveto)
                os.system('xdg-open "' + p.dirname(saveto) + '"')
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Package building error!")
            msg.setInformativeText(log)
            msg.setWindowTitle("Error")
            msg.exec_()
            self.show()
        self.progressDialog.close()
        deleteconfirmation = QMessageBox.critical(self.parent(), "BlackPack RPM builder", "Delete build tree?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            shutil.rmtree(p.join(p.expanduser("~"), "rpmbuild"))
            return None
        else:
            return None
        
    @pyqtSlot(int, str)
    def changeProgressInDialog(self, percent, process):
        self.progressDialog.Dialog.progressBar.setValue(percent)
        self.progressDialog.Dialog.label_3.setText(process)
    def updateDesktopSection(self):
        if self.MainWizard.checkBox.isChecked():
            desktopteminal = "True"
        else:
            desktopteminal = 'False'
        desktopfile = """[Desktop Entry]
Encoding=UTF-8
Version=1.0
Type=Application
Terminal="""+desktopteminal+"""
Exec="""+self.MainWizard.pkgsummary_2.text()+"""
Name="""+self.MainWizard.pkgname_2.text()+"""
Icon="""+self.MainWizard.pkgversion_2.text()+"""
Categories="""+self.MainWizard.pkgrelease_3.text()+"""
Comment="""+self.MainWizard.pkgrelease_2.text()+"""
"""
        self.MainWizard.pkgdesc_2.setPlainText(desktopfile)
        
    def runBuild(self):
        self.loadthread = BuildPackage(self.MainWizard, self.changeProgress, self.exitSignal)
        self.exitSignal.connect(self.show)
        self.loadthread.start()
        self.progressDialog = ProgressDialog()
        self.progressDialog.show()
     
 
    def cleanFolder(self):
        rowPosition = self.MainWizard.tableWidget.rowCount()
        deleteconfirmation = QMessageBox.critical(self.parent(), "Delete row", "Really delete the all selected packages?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            self.MainWizard.tableWidget.setRowCount(0)
            return None
        else:
            return None
    def removeFolder(self):
        index = self.MainWizard.tableWidget.currentIndex()
        deleteconfirmation = QMessageBox.critical(self.parent(), "Delete row", "Really delete this file/direcotry from yout project?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            self.MainWizard.tableWidget.removeRow(index.row())
            return None
        else:
            return None
    def cleanPkg(self):
        rowPosition = self.MainWizard.tableWidget_2.rowCount()
        deleteconfirmation = QMessageBox.critical(self.parent(), "Delete row", "Really delete the all selected packages?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            self.MainWizard.tableWidget_2.setRowCount(0)
            return None
        else:
            return None
    def removePkg(self):
        index = self.MainWizard.tableWidget_2.currentIndex()
        deleteconfirmation = QMessageBox.critical(self.parent(), "Delete row", "Really delete the selected package?", QMessageBox.Yes, QMessageBox.No)
        if deleteconfirmation == QMessageBox.Yes:
            self.MainWizard.tableWidget_2.removeRow(index.row())
            return None
        else:
            return None
    def addPkg(self):
        pkgname = self.MainWizard.lineEdit_3.text()
        pkgver = self.MainWizard.lineEdit_4.text()
        rowPosition = self.MainWizard.tableWidget_2.rowCount()
        self.MainWizard.tableWidget_2.insertRow(rowPosition)
        self.MainWizard.tableWidget_2.setItem(rowPosition , 0, QTableWidgetItem(pkgname))
        self.MainWizard.tableWidget_2.setItem(rowPosition , 1, QTableWidgetItem(pkgver))
    def addFolder(self):
        dirname = p.normpath(self.MainWizard.lineEdit_6.text())
        if not dirname[:1] == "/":
            print("[error]: Bad direcotry name!")
            return None
        self.MainWizard.lineEdit_6.clear()
        rowPosition = self.MainWizard.tableWidget.rowCount()
        self.MainWizard.tableWidget.insertRow(rowPosition)
        self.MainWizard.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(""))
        self.MainWizard.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(dirname))
    def addFile(self):
        if self.MainWizard.lineEdit.text() == "" or not p.exists(self.MainWizard.lineEdit.text()): 
            print("[error]: File not exists!")
            return None
        if self.MainWizard.radioButton.isChecked():
            copyto = self.MainWizard.comboBox_2.currentText()
            rowPosition = self.MainWizard.tableWidget.rowCount()
            if self.MainWizard.checkBox_2.isChecked():
                newname = self.MainWizard.lineEdit_5.text()
                if "<package_name>" in copyto and p.isdir(self.MainWizard.lineEdit.text()):
                    copyto = copyto.replace("<package_name>", newname)
                elif "<package_name>" in copyto and p.isfile(self.MainWizard.lineEdit.text()):
                    copyto = copyto.replace("<package_name>", self.MainWizard.pkgname.text())
                    copyto = p.join(copyto, newname)
                else:
                    copyto = p.join(copyto, newname)
            else:
                if "<package_name>" in copyto and p.isdir(self.MainWizard.lineEdit.text()):
                    copyto = copyto.replace("<package_name>", self.MainWizard.pkgname.text())
                elif "<package_name>" in copyto and p.isfile(self.MainWizard.lineEdit.text()):
                    copyto = copyto.replace("<package_name>", self.MainWizard.pkgname.text())
                    copyto = p.join(copyto, p.basename(self.MainWizard.lineEdit.text()))
                else:
                    copyto = p.join(copyto, p.basename(self.MainWizard.lineEdit.text()))
        elif self.MainWizard.lineEdit_2.text() == "" or not p.exists(self.MainWizard.lineEdit_2.text()):
            print("[error]: File not exists!")
            return None
        if self.MainWizard.radioButton_2.isChecked():
            copyto = p.join(self.MainWizard.lineEdit_2.text(), p.basename(self.MainWizard.lineEdit.text()))
        if self.MainWizard.checkBox_2.isChecked() and not self.MainWizard.radioButton.isChecked():
            newname = self.MainWizard.lineEdit_5.text()
            copyto = p.join(p.dirname(copyto), newname)
        rowPosition = self.MainWizard.tableWidget.rowCount()
        self.MainWizard.tableWidget.insertRow(rowPosition)
        self.MainWizard.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(p.normpath(self.MainWizard.lineEdit.text())))
        self.MainWizard.tableWidget.setItem(rowPosition , 1, QTableWidgetItem(p.normpath(copyto)))
    def setPkgname(self, text):
        pkgname = str(text).lower().replace(" ", "-")
        self.MainWizard.pkgname.setText(pkgname)
        self.MainWizard.label_17.setText("Will save in /usr/share/doc/<program_name>/copyright".replace("<program_name>", pkgname))
        
    def browse1File(self):
        dialog = QFileDialog(self, 'All files ...', p.expanduser("~"))
        dialog.setFileMode(QFileDialog.AnyFile)
        if dialog.exec_() == QDialog.Accepted:
            file = dialog.selectedFiles()[0]
            self.MainWizard.lineEdit.setText(file)
    def browse2File(self):
        dialog = QFileDialog(self, 'Install to ...', "/")
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            file = dialog.selectedFiles()[0]
            self.MainWizard.lineEdit_2.setText(file)
    def browse3File(self):
        dialog = QFileDialog(self, 'All files ...', p.expanduser("~"))
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            file = dialog.selectedFiles()[0]
            self.MainWizard.lineEdit.setText(file)

class BuildPackage(QThread):
    def __init__(self, parent, signal1, signal2):
        QThread.__init__(self)
        self.MainWizard = parent
        self.changeProgress = signal1
        self.exitSignal = signal2 
    @pyqtSlot()
    def run(self):
        self.changeProgress.emit(10, "Removing old rpmbuild ...")
        if p.isdir(p.join(p.expanduser("~"), "rpmbuild")):
            print("- Removing old rpmbuild-tree ...")
            shutil.rmtree(p.join(p.expanduser("~"), "rpmbuild"))
        self.changeProgress.emit(20, "Making new build tree (rpmbuild) ...")
        print("- Building rpm-build tree ...")
        os.system("rpmdev-setuptree")
        
        self.changeProgress.emit(30, "Writing SPEC (part 1) ...")
        self.specfiles = "/usr/share/doc/" + self.MainWizard.pkgname.text()
        for item in range(self.MainWizard.tableWidget.rowCount()):
            item = self.MainWizard.tableWidget.item(item, 1).text() 
            self.specfiles = self.specfiles + '\n"' + item + '"'
        
        self.changeProgress.emit(40, "Adding license to package ...")
        lic = p.join(p.expanduser("~"), "rpmbuild/BUILD", "usr/share/doc/" +self.MainWizard.pkgname.text()) + "/copyright"
        os.makedirs(p.dirname(lic))
        open(lic, 'a').close()
        f = open(lic, 'a')
        f.write(self.MainWizard.plainTextEdit_6.toPlainText())
        f.close()
        
        if self.MainWizard.groupBox_5.isChecked():
            self.changeProgress.emit(45, "Adding menu launcher ...")
            desktopfiletext = self.MainWizard.pkgdesc_2.toPlainText()
            appname = self.MainWizard.pkgname_2.text()
            desktopfile = p.join(p.expanduser("~"), "rpmbuild/BUILD/usr/share/applications", appname.replace(" ", "_") + ".desktop")
            if not p.exists(p.dirname(desktopfile)):
                os.makedirs(p.dirname(desktopfile))
            open(desktopfile, 'a').close()
            f = open(desktopfile, 'a')
            f.write(desktopfiletext)
            f.close()
            self.specfiles = self.specfiles + "\n" + p.join("/usr/share/applications", appname.replace(" ", "_") + ".desktop")  
        self.changeProgress.emit(60, "Writing SPEC (part 2) ...")
        self.requires = "Requires:    "
        for item in range(self.MainWizard.tableWidget_2.rowCount()):
            pkgname = ""
            pkgname = self.MainWizard.tableWidget_2.item(item, 0).text()
            pkgversion = self.MainWizard.tableWidget_2.item(item, 1).text()
            if pkgname:
                if not pkgversion and not self.requires:
                    self.requires = pkgname
                elif not pkgversion and self.requires:
                    self.requires = self.requires + ", " + pkgname
                elif not self.requires and pkgversion:
                    self.requires = pkgname + " >= " + str(pkgversion)
                elif self.requires and pkgversion:
                    self.requires = self.requires + ", " + pkgname + " >= " + str(pkgversion)
            else:
                print("[warning]: No package name only version ("+pkgversion+")! - skkiping")
        
        if self.requires == "Requires:    ":
            self.requires = ""
        
        
        if not self.specfiles.count('\n') == 0:
            progress = int(70 / int(self.specfiles.count('\n')))
        if not range(self.MainWizard.tableWidget.rowCount()):
            self.exitSignal.emit("No files selected ...")
            return None
        self.changeProgress.emit(70, "Copying files (please be patient) ...")
        for item in range(self.MainWizard.tableWidget.rowCount()):
            src = self.MainWizard.tableWidget.item(item, 0).text() 
            dst = p.join(p.expanduser("~"), "rpmbuild", "BUILD", self.MainWizard.tableWidget.item(item, 1).text()[1:])
            print("Copy from: '" + src + "' to '" +dst +"'")
            if p.isdir(src):
                shutil.copytree(src, dst)
            elif p.isfile(src):
                if not p.exists(p.dirname(dst)):
                    os.makedirs(p.dirname(dst))
                shutil.copy(src,dst)
            
            value = progress + progress
        self.changeProgress.emit(30, "Writing SPEC (part 3) ...")
        self.sources = ""
        
        for item in range(self.MainWizard.listWidget_3.count()):
            name = self.MainWizard.listWidget_3.item(item)
            shutil.copy(name.text(), p.join(p.expanduser("~"), "rpmbuild/SOURCES", p.basename(name.text())))
            self.sources = self.sources+ "Source" + str(item) + ":    " + p.basename(name.text()) + "\n"
            
        spec = """Name:    """ + self.MainWizard.pkgname.text() + """
Version:    """ + self.MainWizard.pkgversion.text() + """
Release:    """ + self.MainWizard.pkgrelease.text() + """
Summary:    """ + self.MainWizard.pkgsummary.text() + """
License:    """ + self.MainWizard.comboBox.currentText() + """
Url:    """ + self.MainWizard.lineEdit_7.text() + """\n""" + self.sources + """
""" + self.requires + """

%description
""" + self.MainWizard.pkgdesc.toPlainText() + """

%prep
""" + self.MainWizard.plainTextEdit.toPlainText() + """

%build
""" + self.MainWizard.plainTextEdit_2.toPlainText() + """

%install
""" + self.MainWizard.plainTextEdit_3.toPlainText() + """

%files
""" + self.specfiles + """

%clean

%changelog
""" + self.MainWizard.plainTextEdit_5.toPlainText() + """
%check
""" + self.MainWizard.plainTextEdit_4.toPlainText() + """
%post
""" + self.MainWizard.plainTextEdit_11.toPlainText() + """
%pre
""" + self.MainWizard.plainTextEdit_12.toPlainText() + """
%preun
""" + self.MainWizard.plainTextEdit_13.toPlainText() + """
%postun
""" + self.MainWizard.plainTextEdit_14.toPlainText()

        specfile = p.join(p.expanduser("~"), "rpmbuild", "SPECS", self.MainWizard.pkgname.text() + ".spec")
        open(specfile, 'a').close()
        f= open(specfile,"a")
        f.write(spec)
        f.close()
        
        self.changeProgress.emit(99, "Building RPM package (please be patient) ...")
        cmd = "QA_SKIP_RPATHS=true rpmbuild -v -bb " + specfile + " > /tmp/rpmbuild-blackpack.log"
        log = getoutput(cmd)
        
        self.exitSignal.emit(log)

class ProgressDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.Dialog = progress.Ui_Dialog()
        self.Dialog.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWizard()
    ui.show()
    sys.exit(app.exec_())

