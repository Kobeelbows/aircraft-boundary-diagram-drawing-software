#ifndef ENGINE_H
#define ENGINE_H

#include <QDialog>

namespace Ui {
class engine;
}

class engine : public QDialog
{
    Q_OBJECT

public:
    explicit engine(QWidget *parent = nullptr);
    ~engine();

signals:
    void sendData(int enginetype, QString buttonText); // 改：增加 QString

private slots:
    void on_pushButton1_clicked(); // 注意大小写
    void on_pushButton2_clicked();

private:
    Ui::engine *ui;
};

#endif // ENGINE_H
