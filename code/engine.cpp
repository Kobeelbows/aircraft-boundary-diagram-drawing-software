#include "engine.h"
#include "ui_engine.h"

engine::engine(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::engine)
{
    ui->setupUi(this);
    // 自动connect，不用手写connect
}

engine::~engine()
{
    delete ui;
}

void engine::on_pushButton1_clicked()
{
    emit sendData(1, ui->pushButton1->text()); // enginetype = 1
    close();
}

void engine::on_pushButton2_clicked()
{
    emit sendData(2, ui->pushButton2->text()); // enginetype = 2
    close();
}
