#!/bin/bash
# 安装技能的打包脚本，默认拷贝启动文件，源码，模型目录和数据文件目录到temp临时目录，打包文件名为项目名称.zip，成功后会删除临时目录
# 用户可以自定义打包脚本，保留想要的文件夹或者文件
project_path=`pwd`
project_name="${project_path##*/}"
echo $project_name


if [ -d temp ]; then
    rm -rf temp
fi
mkdir temp

cp -r model temp
cp -r src temp
cp -r data temp
cp -r .hilens temp
cp start.py temp
cd temp


zip -0 -r $project_name.zip * .[^.]*