# **ESP开发之入门**  
![ESP32](media1\ESP.jpg)  
## ESP32的开发，有几种开发方式:  
* Arduino方式开发，得益于简单易上手的体验，Arduino无疑成为最成功的开源硬件平台之一，结合众多的开源库，可玩性非常非常高；
* Espressif IDF，这是乐鑫官方的原生开发方式，设置工具链，自己安装CMake Ninja编译构建工具，获取ESP-IDF软件开发框架，运行工具链脚本，Windows,Linux,macOS下均可以开发，新手配置略显复杂，但代码效率最高；
* 在VSCode下添加ESP-IDF插件，跟第二种一样，但可以一键配置好环境，编译工具什么的都会自动安装好，体验还是不错的，产品级别的ESP32推荐此方式开发；
* microPython方式开发，类似Arduino的开发方式，大部分语法都能跟Python兼容；
* AT命令开发方式。  
  
   我们选择用Arduino的方式开发,Arduino core for the ESP32是乐鑫官方主导开发维护的，Arduino有很多很多优秀的库，非常方便我们做一些小制作。  

  接下来让我们进入正式的开发吧！
  ## <table><tr><td bgcolor=DarkTurquoise> 1、ESP32介绍 </td></tr></table>  
  > ESP32 芯片是由乐鑫公司继 ESP8266 芯片后推出的又一款集成 WiFi/BLE 功能的微控制器。性能比 ESP8266 更加强大，ESP32 芯片或模组具有下列特点: 

  ![](media1\ESP1.jpg)
   功能框图： 
  ![](media1\ESP2.jpg)  
  引脚图:  
  初期开发我们用ESP32-DevKit开发板  
  ![](media1\ESP3.jpg)  
## <table><tr><td bgcolor=DarkTurquoise> 2、开发环境搭建 </td></tr></table>  
 * Arduino软件安装,下载Arduino IDE并安装，当然也可以用其它编辑器，VSCode + PlatformIO IDE插件等方式，这个后续介绍。<https://www.arduino.cc/en/software>  
 * Arduino IDE中添加对应开发板，在文件->首选项->附加开发板管理网址中，添加ESP32的管理网址：<https://dl.espressif.com/dl/package_esp32_index.json>  
    ![](media\ESP4.jpg)  
* 添加开发板，在工具->开发板->开发板管理中，搜索esp32，如下图所示，安装Arduino core for esp32，过程可能比较慢，也可能需要科学上网才能安装好。  
![](media1\ESP5.jpg)  
* 然后选择中对应的开发板，我们可以看到这里有很多不同的ESP32开发板，这里选择ESP32 Dev Module就可以了。  
![](media1\ESP6.jpg) 
## <table><tr><td bgcolor=DarkTurquoise> 3、程序测试 </td></tr></table>  
``` 
void setup()
{
  Serial.begin(115200);
  Serial.println("");
}
void loop()
{
  Serial.println("Hello World!");
  Serial.println("This is my first esp32 code!");
  delay(1000);
} 
```
 默认已经引用了ESP32的头文件，通过```Serial.begin(115200);```初始化串口波特率之后，就可以通过```Serial.println();```打印输出了。  
 选中对应串口并点击```编译下载```  
![](media1\ESP7.jpg)  
通过串口观察实际效果  
![](media1\ESP8.jpg)   

今天我们先介绍到这里,后面我们会一一介绍ESP32的外设,敬请期待!