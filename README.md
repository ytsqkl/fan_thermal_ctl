[# fan_thermal_ctl ]
mmdvm温控  

此文档介绍把温控功能加到原有树莓派系统里，不用重新刷镜像文件的方法：pi-star-4.2.3
1.克隆程序文件  
方法一（速度快）：  
rpi-rw;   
sudo git clone https://gitee.com/ytqkl/fan_thermal_ctl.git;    
cd fan_thermal_ctl    
方法二：  
rpi-rw;   
sudo git clone https://github.com/ytsqkl/fan_thermal_ctl.git;  
cd fan_thermal_ctl    
2. 移动文件到指定位置     
sudo mv fan_thermal_ctl.py /boot/;  
sudo mv fan.service /etc/systemd/system/;  
sudo mv fan_on.py /home/mmdvm;  
sudo mv fan_off.py /home/mmdvm  
3. 输入以下命令以确认风扇及MOS管接线正确：（根据python版本可以为python(3) fan_on.py ）     
python3 fan_on.py回车  
这时风扇应该转起来的  
然后输入：  
python3 fan_off.py回车  
这时风扇应该转停掉  
如果这两命运行后风扇状态不对，请检查风扇的接线，MOS管的焊接  
4. 经上一步确认风扇正常后，输入以下命令，以让风扇管理程序能开机运行      
sudo systemctl enable fan;  
sudo systemctl start fan;  
sudo systemctl status fan  
5. 恭喜温控风扇功能已经安装上去了，重新开机就能启动温控风扇功能了      
6. 风扇的开启及关闭温度，是在fan_thermal_ct.py里面有定义的，您可以通过修改这个文件的对应值来调整到需要的温度。 注意开启温度要比关闭温度大。

