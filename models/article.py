import os

from models.active_record_entity import ActiveRecordEntity
from models.user import User
from exceptions import InvalidArgumentException

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 МБ

class Article(ActiveRecordEntity):
    # __tablename__ = 'articles'
    _author_id = None
    _name = None
    _text = None
    _create_at = None
    _img = None

    def get_author_id(self):
        return self._author_id

    def get_name(self):
        return self._name

    def get_text(self):
        return self._text

    def get_img(self):
        return self._img

    def get_create_at(self):
        return self._create_at

    def get_author(self):
        return User.get_by_id(self._author_id)

    def set_author_id(self, author_id):
        self._author_id = author_id

    def set_name(self, name):
        self._name = name

    def set_text(self, text):
        self._text = text

    # def set_create_at(self, create_at):
    #     self._create_at = create_at

    @staticmethod
    def create(fields, img_file, author):
        article = Article()
        article.validate(fields, img_file)

        article._name = fields['name']
        article._text = fields['text']
        article._author_id = author.get_id()

        article.move_img_file(img_file)

        article.save()
        return article


    def updateFromArray(self, fields, img_file):

        self.validate(fields, img_file)


        self._name = fields['name']
        self._text = fields['text']
        self.move_img_file(img_file)

        self.save()
        return self

    @staticmethod
    def search_by_name(search_string):
        return __class__.search('name', search_string)

    def validate(self, fields, img_file):
        print(fields)
        if not fields['name']:
            raise InvalidArgumentException('не передано название статьи')

        if not fields['text']:
            raise InvalidArgumentException('не передан текст статьи')

        if __class__.check_file_size(img_file, MAX_FILE_SIZE)[0] == False :
            raise InvalidArgumentException('Слишком большой файл! Должно быть не более 5МБ')

    def move_img_file(self, img_file):
        if img_file.filename:
            file_path = '/uploads/' +  img_file.filename
            self._img = file_path
            file_path = 'assets' + file_path
            os.makedirs('assets/uploads', exist_ok=True)
            with open(file_path, 'wb') as f:
                while True:
                    chunk = img_file.file.read(8192)  # Читаем файл по частям
                    if not chunk:
                        break
                    f.write(chunk)

    @staticmethod
    def check_file_size(file_item, max_size):
        """
        Проверка размера файла без загрузки всего файла в память.
        Читает файл по частям и суммирует их размер.
        """
        total_size = 0
        chunk_size = 8192  # Читаем по 8KB

        # Сохраняем текущую позицию, чтобы потом вернуться
        current_pos = file_item.file.tell()

        try:
            # Перемещаемся в начало файла
            file_item.file.seek(0)

            # Читаем файл по частям и суммируем размер
            while True:
                chunk = file_item.file.read(chunk_size)
                if not chunk:
                    break
                total_size += len(chunk)

                # Если уже превысили лимит, можно прервать проверку
                if total_size > max_size:
                    break
        finally:
            # Возвращаемся на исходную позицию для последующего чтения
            file_item.file.seek(current_pos)
        print(total_size)
        return total_size <= max_size, total_size


    @staticmethod
    def get_table_name():
        return 'articles'