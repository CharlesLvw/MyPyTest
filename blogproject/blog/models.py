from django.db import models
from django.contrib.auth.models import User

"""
    编写博客模型代码
    Django 把那一套数据库的语法转换成了 Python 的语法形式，我们只要写 Python 代码就可以了，Django 会把 Python 代码翻译成对应的数据库操作语言。
    用更加专业一点的说法，就是 Django 为我们提供了一套 ORM（Object Relational Mapping）系统。

"""


# 写一个分类数据库
class Category(models.Model):
    """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
        Django 内置的全部类型可查看文档：
        https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 定义标签数据库
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


# 定义文章数据库
class Article(models.Model):
    """
        CharFiled 要求必须存入数据, 但若指定了blank=True 参数后, 则允许空值
    """
    title = models.CharField(u"文章标题", max_length=100)    # 文章标题
    category = models.CharField(u"文章标签", max_length=50, blank=True)    # 文章标签
    created_time = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)    # 发布日期
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    content = models.TextField(blank=True, null=True)    # 文章正文, 因为正文比较大, 所以用TextField来存储

    """
        这是分类与标签，分类与标签的模型我们已经定义在上面。
        我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
        我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
        而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
        同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
        如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
        https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    """
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
