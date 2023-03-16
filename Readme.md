# CV-Change

项目主要目的是复现[VITON-HD](https://github.com/shadow2496/VITON-HD)的时候，记录获取输入VITON-HD数据的工具。

复现流程思路来源：[An-implementation-of-preprocess-in-VITON-HD](https://github.com/Charlie839242/An-implementation-of-preprocess-in-VITON-HD-)。

项目提供了在Google Colab上的获取数据的代码：

1. ClothSegm_u2net.ipynb
  - 衣服分割
2. Self-Correction-Human-Parsing.ipynb
  - 人体分割
3. openpose.ipynb
  - 姿态检测
4. VITON-HD.ipynb
  - 换装

1-3步为获取输入数据阶段，第四步前请先将VITON-HD代码克隆到本地环境在执行。

utils包中有图片修正的辅助工具。
