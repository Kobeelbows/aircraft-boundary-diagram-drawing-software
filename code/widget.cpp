#include "widget.h"
#include "./ui_widget.h"
#include <QMessageBox>
#include <QRandomGenerator>
#include <cmath>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QGraphicsLineItem>

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    mydialog = new Dialog(this);
    connect(ui->pushButton, &QPushButton::clicked, this, &Widget::openDialog);
    connect(mydialog, &Dialog::sendData, this, &Widget::receiveData);

    myengine = new engine(this);
    connect(ui->pushButton2, &QPushButton::clicked, this, &Widget::openEngine);
    connect(myengine, &engine::sendData, this, &Widget::receiveEngineData);

    connect(ui->pushButton_2, &QPushButton::clicked, this, &Widget::onCalculateClicked);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::openDialog()
{
    mydialog->show();
}

void Widget::receiveData(float a, float c, QString buttonText)
{
    A = a;
    C = c;
    ui->pushButton->setText(buttonText);
}

void Widget::openEngine()
{
    myengine->show();
}

void Widget::receiveEngineData(int type, QString buttonText)
{
    enginetype = type;
    ui->pushButton2->setText(buttonText);
}

void Widget::plotCurve(double qcc, double cdmin, double k, double densitycc, double vs, double takelength, double landlength, double vv, double qtl, double clmax)
{
    QGraphicsScene *scene = new QGraphicsScene(this);
    ui->graphicsView->setScene(scene);

    ui->graphicsView->setRenderHint(QPainter::Antialiasing);
    ui->graphicsView->setSceneRect(0, -200, 400, 200);

    double step = 0.1;
    double xStart = 0.0;  // 从0开始
    double xEnd = 120.0;  // 到120结束

    double scaleX = 2.0;
    double scaleY = 300;

    QPointF lastPoint2, lastPoint3, lastPoint4, lastPoint5;

    for (double x = xStart; x <= xEnd; x += step)
    {
        double y2 = (vv) / (2 * x * std::sqrt(k / (3 * cdmin)) / 1.225) + (cdmin / x) + (k * x / qtl);
        double y3 = (1.1 * vs) * (1.1 * vs) / 2 / 9.81 / takelength + qtl * 0.0425 / x + 0.04 - 0.04 * qtl * 0.7 / x;
        double y4 = qtl*cdmin/x+k*x/qtl;
        double y5 = 0.01 * vcc / (2 * x * std::sqrt(k / (3 * cdmin)) / densitycc) + 4 * std::sqrt(k * cdmin / 3);
        double x_target = 0.5 * clmax * 1.225 * vs * vs;
        double x_target2 = 1.225 * clmax * (landlength - 183) / 5;

        QPointF point2(x * scaleX, -y2 * scaleY);
        QPointF point3(x * scaleX, -y3 * scaleY);
        QPointF point4(x * scaleX, -y4 * scaleY);
        QPointF point5(x * scaleX, -y5 * scaleY);

        if (x != xStart)
        {
            scene->addLine(QLineF(lastPoint2, point2), QPen(Qt::red));
            scene->addLine(QLineF(lastPoint3, point3), QPen(Qt::green));
            scene->addLine(QLineF(lastPoint4, point4), QPen(Qt::blue));
            scene->addLine(QLineF(lastPoint5, point5), QPen(Qt::red));
            scene->addLine(x_target * scaleX, -200, x_target * scaleX, 0, QPen(Qt::black, 2, Qt::DashLine));
            scene->addLine(x_target2 * scaleX, -200, x_target2 * scaleX, 0, QPen(Qt::red, 2, Qt::DashLine));
        }

        lastPoint2 = point2;
        lastPoint3 = point3;
        lastPoint4 = point4;
        lastPoint5 = point5;
    }

    // 坐标轴
    scene->addLine(0, 0, 400, 0, QPen(Qt::black));  // x轴
    scene->addLine(0, 0, 0, -200, QPen(Qt::black)); // y轴

    // 刻度线 + 数字
    QFont font;
    font.setPointSize(8);

    // x轴刻度
    for (int i = 0; i <= 120; i += 20) {  // 修改x轴刻度范围为0到120
        scene->addLine(i * scaleX, 0, i * scaleX, -5, QPen(Qt::black)); // 注意x放大了scaleX倍
        QGraphicsTextItem *text = scene->addText(QString::number(i), font); // x轴的数字
        text->setPos(i * scaleX - 10, 5); // 调整位置
    }

    // y轴刻度
    for (int i = 0; i <= 200; i += 20) {
        scene->addLine(0, -i, 5, -i, QPen(Qt::black));
        QGraphicsTextItem *text = scene->addText(QString::number(i / scaleY), font);
        text->setPos(-25, -i - 8); // 调整位置
    }
}



void Widget::onCalculateClicked()
{
    bool ok = true; // 在外部初始化 ok
    auto getFloatFromLineEdit = [&](QLineEdit *edit, const QString &warning) -> float {
        bool tempOk;
        float value = edit->text().toFloat(&tempOk);
        ok &= tempOk; // 更新 ok
        if (!tempOk) {
            QMessageBox::warning(this, "输入错误", warning);
        }
        return value;
    };

    wp = getFloatFromLineEdit(ui->lineEdit_1, "请输入有效的有效载荷喵！");
    vcc = getFloatFromLineEdit(ui->lineEdit_2, "请输入有效的巡航速度喵！");
    heightcc = getFloatFromLineEdit(ui->lineEdit_3, "请输入有效的巡航高度喵！");
    standbyoil = getFloatFromLineEdit(ui->lineEdit_5, "请输入有效的飞行待机用油喵！");
    takelength = getFloatFromLineEdit(ui->lineEdit_6, "请输入有效的起飞场长喵！");
    landlength = getFloatFromLineEdit(ui->lineEdit_7, "请输入有效的着陆场长喵！");
    R = getFloatFromLineEdit(ui->lineEdit_10, "请输入有效的航程喵！");
    sfc = getFloatFromLineEdit(ui->lineEdit_11, "请输入有效的巡航耗油率喵！");
    clmax = getFloatFromLineEdit(ui->lineEdit_12, "请输入有效的最大升力系数喵！");
    vv = getFloatFromLineEdit(ui->lineEdit_13, "请输入有效的设计爬升率喵！");
    vs = getFloatFromLineEdit(ui->lineEdit_14, "请输入有效的失速速度喵！");
    initialwto = getFloatFromLineEdit(ui->lineEdit_15, "请输入有效的初始估算重量喵！");
    lnd = getFloatFromLineEdit(ui->lineEdit_18, "请输入有效的升阻比喵！");
    ar = getFloatFromLineEdit(ui->lineEdit_20, "请输入有效的展弦比喵！");

    if (!ok) return; // 有任何一个输入错误就退出

    // 计算燃油系数
    double E = standbyoil / 100.0;
    double rnd1 = 0.97 + (0.975 - 0.97) * QRandomGenerator::global()->generateDouble();  // 起飞重量调整因子
    double rnd2 = 0.990 + (0.995 - 0.990) * QRandomGenerator::global()->generateDouble(); // 飞行任务调整因子
    double rnd3 = 0.992 + (0.997 - 0.992) * QRandomGenerator::global()->generateDouble(); // 备降调整因子

    double term1 = std::exp(-R * sfc / vcc / lnd);
    double term2 = std::exp(-E * sfc / lnd);
    double perfuel = 1.06 * (1 - rnd1 * 0.985 * term1 * term2 * rnd2 * rnd3);

    // 计算空重系数
    double perempty = A * std::pow(initialwto, C);
    double wto;
    double error = 1.0;
    int maxIterations = 1000;
    int iteration = 0;

    while (error > 1e-6 && iteration < maxIterations) {
        double denominator = 1 - perempty - perfuel;
        if (denominator <= 0) {
            QMessageBox::warning(this, "计算错误", "分母为0或负数，无法计算喵！");
            return;
        }
        wto = wp / denominator;
        error = std::fabs((wto - initialwto) / wto);
        initialwto = wto;
        iteration++;
    }

    if (iteration >= maxIterations) {
        QMessageBox::warning(this, "计算错误", "最大起飞重量迭代未收敛喵！");
        return;
    }

    // 计算界限线图参数
    double densitycc = 1.225 * std::pow((1 - 0.0065 * heightcc / 288.15), 4.25588); // 标准大气模型
    double cdmin = 0.0325;
    double k = 1.0 / (M_PI * 0.8 * ar);
    double qcc = 0.5 * densitycc * vcc * vcc;
    double qtl = 0.5 * 1.225*1.21*vs*vs;
    // 绘制界限线图
    plotCurve(qcc, cdmin, k,  densitycc, vs, takelength, landlength, vv,qtl,clmax);

}
