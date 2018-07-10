from urllib import request

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件