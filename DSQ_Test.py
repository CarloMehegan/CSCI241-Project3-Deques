import unittest
from Deque_Generator import get_deque

class Linked_Lest_Tester(unittest.TestCase):

  def setUp(self):
    self.__dq = get_deque(0)

  def test_empty_dq_string(self):
    # # self.assertEqual('[ ]', str(self.__string_list), 'Empty list should print as "[ ]"')
    print(str(self.__dq))
    self.assertEqual('[ ]', str(self.__dq), 'Empty LLdq should print as "[ ]"')

  def test_push_front_empty(self):
    self.__dq.push_front(0)
    self.assertEqual('[ 0 ]', str(self.__dq))

  def test_push_back_empty(self):
    # self.__string_list.append_element('Victory')
    # # self.assertEqual('[ Victory ]', str(self.__string_list))
    self.__dq.push_back(0)
    self.assertEqual('[ 0 ]', str(self.__dq))

  def test_push_front_with_one(self):
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at('Data', 0)
    # # self.assertEqual('[ Data, Structures ]', str(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.assertEqual('[ 1, 0 ]', str(self.__dq))

  def test_push_back_with_one(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # # self.assertEqual('[ Data, Structures ]', str(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.assertEqual('[ 0, 1 ]', str(self.__dq))

  def test_push_front_with_two(self):
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Data', 0)
    # # self.assertEqual('[ Data, Structures, Rocks ]', str(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.__dq.push_front(2)
    self.assertEqual('[ 2, 1, 0 ]', str(self.__dq))

  def test_push_back_with_two(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # # self.assertEqual('[ Data, Structures, Rocks ]', str(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.push_back(2)
    self.assertEqual('[ 0, 1, 2 ]', str(self.__dq))

  def test_get_empty_length(self):
    # # self.assertEqual(0, len(self.__string_list))
    self.assertEqual(0, len(self.__dq))

  def test_get_one_length_push_front(self):
    # self.__string_list.append_element('Victory')
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_front(0)
    self.assertEqual(1, len(self.__dq))

  def test_get_one_length_push_back(self):
    # self.__string_list.append_element('Victory')
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_back(0)
    self.assertEqual(1, len(self.__dq))

  def test_get_two_length_push_front(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.assertEqual(2, len(self.__dq))

  def test_get_two_length_push_back(self):
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at('Data', 0)
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.assertEqual(2, len(self.__dq))

  def test_get_three_length_push_front(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.__dq.push_front(2)
    self.assertEqual(3, len(self.__dq))

  def test_get_three_length_push_back(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.push_back(2)
    self.assertEqual(3, len(self.__dq))








  def test_push_pop_front_leaving_zero_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(1)
    returned = self.__dq.pop_front()
    self.assertEqual(1, returned)

  def test_push_pop_back_leaving_zero_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(1)
    returned = self.__dq.pop_back()
    self.assertEqual(1, returned)

  def test_push_back_pop_front_leaving_zero_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(1)
    returned = self.__dq.pop_front()
    self.assertEqual(1, returned)

  def test_push_front_pop_back_leaving_zero_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(1)
    returned = self.__dq.pop_back()
    self.assertEqual(1, returned)

  def test_push_pop_front_leaving_zero_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(1)
    returned = self.__dq.pop_front()
    self.assertEqual('[ ]', str(self.__dq))

  def test_push_pop_back_leaving_zero_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(1)
    returned = self.__dq.pop_back()
    self.assertEqual('[ ]', str(self.__dq))

  def test_push_back_pop_front_leaving_zero_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(1)
    returned = self.__dq.pop_front()
    self.assertEqual('[ ]', str(self.__dq))

  def test_push_front_pop_back_leaving_zero_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(1)
    returned = self.__dq.pop_back()
    self.assertEqual('[ ]', str(self.__dq))
  
  def test_push_pop_front_leaving_zero_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.pop_front()
    self.assertEqual(0, len(self.__dq))

  def test_push_pop_back_leaving_zero_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.pop_back()
    self.assertEqual(0, len(self.__dq))

  def test_push_back_pop_front_leaving_zero_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.pop_front()
    self.assertEqual(0, len(self.__dq))

  def test_push_front_pop_back_leaving_zero_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.pop_back()
    self.assertEqual(0, len(self.__dq))




  def test_push_pop_front_leaving_one_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    returned = self.__dq.pop_front()
    self.assertEqual(1, returned)

  def test_push_pop_back_leaving_one_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    returned = self.__dq.pop_back()
    self.assertEqual(1, returned)

  def test_push_back_pop_front_leaving_one_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    returned = self.__dq.pop_front()
    self.assertEqual(0, returned)

  def test_push_front_pop_back_leaving_one_returned_value(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    returned = self.__dq.pop_back()
    self.assertEqual(0, returned)

  def test_push_pop_front_leaving_one_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    returned = self.__dq.pop_front()
    self.assertEqual('[ 0 ]', str(self.__dq))

  def test_push_pop_back_leaving_one_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    returned = self.__dq.pop_back()
    self.assertEqual('[ 0 ]', str(self.__dq))

  def test_push_back_pop_front_leaving_one_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    returned = self.__dq.pop_front()
    self.assertEqual('[ 1 ]', str(self.__dq))

  def test_push_front_pop_back_leaving_one_remaining_list(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    returned = self.__dq.pop_back()
    self.assertEqual('[ 1 ]', str(self.__dq))

  def test_push_pop_front_leaving_one_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.__dq.pop_front()
    self.assertEqual(1, len(self.__dq))

  def test_push_pop_back_leaving_one_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.pop_back()
    self.assertEqual(1, len(self.__dq))

  def test_push_back_pop_front_leaving_one_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.pop_front()
    self.assertEqual(1, len(self.__dq))

  def test_push_front_pop_back_leaving_one_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.__dq.pop_back()
    self.assertEqual(1, len(self.__dq))








  def test_peek_front_with_one_element(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.get_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_front(1)
    returned = self.__dq.peek_front()
    self.assertEqual(1, returned)

  def test_peek_back_with_one_element(self):
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.get_element_at(0)
    # self.assertEqual('Victory', returned)
    self.__dq.push_back(1)
    returned = self.__dq.peek_back()
    self.assertEqual(1, returned)

  def test_peek_front_with_one_element_remaining(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual('[ Victory ]', str(self.__string_list))
    self.__dq.push_front(1)
    self.__dq.peek_front()
    self.assertEqual('[ 1 ]', str(self.__dq))

  def test_peek_back_with_one_element_remaining(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual('[ Victory ]', str(self.__string_list))
    self.__dq.push_back(1)
    self.__dq.peek_back()
    self.assertEqual('[ 1 ]', str(self.__dq))

  def test_peek_front_with_one_element_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_front(1)
    self.__dq.peek_front()
    self.assertEqual(1, len(self.__dq))

  def test_peek_back_with_one_element_length(self):
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_back(1)
    self.__dq.peek_back()
    self.assertEqual(1, len(self.__dq))

  def test_peek_back_with_two_elements(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # returned = self.__string_list.get_element_at(1)
    # self.assertEqual('Structures', returned)
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    returned = self.__dq.peek_back()
    self.assertEqual(1, returned)

  def test_peek_back_with_two_elements_remaining(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual('[ Data, Structures ]', str(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.peek_back()
    self.assertEqual('[ 0, 1 ]', str(self.__dq))

  def test_get_tail_with_two_elements_length(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.peek_back()
    self.assertEqual(2, len(self.__dq))








  def test_one_None_str(self):
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ None ]', str(self.__string_list))
    self.__dq.push_front(None)
    self.assertEqual('[ None ]', str(self.__dq))
  
  def test_one_None_len(self):
    # self.__string_list.append_element(None)
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_front(None)
    self.assertEqual(1, len(self.__dq))

  def test_five_None_str(self):
    # for _ in range(5):
      # self.__string_list.append_element(None)
    # # self.assertEqual('[ None, None, None, None, None ]', str(self.__string_list))
    for _ in range(5):
      self.__dq.push_front(None)
    self.assertEqual('[ None, None, None, None, None ]', str(self.__dq))
  
  def test_five_None_len(self):
    # for _ in range(5):
      # self.__string_list.append_element(None)
    # # self.assertEqual(5, len(self.__string_list))
    for _ in range(5):
      self.__dq.push_front(None)
    self.assertEqual(5, len(self.__dq))

  def test_two_end_None_str(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ Data, None ]', str(self.__string_list))
    self.__dq.push_front(None)
    self.__dq.push_front(0)
    self.assertEqual('[ 0, None ]', str(self.__dq))
  
  def test_two_end_None_len(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element(None)
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_front(None)
    self.__dq.push_front(0)
    self.assertEqual(2, len(self.__dq))
  
  def test_three_insert_None_head_str(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,0)
    # # self.assertEqual('[ None, Data, Structures ]', str(self.__string_list))
    self.__dq.push_front(1)
    self.__dq.push_front(0)
    self.__dq.push_front(None)
    self.assertEqual('[ None, 0, 1 ]', str(self.__dq))
  
  def test_three_insert_None_head_len(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,0)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_front(1)
    self.__dq.push_front(0)
    self.__dq.push_front(None)
    self.assertEqual(3, len(self.__dq))
  
  def test_three_append_None_str(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ Data, Structures, None ]', str(self.__string_list))
    self.__dq.push_front(None)
    self.__dq.push_front(1)
    self.__dq.push_front(0)
    self.assertEqual('[ 0, 1, None ]', str(self.__dq))
  
  def test_three_append_None_len(self):
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element(None)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_front(None)
    self.__dq.push_front(1)
    self.__dq.push_front(0)
    self.assertEqual(3, len(self.__dq))
  
  

if __name__ == '__main__':
  unittest.main()
