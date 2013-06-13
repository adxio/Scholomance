Django Handbook
===

一 开始
---
1. 下载<br/>[https://www.djangoproject.com/download/](https://www.djangoproject.com/download/)
2. 安装<br/>`python setup.py install`<br/>Django安装文档：[How to install Django](https://docs.djangoproject.com/en/1.5/topics/install/)
3. 查看Django版本<br/> `python -c "import django; print(django.get_version())"
`
4. 生成项目目录<br/>`django-admin.py startproject mysite`
5. 启动<br/>`python manage.py runserver`
6. 连接数据库<br/>`python manage.py syncdb`
7. 创建app<br/>`python manage.py startapp newapp`