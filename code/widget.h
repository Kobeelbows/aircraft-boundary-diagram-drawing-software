#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QLineEdit>
#include "dialog.h"
#include "engine.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class Widget;
}
QT_END_NAMESPACE

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

private slots:
    void openDialog();
    void receiveData(float A, float C, QString buttonText);
    void openEngine();
    void receiveEngineData(int enginetype, QString buttonText);
    void onCalculateClicked();
    void plotCurve(double qcc, double cdmin, double k,double densitycc,double vs,double takelength,double landlength,double vv,double qtl,double clmax);

private:
    Ui::Widget *ui;
    Dialog* mydialog;
    engine* myengine;
    float A;
    float C;
    int enginetype;

    // 为 18 个文本框定义变量，使用新的变量名
    double wp;              // 对应 lineEdit_1 (有效载荷 kg)
    double vcc;             // 对应 lineEdit_2 (巡航速度 m/h)
    double heightcc;        // 对应 lineEdit_3 (巡航高度 m)
    double standbyoil;       // 对应 lineEdit_5 (飞行待机用油 min)
    double takelength;      // 对应 lineEdit_6 (起飞场长 m)
    double landlength;      // 对应 lineEdit_7 (着陆场长 m)
    double R;               // 对应 lineEdit_10 (航程 km)
    double sfc;             // 对应 lineEdit_11 (巡航耗油率 kg/kw/s)
    double clmax;           // 对应 lineEdit_12 (最大升力系数 C_lmax)
    double vv;              // 对应 lineEdit_13 (设计爬升率 m/s)
    double vs;              // 对应 lineEdit_14 (失速速度 m/s)
    double initialwto;      // 对应 lineEdit_15 (初始估算重量 kg)
    double lnd;             // 对应 lineEdit_18 (升阻比)
    double ar;             // 对应 lineEdit_20 (展弦比)
    double perfuel;         // 燃油系数
    double qcc;
    double cdmin;
    double k;
    double n;
    double roundfunc(double x);
    double qtl;


};

#endif // WIDGET_H
