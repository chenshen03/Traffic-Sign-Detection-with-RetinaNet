# Traffic-Sign-Detection-with-RetinaNet
## Introduction

在这个项目里，我们实现了基于[RetinaNet](https://arxiv.org/pdf/1708.02002.pdf) 的交通标志检测算法。该项目主要代码参考自：[Simultaneous-Traffic-Sign-Detection-and-Classification-with-RetinaNet](https://github.com/CJHMPower/Simultaneous-Traffic-Sign-Detection-and-Classification-with-RetinaNet)。我们对数据集和代码进行了部分更改，使其能够在pytorch1.0版本下正常运行，并实现了一个五类的交通标志检测任务。

RetinaNet是 Facebook AI 团队在 2018 年提出的目标检测框架。 RetinaNet 结合了 FPN 网络与FCN 网络， 在目标网络检测框架上并无特别亮眼点， 其最大创新在于 Focal loss 的提出以及在 onestage 目标检测网络的成功应用。 Focal loss 是一种改进的交叉熵损失（cross-entropy, CE），它通过在原有的交叉熵损失上乘上一个衰减因子， 使得 Focal loss 成功地解决了目标检测中的类别不平衡问题。 RetinaNet 的作者通过后续实验成功表明 Focal loss 可以成功应用在 one-stage 目标检测网络中，并最终能以更快的速率实现与 two-stage 目标检测网络近似或更优的效果。 

## Dataset

### CVTS数据集

Computer Vision Traffic Sign，CVTS是计算机视觉课程上所有人手工标注得到的交通标志数据集。一共有警告、禁令、指示、道路、交通灯五大类别，每个大类别又包含若干个小类别，共77个小类别。其部分类别示例如下图所示：

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxslc95x7j20b606vjti.jpg)

**数据清理：**

CVTS数据集共包含2620张图片，但由于标注质量参差不齐，存在漏标、误标、检测框未对齐等多种情况，原始数据无法直接用以网络训练。因此，我们对CVTS数据集进行了清理，去除掉图片质量和标注质量较差的数据。经过清理之后，得到的数据集共有1250张，分别包含了754个红绿灯标志、623个禁令标志、345个指路标志以及244个警告标志。显然，清理后的数据集存在着不同类别上的数据量不平衡的问题。

**数据增强：**

为了确保网络在每个类别上的表现均衡，我们对清理后的数据集进行了数据增强，确保每个类别的图片量都在1000张以上。经过数据增强后，得到的数据集包含6333张图片，数据量大致确保了在小型网络上能够得到相对较好的结果。

### Tsinghua_Tencent_100K数据集

[Tsinghua_Tencent_100K](https://cg.cs.tsinghua.edu.cn/traffic-sign/)是清华大学在2016年发布的交通标志数据集。该数据集是从1,000,000张腾讯街景图片中选取的300,000张交通标志图片构成。在去除掉出现次数少于100次的交通标志数据后，得到的数据集共有37212张图片，共包含指示标志、禁令标志、警告标志3个大类，其中又细分为42个小类。其交通标志示例下图所示。

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxsmx6zuqj20eg06qmyy.jpg)

**类别转换：**

为了将Tsinghua_Tencent_100K数据集应用到我们的五类交通标志检测任务中，我们对该数据集的类别进行了转换，将以**i**开头的类别转换为**s**（指示标志），以**p**开头的类别转换为**z**（禁令标志），以**w**开头的类别转换为**j**（警告标志）。

**数据合并：**

Tsinghua_Tencent_100K的交通标志数据具有很好的标注质量，能够有效得提高算法的检测准确度，因此我们从该数据集的三大类中随机采样1000张图片，和CVTS数据集合并起来，从而构成了我们最后实验中所使用的数据集：*CVTS-TT100K*。

CVTS-TT100K数据集共包含9333张图片，包含了警告标志、禁令标志、指示标志、道路标志和交通灯五个类别。我们从CVTS-TT100K中随机采样1000张图片作为测试集，剩下的8333张图片作为训练集。

## Model

- 代码中所采用的数据集：[CVTS-TT100K](https://pan.baidu.com/s/1z5X9kmo_9uJPl0GBLFItgA)
- 在CVTS-TT100K和resnet101上训练得到的模型：[resnet101_8K.pth](https://pan.baidu.com/s/1YB74Fzkxs_NyKxSY0nD93A)
- 在Tsinghua_Tencent_100K和resnet152训练得到的模型：[resnet152_40K.pth](https://pan.baidu.com/s/1-DKlXwq6olEbQherzaDFRw)

## Usage

利用预训练模型对 /samples 文件夹下的图片进行检测，并将检测结果输出在 /result 文件夹下：

```python
python test.py -m demo
```

利用预训练模型测试在验证集上的表现，并在预测结果（json文件）输出到 /data 文件夹下：

```python
python test.py -m valid
```

训练网络：

```python
python train.py -exp model
```

evaluate 文件下有着许多实用代码：

- crop_image：对数据集进行resize和增强操作；
- eval_check.ipynb：测试模型在多个指标上的表现；
- anno_process.ipynb：用于处理annotations各种函数；
- data_process.ipynb：用于处理数据集的各种函数。

## Performance

不同类别和不同边框大小下的accuracy和recall：

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxsrcbl3wj20zh0jswh2.jpg)

不同检测框范围下的 acc-recall 曲线：

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxss06k1rj20jr0jg0w4.jpg)

ground truth 和预测的检测框大小分布直方图：

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxssk1j40j20fe068dg4.jpg)

## Demo

 CVTS-TT100K的部分检测结果示例：

![](https://ws1.sinaimg.cn/large/a92fa7d4gy1fyxsteh2juj20fe0fe49k.jpg)

## References

- Zhu, Zhe, et al. "Traffic-sign detection and classification in the wild." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2016.
- Li, Yuming, et al. "TAD16K: An enhanced benchmark for autonomous driving." Image Processing (ICIP), 2017 IEEE International Conference on. IEEE, 2017.
- Lin, Tsung-Yi, et al. "Focal loss for dense object detection." *IEEE transactions on pattern analysis and machine intelligence* (2018).
- Lin, Tsung-Yi, et al. "Feature Pyramid Networks for Object Detection." CVPR. Vol. 1. No. 2. 2017.
- Long, Jonathan, Evan Shelhamer, and Trevor Darrell. "Fully convolutional networks for semantic segmentation." Proceedings of the IEEE conference on computer vision and pattern recognition. 2015. 