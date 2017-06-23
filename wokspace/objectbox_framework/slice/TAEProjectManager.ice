#pragma once

#include <OBBase.ice>

module tae
{
    module projectmanager
    {
        interface TaeProject extends objectbox::base::OBContainer
        {
            //存储所有的全局变量
            objectbox::base::OBContainer* getGlobalVariableBox();

            //还应该有一个地方用来选择默认的设备，hil，ees，vdt...
            //选择默认设备后，对应设备的路径信息会自动显示出来，
            //或者不同类型的路径信息一直显示，可以选择设备对象，来加载路径信息
            //供map模块，seqx模块使用
            //选择默认设备后，对应设备的简单方法会自动显示出来，
            //供seqx模块使用

            //集中管理数据字典map，当路径拖拽到seqx时，自动在map中添加数据字典
            //map支持复制，新建等操作

            //TestCase模块，支持package管理，支持seq，seqx，py方式搭建测试序列
            //支持调用其他seq文件，testplan文件
            //testplan模块，支持组织seq文件

            //测试报告模块，灵活强大，好用，（客户实际很需要这个功能）

            //后处理模块，数据已经保存下来了，可以各种处理

            //in the future
            //layout模块，有不同的控件，可以加载不同数据字典，做监测控制
            //诊断，等等操作
        };
    };
};