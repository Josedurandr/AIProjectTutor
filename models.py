from mongoengine import Document, fields

class Grammar(Document):
    rule = fields.StringField()
    explanation = fields.StringField()
    examples = fields.ListField(fields.StringField())

class Vocabulary(Document):
    word = fields.StringField()
    translation = fields.StringField()

class Text(Document):
    text = fields.StringField()
    language = fields.StringField()
    category = fields.IntField()

class Users(Document):
    name = fields.StringField()
    email = fields.EmailField()
    preferred_languages = fields.ListField(fields.StringField())
    skill_level = fields.DictField()
    experience_level = fields.DictField()
