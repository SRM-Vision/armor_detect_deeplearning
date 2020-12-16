import os

# 需要改变的图像文件的路径，我放于桌面了
path ='images'
# 改变后存放图片的文件夹路径，我也放于桌面了
path1 = '1'
filelist = os.listdir(path)

xmllist = os.listdir('labels_voc')
j=0
n=0
for i in filelist:
    # 判断该路径下的文件是否为图片
    if i.endswith('.jpg'):#png可以改为jpg
        # 打开图片
        src = os.path.join("images",i)
        # 重命名
        dst = os.path.join("images",format(str(j), '0>s')+ '.jpg')#0>s的意思是 图片的名称没有0，例如1_label.png，
                                                                                             #   如果改为0>3s，则结果为001_label.png
        # 执行操作
        os.rename(src, dst)
    x=i.replace('.jpg','.xml')
    if x.endswith('.xml'):
        src = os.path.join("labels_voc",x)
        dst = os.path.join("labels_voc", format(str(j), '0>s') + '.xml')
        os.rename(src, dst)
    j=j+1
    n=n+1