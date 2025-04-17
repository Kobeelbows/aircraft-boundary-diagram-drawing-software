#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    // 不需要手动 connect，Qt会根据名字自动连接
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_button1_clicked()
{
    emit sendData(2.05f, -0.18f, ui->button1->text());
    close();
}

void Dialog::on_button2_clicked()
{
    emit sendData(1.4f, -0.10f, ui->button2->text());
    close();
}

void Dialog::on_button3_clicked()
{
    emit sendData(0.72f, -0.03f, ui->button3->text());
    close();
}

void Dialog::on_button4_clicked()
{
    emit sendData(0.92f, -0.05f, ui->button4->text());
    close();
}
