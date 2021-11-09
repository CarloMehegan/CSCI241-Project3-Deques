import unittest
from Deque_Generator import get_deque

class Linked_Lest_Tester(unittest.TestCase):

  def setUp(self):
    self.__dq = get_deque(0)
    self.__lldq = get_deque(0)
    self.__adq = get_deque(1)


  # def test_stringify_LL_DSQ(self):
  #   print(str(self.__lldq))
  #   self.assertEqual('[ ]', str(self.__lldq), 'Empty LLdq should print as "[ ]"')
  
  # def test_push_front_to_LL_DSQ(self):
  #   self.__lldq.push_front(0)

  # def test_push_front_multiple_to_LL_DSQ(self):
  #   self.__lldq.push_front(0)
  #   self.__lldq.push_front(1)
  #   self.__lldq.push_front(2)
  #   self.__lldq.push_front(3)

  # def test_push_front_and_pop_front_from_LL_DSQ(self):
  #   self.__lldq.push_front(0)
  #   self.__lldq.pop_front()

  # def test_push_front_and_pop_front_multiple_from_LL_DSQ(self):
  #   self.__lldq.push_front(0)
  #   self.__lldq.push_front(1)
  #   self.__lldq.push_front(2)
  #   self.__lldq.push_front(3)
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()

  # def test_push_front_and_pop_front_then_push_front_again_LL_DSQ(self):
  #   self.__lldq.push_front(0)
  #   self.__lldq.push_front(1)
  #   self.__lldq.push_front(2)
  #   self.__lldq.push_front(3)
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()
  #   self.__lldq.pop_front()
  #   self.__lldq.push_front(0)
  #   self.__lldq.push_front(1)
  #   self.__lldq.push_front(2)
  #   self.__lldq.push_front(3)


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

  def test_add_middle_with_two(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual('[ Data, Structures, Rocks ]', str(self.__string_list))

  def test_add_second_of_four(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('and')
    # self.__string_list.append_element('Algorithms')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual('[ Data, Structures, and, Algorithms ]', str(self.__string_list))

  def test_add_third_of_four(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Algorithms')
    # self.__string_list.insert_element_at('and', 2)
    # # self.assertEqual('[ Data, Structures, and, Algorithms ]', str(self.__string_list))
  
  def test_get_empty_length(self):
    # # self.assertEqual(0, len(self.__string_list))
    self.assertEqual(0, len(self.__dq))

  def test_get_one_length_push_front(self):
    pass
    # self.__string_list.append_element('Victory')
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_front(0)
    self.assertEqual(1, len(self.__dq))

  def test_get_one_length_push_back(self):
    pass
    # self.__string_list.append_element('Victory')
    # # self.assertEqual(1, len(self.__string_list))
    self.__dq.push_back(0)
    self.assertEqual(1, len(self.__dq))

  def test_get_two_length_push_front(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.assertEqual(2, len(self.__dq))

  def test_get_two_length_push_back(self):
    pass
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at('Data', 0)
    # # self.assertEqual(2, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.assertEqual(2, len(self.__dq))

  def test_get_three_length_push_front(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_front(0)
    self.__dq.push_front(1)
    self.__dq.push_front(2)
    self.assertEqual(3, len(self.__dq))

  def test_get_three_length_push_back(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual(3, len(self.__string_list))
    self.__dq.push_back(0)
    self.__dq.push_back(1)
    self.__dq.push_back(2)
    self.assertEqual(3, len(self.__dq))

  def test_remove_head_leaving_zero_returned_value(self):
    pass
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Victory', returned)

  def test_remove_head_leaving_zero_remaining_list(self):
    pass
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_remove_head_leaving_zero_length(self):
    pass
    # self.__string_list.append_element('Victory')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(0, len(self.__string_list))

  def test_remove_head_leaving_one_returned_value(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # returned = self.__string_list.remove_element_at(0)
    # self.assertEqual('Data', returned)

  def test_remove_head_leaving_one_remaining_list(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual('[ Structures ]', str(self.__string_list))

  def test_removeHeadLeavingOneLength(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.remove_element_at(0)
    # # self.assertEqual(1, len(self.__string_list))

  def test_remove_tail_leaving_one_returned_value(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # returned = self.__string_list.remove_element_at(1)
    # self.assertEqual('Structures', returned)

  def test_remove_tail_leaving_one_remaining_list(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.remove_element_at(1)
    # # self.assertEqual('[ Data ]', str(self.__string_list))

  def test_remove_tail_leaving_one_length(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.remove_element_at(1)
    # # self.assertEqual(1, len(self.__string_list))

  def test_remove_middle_leaving_two_returned_value(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # returned = self.__string_list.remove_element_at(1)
    # self.assertEqual('Structures', returned)

  def test_remove_middle_leaving_two_remaining_list(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.remove_element_at(1)
    # # self.assertEqual('[ Data, Rocks ]', str(self.__string_list))

  def test_remove_middle_leaving_two_length(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.remove_element_at(1)
    # # self.assertEqual(2, len(self.__string_list))
  
  def test_get_head_with_one_element(self):
    pass
    # self.__string_list.append_element('Victory')
    # returned = self.__string_list.get_element_at(0)
    # self.assertEqual('Victory', returned)

  def test_get_head_with_one_element_remaining(self):
    pass
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual('[ Victory ]', str(self.__string_list))

  def test_get_head_with_one_element_length(self):
    pass
    # self.__string_list.append_element('Victory')
    # self.__string_list.get_element_at(0)
    # # self.assertEqual(1, len(self.__string_list))

  def test_get_tail_with_two_elements(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # returned = self.__string_list.get_element_at(1)
    # self.assertEqual('Structures', returned)

  def test_get_tail_with_two_elements_remaining(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual('[ Data, Structures ]', str(self.__string_list))

  def test_get_tail_with_two_elements_length(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual(2, len(self.__string_list))

  def test_get_middle_with_three_elements(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # returned = self.__string_list.get_element_at(1)
    # self.assertEqual('Structures', returned)

  def test_get_middle_with_three_elements_remaining(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual('[ Data, Structures, Rocks ]', str(self.__string_list))

  def test_get_middle_with_three_elements_length(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # self.__string_list.get_element_at(1)
    # # self.assertEqual(3, len(self.__string_list))

  def test_add_at_negative_index_ignore(self):
    pass
    # with self.assertRaises(IndexError):
      # self.__string_list.insert_element_at('Victory', -1)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_remove_at_negative_index_ignore(self):
    pass 
    # with self.assertRaises(IndexError):
      # self.__string_list.remove_element_at(-1)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_get_at_negative_index_ignore(self):
    pass 
    # with self.assertRaises(IndexError):
      # self.__string_list.get_element_at(-1)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_add_at_zero_index_empty_ignore(self):
    pass 
    # with self.assertRaises(IndexError):
      # self.__string_list.insert_element_at('Victory', 0)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_remove_at_zero_index_empty_ignore(self):
    pass 
    # with self.assertRaises(IndexError):
      # self.__string_list.remove_element_at(0)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_get_at_zero_index_empty_ignore(self):
    pass 
    # with self.assertRaises(IndexError):
      # self.__string_list.get_element_at(0)
    # # self.assertEqual('[ ]', str(self.__string_list))

  def test_add_at_one_past_index_ignore(self):
    pass 
    # self.__string_list.append_element('Data')
    # with self.assertRaises(IndexError):
      # self.__string_list.insert_element_at('Structures', 1)
    # # self.assertEqual('[ Data ]', str(self.__string_list))

  def test_remove_at_one_past_index_ignore(self):
    pass 
    # self.__string_list.append_element('Data')
    # with self.assertRaises(IndexError):
      # self.__string_list.remove_element_at(1)
    # # self.assertEqual('[ Data ]', str(self.__string_list))

  def test_get_at_one_past_index_ignore(self):
    pass 
    # self.__string_list.append_element('Data')
    # with self.assertRaises(IndexError):
      # self.__string_list.get_element_at(1)
    # # self.assertEqual('[ Data ]', str(self.__string_list))
  
  def test_empty_iterator(self):
    pass
    # for _ in self.__string_list:
      # self.fail()
  
  def test_one_iterator(self):
    pass
    # self.__string_list.append_element('Data')
    # count = 0
    # for value in self.__string_list:
      # self.assertEqual('Data', value)
      # count = count + 1
    # self.assertEqual(1, count)
  
  def test_multiple_iterator(self):
    pass
    # strs = ['Data', 'Structures', 'Rocks']
    # self.__string_list.append_element(strs[0])
    # self.__string_list.append_element(strs[1])
    # self.__string_list.append_element(strs[2])
    # count = 0
    # for value in self.__string_list:
      # self.assertEqual(strs[count], value)
      # count = count + 1
    # self.assertEqual(3, count)
    
  def test_rotate_left_empty(self):
    pass
    # self.__string_list.rotate_left()
    # # self.assertEqual('[ ]', str(self.__string_list))
  
  def test_rotate_left_with_one(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.rotate_left()
    # # self.assertEqual('[ Data ]', str(self.__string_list))
  
  def test_rotate_left_with_two(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.rotate_left()
    # # self.assertEqual('[ Structures, Data ]', str(self.__string_list))  
  
  def test_rotate_left_with_three(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')    
    # self.__string_list.rotate_left()
    # # self.assertEqual('[ Structures, Rocks, Data ]', str(self.__string_list))

  def test_reversed_empty_str(self):
    pass
    # ll = reversed(self.__string_list)
    # # self.assertEqual('[ ]', str(self.__string_list))
    # self.assertEqual('[ ]', str(ll))
  
  def test_reversed_empty_len(self):
    pass
    # ll = reversed(self.__string_list)
    # # self.assertEqual(0,len(self.__string_list))
    # self.assertEqual(0,len(ll))

  def test_reversed_one_str(self):
    pass
    # self.__string_list.append_element('Data')
    # ll = reversed(self.__string_list)
    # # self.assertEqual('[ Data ]', str(self.__string_list))
    # self.assertEqual('[ Data ]', str(ll))
  
  def test_reversed_one_len(self):
    pass
    # self.__string_list.append_element('Data')
    # ll = reversed(self.__string_list)
    # # self.assertEqual(1,len(self.__string_list))
    # self.assertEqual(1,len(ll))

  def test_reversed_two_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # ll = reversed(self.__string_list)
    # # self.assertEqual('[ Data, Structures ]', str(self.__string_list))
    # self.assertEqual('[ Structures, Data ]', str(ll))
  
  def test_reversed_two_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # ll = reversed(self.__string_list)
    # # self.assertEqual(2,len(self.__string_list))
    # self.assertEqual(2,len(ll))

  def test_reversed_three_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # ll = reversed(self.__string_list)
    # # self.assertEqual('[ Data, Structures, Rocks ]', str(self.__string_list))
    # self.assertEqual('[ Rocks, Structures, Data ]', str(ll))
  
  def test_reversed_three_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element('Rocks')
    # ll = reversed(self.__string_list)
    # # self.assertEqual(3, len(self.__string_list))
    # self.assertEqual(3, len(ll))
  
  def test_one_None_str(self):
    pass
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ None ]', str(self.__string_list))
  
  def test_one_None_len(self):
    pass
    # self.__string_list.append_element(None)
    # # self.assertEqual(1, len(self.__string_list))

  def test_five_None_str(self):
    pass
    # for _ in range(5):
      # self.__string_list.append_element(None)
    # # self.assertEqual('[ None, None, None, None, None ]', str(self.__string_list))
  
  def test_five_None_len(self):
    pass
    # for _ in range(5):
      # self.__string_list.append_element(None)
    # # self.assertEqual(5, len(self.__string_list))

  def test_two_end_None_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ Data, None ]', str(self.__string_list))
  
  def test_two_end_None_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element(None)
    # # self.assertEqual(2, len(self.__string_list))
  
  def test_three_insert_None_head_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,0)
    # # self.assertEqual('[ None, Data, Structures ]', str(self.__string_list))
  
  def test_three_insert_None_head_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,0)
    # # self.assertEqual(3, len(self.__string_list))
  
  def test_three_insert_None_middle_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,1)
    # # self.assertEqual('[ Data, None, Structures ]', str(self.__string_list))
  
  def test_three_insert_None_middle_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.insert_element_at(None,1)
    # # self.assertEqual(3, len(self.__string_list))
  
  def test_three_append_None_str(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element(None)
    # # self.assertEqual('[ Data, Structures, None ]', str(self.__string_list))
  
  def test_three_append_None_len(self):
    pass
    # self.__string_list.append_element('Data')
    # self.__string_list.append_element('Structures')
    # self.__string_list.append_element(None)
    # # self.assertEqual(3, len(self.__string_list))
  
  

if __name__ == '__main__':
  unittest.main()
