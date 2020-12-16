yolo v5环境搭建
===============
2020.12.7
系统：win10<br>
-----------------

### 一、安装anaconda（可装D盘)<br>
    https://www.anaconda.com/products/individual

### 二、打开Anaconda Prompt（在开始里，作用等效于cmd），设置conda为清华源<br>
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

### 三、创建虚拟环境<br>
建议每一个项目都创一个新的<br>
`conda create -n yolov5 python=3.7`
<br>  “yolov5”是环境名，可以自定义。python版本强烈建议3.7的，因此指定版本；如果不指定，默认安装3.8的。 
以后所有关于yolov5的操作都在这个环境里进行，打开Anaconda Prompt后进入环境的方法为：`activate yolov5 `

### 四、安装cuda和cudnn<br>
`conda install cudatoolkit==10.2.89`<br>
`conda install cudnn==7.6.5`<br>

### 五、安装各类库<br>
[官方环境要求](https://github.com/ultralytics/yolov5/blob/master/requirements.txt)<br>
    我的库版本：<br>
    numpy：1.19.2<br>
    opencv-python：4.4.0.46<br>
    Cython：0.29.21<br>
    pillow：8.0.1<br>
    matplotlib：3.3.2<br>
    pyyaml：5.3.1<br>
    tensorboard：2.3.0<br>
    scipy：1.5.2<br>
    tqdm：4.54.0<br>
    pandas：1.1.3<br>
    seaborn：0.11.0<br>
一般先`conda install Cython`，看看版本是否符合要求，若默认版本不符合要求：<br>
##### 方法一：去[anaconda网站](https://anaconda.org/)上找相应版本的库，然后安装。<br>
    以opencv为例：https://anaconda.org/conda-forge/opencv
    `conda install -c conda-forge opencv`
##### 方法二：去清华源或库的官网上下载.tar.bz2的压缩包<br>
    在anaconda Prompt中，进入yolov5环境，cd到压缩包所在目录，输入：
    `conda install --offline XXX.tar.bz2`<br>
cv4.4：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python`<br>

### 六、安装pytorch和torchvision  **(两者版本也要匹配)** <br>
我用的是 **pytorch1.6.0** 和 **torchvision0.7.0** 。别的版本我也试过，强烈建议按照我的。<br>
注意:  ***pytorch和torchvision在安装完所有其它库后最后安装*** ！否则会报错。<br>

### 七、下载[yolov5源码](https://github.com/ultralytics/yolov5)<br>

### 八、下载[yolov5模型](https://github.com/ultralytics/yolov5/releases)（.pt文件），放到源码文件的./weights文件下<br>

### 九、运行<br>
图片：`python detect.py --source ./inference/images/ --weights ./weights/yolov5s.pt --conf 0.4`<br>
摄像头：`python detect.py --source 0 --weights ./weights/yolov5s.pt --conf 0.4`<br>
自己的模型：`python detect.py --source 0 --weights ./路径 --conf 阈值`<br>
