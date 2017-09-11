# NMTServer  
An online NMT Server for OpenNMT  
You may need to change your translation server address in [`translate.py`](https://github.com/anoidgit/NMTServer/blob/master/translate.py#L15) and reconfigure your service port in the `.ini` file if you use uwsgi.  
After all the configures were done, you could start your server with:  
`uwsgi --ini huwsgi.ini`.  
If you do not want to use `uwsgi`, you could just use `python userver.py` to start your server, which is ok with Windows, but you maybe need to change the server address and port in [`userver.py`](https://github.com/anoidgit/NMTServer/blob/master/userver.py#L24).  
This is working for Chinese-English Translation, so there are some tokenization jobs in `translate.py`, you may need to change the `translate.py` to fit your use, I think it will be simple.  
You could try the baseline model and get a sample view at http://ano.f3322.net:5678/, but It runs on my PC which was used to train the models at the same time, I can not make sure the server is available at any time. You could try to copy this("欢迎") in the top textbox and click the only button, if you are not familiar with Chinese. It looks like this:  
![STRUCTURE](<doc/images/welcome.png>)  
![STRUCTURE](<doc/images/example.png>)  
But this is a very ugly and rough work, you'd better try this(https://github.com/OpenNMT/Server) after their works done.  
