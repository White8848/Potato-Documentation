GPIO输入输出
~~~~~~~~~~~~~~~~~~

正如初学C语言时的 ``Hello World``，对应在单片机硬件中就是 ``点灯``。GPIO(General Purpose Input/Output)，指的就是一些引脚，具有输入和输出功能，对外输出高低电平或者检测输入的高低电平。高低电平就是1和0，在这里可以粗略对应于电压5V和0V


.. code-block:: c++
   :linenos:

    #define LED_GPIO 2
    void setup()
    {
      pinMode(LED_GPIO, OUTPUT);
    }
    
    void loop()
    {
      digitalWrite(LED_GPIO, HIGH);
      delay(1000);
      digitalWrite(LED_GPIO, LOW);
      delay(1000);
    }

这是一个简单的让灯闪烁的程序，我们定义了1个GPIO引脚， ``setup()`` 函数在单片机复位后只执行一次，之后单片机程序会在 ``loop()`` 中不断循环。开发板上将LED灯连接到了单片机的2号引脚，因此将其定义为2，然后在初始化中将该引脚配置成输出模式，在循环中不断输出高电平和低电平，就实现了灯的闪烁。

