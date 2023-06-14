from django.test import TestCase

from .core.models.news import News

class NewsTestCase(TestCase):
    
    def setUp(self):
        News.objects.create(
            title="O FábricaNews está o ar!"
        )

    def test_return_title_true_str(self):
        true = News.objects.get(title="O FábricaNews está o ar!")
        self.assertEquals(true.__str__(), "O FábricaNews está o ar!")