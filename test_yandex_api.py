from unittest import TestCase
from yandex_API import YaUploader


class TestYaApi(TestCase):

    def test_1_create_folder(self):
        token = ''
        yauploader = YaUploader(token)
        response = yauploader.create_folder('Test_test')
        self.assertIn(response.status_code, (201, 409))

    def test_2_create_folder(self):
        token = ''
        yauploader = YaUploader(token)
        self.assertIn('Test_test', yauploader.get_dir_inform())

    def test_3_create_folder(self):
        yauploader = YaUploader('non_correct_token')
        response = yauploader.create_folder('Test_test_2')
        self.assertEqual(response.status_code, 401)
