import camel_case

from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        
        self.assertEqual('helloWorld' , camel_case.camelcase('Hello World'))
    def test_space_sentence(self):
        self.assertEqual('',camel_case.camelcase(''))
    def test_emoji_sentence (self):
        self.assertEqual('😙' , camel_case.camelcase('😙 '))
    def test_whitespace_sentence(self):
        self.assertEqual('helloWorld', camel_case.camelcase('   Hello   World   '))
    def test_escape_char(self):
        self.assertEqual('helloWorld', camel_case.camelcase(' \n helloWorld'))