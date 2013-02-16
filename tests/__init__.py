from chompy   import chomp

from unittest import TestCase

newlines = ["\n", "\r\n", "\r"]

class Test_chomp(TestCase):
  def test_it_does_not_remove_newlines_from_the_middle_of_the_string(self):
    for n in newlines:
      input = n.join(["hello", "world"])
      self.assertEqual(chomp(input), input)


  def test_it_only_removes_the_last_newline(self):
    input = "hello\r\n\n"
    for n in newlines:
      self.assertEqual(chomp(input + n), input)



