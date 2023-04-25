import unittest

from src.jenkins_tasks import DevOpsJenkins


class TestJenkins(unittest.TestCase):

    def test_build(self):
        # Given
        task = DevOpsJenkins()
        task.input_properties = {
                'url': 'http://localhost:8080',
                'username': 'admin',
                'password': 'admin'
        }

        # When
        task.execute_task()

        # Then
        self.assertEqual(task.get_output_properties()['response'], 'SUCCESS')


if __name__ == '__main__':
    unittest.main()
