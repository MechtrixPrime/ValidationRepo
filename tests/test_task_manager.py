import unittest
from task_bug import add_task, mark_task_completed, delete_task, binary_search

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        add_task(self.tasks, "Test Task")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0], ("Test Task", False))

    def test_mark_completed(self):
        add_task(self.tasks, "Task")
        mark_task_completed(self.tasks, 0)
        self.assertTrue(self.tasks[0][1])

    def test_delete_task(self):
        add_task(self.tasks, "Task")
        delete_task(self.tasks, 0)
        self.assertEqual(len(self.tasks), 0)

    def test_binary_search_found(self):
        add_task(self.tasks, "Alpha")
        add_task(self.tasks, "Beta")
        index = binary_search(self.tasks, "Alpha")
        self.assertNotEqual(index, -1)

    def test_binary_search_not_found(self):
        index = binary_search(self.tasks, "Missing")
        self.assertEqual(index, -1)

if __name__ == "__main__":
    unittest.main()