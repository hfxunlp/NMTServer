# NMTServer
An online NMT Server for OpenNMT

You may need to change your translation server at https://github.com/anoidgit/NMTServer/blob/master/translate.py#L20 and reconfig your service port in ini file if you use uwsgi.

After all the configs were done, you could start your server with:
uwsgi --ini huwsgi.ini
or
uwsgi --ini huwsgipy.ini
if you use pypy rather than python.

This is working for Chinese-English Translation, so there are some segmentation jobs in translate.py, you may need to change the translate.py to fit your use, I think it will be simple.

You could try the baseline model and get a sample view at http://ano.f3322.net:8888/, but It runs on my PC which was used to train the models at the same time, I can not make sure the server is available at any time. You could try put this("欢迎") in the top textbox and click the only button, if you are not familiar with Chinese.
