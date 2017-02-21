from django.db import models


class Author(models.Model):
    username = models.CharField('Ник', max_length=30)
    firstname = models.CharField('Имя', max_length=30, blank=True)
    lastname = models.CharField('Фамилия', max_length=30, blank=True)

    def get_full_name(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

    def __str__(self):
        if self.firstname and self.lastname:
            return '{0} ({1})'.format(self.username, self.get_full_name())
        return '{0}'.format(self.username)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    thumb = models.ImageField('Эскиз', upload_to='articles', blank=True, null=True)
    body = models.TextField('Содержимое')
    author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
