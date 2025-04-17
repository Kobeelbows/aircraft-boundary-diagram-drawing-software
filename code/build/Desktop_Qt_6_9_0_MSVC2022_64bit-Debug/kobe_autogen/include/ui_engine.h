/********************************************************************************
** Form generated from reading UI file 'engine.ui'
**
** Created by: Qt User Interface Compiler version 6.9.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ENGINE_H
#define UI_ENGINE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_engine
{
public:
    QPushButton *pushButton1;
    QPushButton *pushButton2;

    void setupUi(QDialog *engine)
    {
        if (engine->objectName().isEmpty())
            engine->setObjectName("engine");
        engine->resize(186, 173);
        pushButton1 = new QPushButton(engine);
        pushButton1->setObjectName("pushButton1");
        pushButton1->setGeometry(QRect(20, 20, 141, 51));
        pushButton2 = new QPushButton(engine);
        pushButton2->setObjectName("pushButton2");
        pushButton2->setGeometry(QRect(20, 90, 141, 51));

        retranslateUi(engine);

        QMetaObject::connectSlotsByName(engine);
    } // setupUi

    void retranslateUi(QDialog *engine)
    {
        engine->setWindowTitle(QCoreApplication::translate("engine", "Dialog", nullptr));
        pushButton1->setText(QCoreApplication::translate("engine", "\346\264\273\345\241\236", nullptr));
        pushButton2->setText(QCoreApplication::translate("engine", "\346\266\241\346\241\250", nullptr));
    } // retranslateUi

};

namespace Ui {
    class engine: public Ui_engine {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ENGINE_H
