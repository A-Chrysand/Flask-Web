# 实际部署服务器请用deploy_server.py(仅适用tornado)或者autorun.bat(Nginx+tornado->flask)
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app  #这里要和run.py对应

print("Tornado Starting")
s = HTTPServer(WSGIContainer(app))
s.bind(5000, "0.0.0.0")  #监听5000端口，作为服务器这里配置成0.0.0.0，服务器就可以监听所有浏览器的访问了。
s.start(1)
IOLoop.instance().start()
