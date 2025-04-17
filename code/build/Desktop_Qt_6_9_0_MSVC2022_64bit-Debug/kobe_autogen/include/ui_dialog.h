/********************************************************************************
** Form generated from reading UI file 'dialog.ui'
**
** Created by: Qt User Interface Compiler version 6.9.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DIALOG_H
#define UI_DIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QPushButton *button1;
    QPushButton *button2;
    QPushButton *button3;
    QPushButton *button4;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName("Dialog");
        Dialog->resize(302, 190);
        button1 = new QPushButton(Dialog);
        button1->setObjectName("button1");
        button1->setGeometry(QRect(10, 30, 131, 51));
        button2 = new QPushButton(Dialog);
        button2->setObjectName("button2");
        button2->setGeometry(QRect(160, 30, 131, 51));
        button3 = new QPushButton(Dialog);
        button3->setObjectName("button3");
        button3->setGeometry(QRect(10, 110, 131, 51));
        button4 = new QPushButton(Dialog);
        button4->setObjectName("button4");
        button4->setGeometry(QRect(160, 110, 131, 51));

        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Dialog", nullptr));
        button1->setText(QCoreApplication::translate("Dialog", "\351\200\232\350\210\252\351\243\236\346\234\272\357\274\210\345\215\225\345\217\221\357\274\211", nullptr));
        button2->setText(QCoreApplication::translate("Dialog", "\351\200\232\350\210\252\351\243\236\346\234\272\357\274\210\345\217\214\345\217\221\357\274\211", nullptr));
        button3->setText(QCoreApplication::translate("Dialog", "\345\206\234\347\224\250\351\243\236\346\234\272", nullptr));
        button4->setText(QCoreApplication::translate("Dialog", "\345\217\214\345\217\221\346\266\241\346\241\250\351\243\236\346\234\272", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DIALOG_H
