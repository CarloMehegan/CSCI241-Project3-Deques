import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue
from Hanoi import Hanoi

class DSQTester(unittest.TestCase):

  def setUp(self):
    self._deque = get_deque()
    self._stack = Stack()
    self._queue = Queue()

  # -- Empty Deque

  def test_d_popf_empty_return(self):
    result = self._deque.pop_front()
    self.assertIs(None, result)

  def test_d_popf_empty_len(self):
    self._deque.pop_front()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popf_empty_str(self):
    self._deque.pop_front()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_popb_empty_return(self):
    result = self._deque.pop_back()
    self.assertIs(None, result)

  def test_d_popb_empty_len(self):
    self._deque.pop_back()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popb_empty_str(self):
    self._deque.pop_back()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_peekf_empty_return(self):
    result = self._deque.peek_front()
    self.assertIs(None, result)

  def test_d_peekf_empty_len(self):
    self._deque.peek_front()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_peekf_empty_str(self):
    self._deque.peek_front()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_peekb_empty_return(self):
    result = self._deque.peek_back()
    self.assertIs(None, result)

  def test_d_peekb_empty_len(self):
    self._deque.peek_back()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_peekb_empty_str(self):
    self._deque.peek_back()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_empty_len(self):
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_empty_str(self):
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  # -- One Front Deque

  def test_d_popf_onef_return(self):
    self._deque.push_front(8)
    result = self._deque.pop_front()
    self.assertEqual(8, result)

  def test_d_popf_onef_len(self):
    self._deque.push_front(8)
    self._deque.pop_front()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popf_onef_str(self):
    self._deque.push_front(8)
    self._deque.pop_front()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_popb_onef_return(self):
    self._deque.push_front(8)
    result = self._deque.pop_back()
    self.assertEqual(8, result)

  def test_d_popb_onef_len(self):
    self._deque.push_front(8)
    self._deque.pop_back()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popb_onef_str(self):
    self._deque.push_front(8)
    self._deque.pop_back()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_peekf_onef_return(self):
    self._deque.push_front(8)
    result = self._deque.peek_front()
    self.assertEqual(8, result)

  def test_d_peekf_onef_len(self):
    self._deque.push_front(8)
    self._deque.peek_front()
    result = len(self._deque)
    self.assertEqual(1, result)

  def test_d_peekf_onef_str(self):
    self._deque.push_front(8)
    self._deque.peek_front()
    result = str(self._deque)
    self.assertEqual('[ 8 ]', result)

  def test_d_peekb_onef_return(self):
    self._deque.push_front(8)
    result = self._deque.peek_back()
    self.assertEqual(8, result)

  def test_d_onef_len(self):
    self._deque.push_front(8)
    result = len(self._deque)
    self.assertEqual(1, result)

  def test_d_onef_str(self):
    self._deque.push_front(8)
    result = str(self._deque)
    self.assertEqual('[ 8 ]', result)

  # -- One Back Deque

  def test_d_popf_oneb_return(self):
    self._deque.push_back(8)
    result = self._deque.pop_front()
    self.assertEqual(8, result)

  def test_d_popf_oneb_len(self):
    self._deque.push_back(8)
    self._deque.pop_front()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popf_oneb_str(self):
    self._deque.push_back(8)
    self._deque.pop_front()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_popb_oneb_return(self):
    self._deque.push_back(8)
    result = self._deque.pop_back()
    self.assertEqual(8, result)

  def test_d_popb_oneb_len(self):
    self._deque.push_back(8)
    self._deque.pop_back()
    result = len(self._deque)
    self.assertEqual(0, result)

  def test_d_popb_oneb_str(self):
    self._deque.push_back(8)
    self._deque.pop_back()
    result = str(self._deque)
    self.assertEqual('[ ]', result)

  def test_d_peekf_oneb_return(self):
    self._deque.push_back(8)
    result = self._deque.peek_front()
    self.assertEqual(8, result)

  def test_d_peekf_oneb_len(self):
    self._deque.push_back(8)
    self._deque.peek_front()
    result = len(self._deque)
    self.assertEqual(1, result)

  def test_d_peekf_oneb_str(self):
    self._deque.push_back(8)
    self._deque.peek_front()
    result = str(self._deque)
    self.assertEqual('[ 8 ]', result)

  def test_d_peekb_oneb_return(self):
    self._deque.push_back(8)
    result = self._deque.peek_back()
    self.assertEqual(8, result)

  def test_d_peekb_oneb_len(self):
    self._deque.push_back(8)
    self._deque.peek_back()
    result = len(self._deque)
    self.assertEqual(1, result)

  def test_d_peekb_oneb_str(self):
    self._deque.push_back(8)
    self._deque.peek_back()
    result = str(self._deque)
    self.assertEqual('[ 8 ]', result)

  def test_d_oneb_len(self):
    self._deque.push_back(8)
    result = len(self._deque)
    self.assertEqual(1, result)

  def test_d_oneb_str(self):
    self._deque.push_back(8)
    result = str(self._deque)
    self.assertEqual('[ 8 ]', result)

  # -- Two Front Front Deque

  def test_d_popf_twoff_return(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = self._deque.pop_front()
    self.assertEqual(-7, result)

  def test_d_popb_twoff_return(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = self._deque.pop_back()
    self.assertEqual(8, result)

  def test_d_peekf_twoff_return(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = self._deque.peek_front()
    self.assertEqual(-7, result)

  def test_d_peekb_twoff_return(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = self._deque.peek_back()
    self.assertEqual(8, result)

  def test_d_str_twoff(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = str(self._deque)
    self.assertEqual('[ -7, 8 ]', result)

  def test_d_len_twoff(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    result = len(self._deque)
    self.assertEqual(2, result)

  # -- Two Back Back Deque

  def test_d_popf_twobb_return(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = self._deque.pop_front()
    self.assertEqual(8, result)

  def test_d_popb_twobb_return(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = self._deque.pop_back()
    self.assertEqual(-7, result)

  def test_d_peekf_twobb_return(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = self._deque.peek_front()
    self.assertEqual(8, result)

  def test_d_peekb_twobb_return(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = self._deque.peek_back()
    self.assertEqual(-7, result)

  def test_d_str_twobb(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = str(self._deque)
    self.assertEqual('[ 8, -7 ]', result)

  def test_d_len_twobb(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    result = len(self._deque)
    self.assertEqual(2, result)

  # -- Two Front Back Deque

  def test_d_popf_twofb_return(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = self._deque.pop_front()
    self.assertEqual(8, result)

  def test_d_popb_twofb_return(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = self._deque.pop_back()
    self.assertEqual(-7, result)

  def test_d_peekf_twofb_return(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = self._deque.peek_front()
    self.assertEqual(8, result)

  def test_d_peekb_twofb_return(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = self._deque.peek_back()
    self.assertEqual(-7, result)

  def test_d_str_twofb(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = str(self._deque)
    self.assertEqual('[ 8, -7 ]', result)

  def test_d_len_twofb(self):
    self._deque.push_front(8)
    self._deque.push_back(-7)
    result = len(self._deque)
    self.assertEqual(2, result)

  # -- Two Back Front Deque

  def test_d_popf_twobf_return(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = self._deque.pop_front()
    self.assertEqual(-7, result)

  def test_d_popb_twobf_return(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = self._deque.pop_back()
    self.assertEqual(8, result)

  def test_d_peekf_twobf_return(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = self._deque.peek_front()
    self.assertEqual(-7, result)

  def test_d_peekb_twobf_return(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = self._deque.peek_back()
    self.assertEqual(8, result)

  def test_d_str_twobf(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = str(self._deque)
    self.assertEqual('[ -7, 8 ]', result)

  def test_d_len_twobf(self):
    self._deque.push_back(8)
    self._deque.push_front(-7)
    result = len(self._deque)
    self.assertEqual(2, result)
  
  # Add, empty, add
  
  def test_d_str_pushff_popff_pushf(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self._deque))
 
  def test_d_str_pushbb_popbb_pushb(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self._deque))

  def test_d_str_pushff_popff_pushb(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.push_back(1)
    self.assertEqual('[ 1 ]', str(self._deque))

  def test_d_str_pushbb_popbb_pushf(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self._deque))

  def test_d_str_pushbbbb_popbbbb_pushf(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    self._deque.push_back(6)
    self._deque.push_back(-5)
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self._deque))

  def test_d_str_pushffff_popffff_pushf(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    self._deque.push_front(6)
    self._deque.push_front(-5)
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.push_front(1)
    self.assertEqual('[ 1 ]', str(self._deque))

  def test_d_str_pushbbbb_popbbbb_pushff(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    self._deque.push_back(6)
    self._deque.push_back(-5)
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.push_front(1)
    self._deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self._deque))

  def test_d_str_pushffff_popffff_pushff(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    self._deque.push_front(6)
    self._deque.push_front(-5)
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.push_front(1)
    self._deque.push_front(2)
    self.assertEqual('[ 2, 1 ]', str(self._deque))

  def test_d_str_pushbbbb_popbbbb_pushbb(self):
    self._deque.push_back(8)
    self._deque.push_back(-7)
    self._deque.push_back(6)
    self._deque.push_back(-5)
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.pop_back()
    self._deque.push_back(1)
    self._deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self._deque))

  def test_d_str_pushffff_popffff_pushbb(self):
    self._deque.push_front(8)
    self._deque.push_front(-7)
    self._deque.push_front(6)
    self._deque.push_front(-5)
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.pop_front()
    self._deque.push_back(1)
    self._deque.push_back(2)
    self.assertEqual('[ 1, 2 ]', str(self._deque))


  # Empty Stack

  def test_s_pop_empty_return(self):
    result = self._stack.pop()
    self.assertIs(None, result)

  def test_s_pop_empty_len(self):
    self._stack.pop()
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_pop_empty_str(self):
    self._stack.pop()
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  def test_s_peek_empty_return(self):
    result = self._stack.peek()
    self.assertIs(None, result)

  def test_s_peek_empty_len(self):
    self._stack.peek()
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_peek_empty_str(self):
    self._stack.peek()
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  def test_s_empty_len(self):
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_empty_str(self):
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  # One Stack

  def test_s_pop_one_return(self):
    self._stack.push(8)
    result = self._stack.pop()
    self.assertEqual(8, result)

  def test_s_pop_one_len(self):
    self._stack.push(8)
    self._stack.pop()
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_pop_one_str(self):
    self._stack.push(8)
    self._stack.pop()
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  def test_s_peek_one_return(self):
    self._stack.push(8)
    result = self._stack.peek()
    self.assertEqual(8, result)

  def test_s_peek_one_len(self):
    self._stack.push(8)
    self._stack.peek()
    result = len(self._stack)
    self.assertEqual(1, result)

  def test_s_peek_one_str(self):
    self._stack.push(8)
    self._stack.peek()
    result = str(self._stack)
    self.assertEqual('[ 8 ]', result)

  def test_s_one_len(self):
    self._stack.push(8)
    result = len(self._stack)
    self.assertEqual(1, result)

  def test_s_one_str(self):
    self._stack.push(8)
    result = str(self._stack)
    self.assertEqual('[ 8 ]', result)

  # Two Stack

  def test_s_pop1_two_return(self):
    self._stack.push(8)
    self._stack.push(-7)
    result = self._stack.pop()
    self.assertEqual(-7, result)

  def test_s_pop1_two_len(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    result = len(self._stack)
    self.assertEqual(1, result)

  def test_s_pop1_two_str(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    result = str(self._stack)
    self.assertEqual('[ 8 ]', result)

  def test_s_pop2_two_return(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    result = self._stack.pop()
    self.assertEqual(8, result)

  def test_s_pop2_two_len(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    self._stack.pop()
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_pop2_two_str(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    self._stack.pop()
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  def test_s_pop3_two_return(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    self._stack.pop()
    result = self._stack.pop()
    self.assertIs(None, result)

  def test_s_pop3_two_len(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    self._stack.pop()
    self._stack.pop()
    result = len(self._stack)
    self.assertEqual(0, result)

  def test_s_pop3_two_str(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.pop()
    self._stack.pop()
    self._stack.pop()
    result = str(self._stack)
    self.assertEqual('[ ]', result)

  def test_s_peek_two_return(self):
    self._stack.push(8)
    self._stack.push(-7)
    result = self._stack.peek()
    self.assertEqual(-7, result)

  def test_s_peek_two_len(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.peek()
    result = len(self._stack)
    self.assertEqual(2, result)

  def test_s_peek_two_str(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.peek()
    result = str(self._stack)
    self.assertEqual('[ -7, 8 ]', result)

  def test_s_two_len(self):
    self._stack.push(8)
    self._stack.push(-7)
    result = len(self._stack)
    self.assertEqual(2, result)

  def test_s_two_str(self):
    self._stack.push(8)
    self._stack.push(-7)
    result = str(self._stack)
    self.assertEqual('[ -7, 8 ]', result)

  # -- Three Stack

  def test_s_three_return(self):
    self._stack.push(8)
    self._stack.push(-7)
    self._stack.push(112)
    self.assertEqual(112, self._stack.pop())
    self.assertEqual(-7, self._stack.pop())
    self.assertEqual(8, self._stack.pop())

  # Empty Queue

  def test_q_dequeue_empty_return(self):
    result = self._queue.dequeue()
    self.assertIs(None, result)

  def test_q_dequeue_empty_len(self):
    self._queue.dequeue()
    result = len(self._queue)
    self.assertEqual(0, result)

  def test_q_dequeue_empty_str(self):
    self._queue.dequeue()
    result = str(self._queue)
    self.assertEqual('[ ]', result)

  def test_q_empty_len(self):
    result = len(self._queue)
    self.assertEqual(0, result)

  def test_q_empty_str(self):
    result = str(self._queue)
    self.assertEqual('[ ]', result)

  # One Queue

  def test_q_dequeue_one_return(self):
    self._queue.enqueue(8)
    result = self._queue.dequeue()
    self.assertEqual(8, result)

  def test_q_dequeue_one_len(self):
    self._queue.enqueue(8)
    self._queue.dequeue()
    result = len(self._queue)
    self.assertEqual(0, result)

  def test_q_dequeue_one_str(self):
    self._queue.enqueue(8)
    self._queue.dequeue()
    result = str(self._queue)
    self.assertEqual('[ ]', result)

  def test_q_one_len(self):
    self._queue.enqueue(8)
    result = len(self._queue)
    self.assertEqual(1, result)

  def test_q_one_str(self):
    self._queue.enqueue(8)
    result = str(self._queue)
    self.assertEqual('[ 8 ]', result)

  # Two Queue

  def test_q_dequeue1_two_return(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    result = self._queue.dequeue()
    self.assertEqual(8, result)

  def test_q_dequeue1_two_len(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    result = len(self._queue)
    self.assertEqual(1, result)

  def test_q_dequeue1_two_str(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    result = str(self._queue)
    self.assertEqual('[ -7 ]', result)

  def test_q_dequeue2_two_return(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    result = self._queue.dequeue()
    self.assertEqual(-7, result)

  def test_q_dequeue2_two_len(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    self._queue.dequeue()
    result = len(self._queue)
    self.assertEqual(0, result)

  def test_q_dequeue2_two_str(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    self._queue.dequeue()
    result = str(self._queue)
    self.assertEqual('[ ]', result)

  def test_q_dequeue3_two_return(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    self._queue.dequeue()
    result = self._queue.dequeue()
    self.assertIs(None, result)

  def test_q_dequeue3_two_len(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    self._queue.dequeue()
    self._queue.dequeue()
    result = len(self._queue)
    self.assertEqual(0, result)

  def test_q_dequeue3_two_str(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.dequeue()
    self._queue.dequeue()
    self._queue.dequeue()
    result = str(self._queue)
    self.assertEqual('[ ]', result)

  def test_q_two_len(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    result = len(self._queue)
    self.assertEqual(2, result)

  def test_q_two_str(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    result = str(self._queue)
    self.assertEqual('[ 8, -7 ]', result)

  # -- Three Queue

  def test_q_three_return(self):
    self._queue.enqueue(8)
    self._queue.enqueue(-7)
    self._queue.enqueue(112)
    self.assertEqual(8, self._queue.dequeue())
    self.assertEqual(-7, self._queue.dequeue())
    self.assertEqual(112, self._queue.dequeue())

  def test_z_Hanoi(self):
    Hanoi(4)

if __name__ == '__main__':
  unittest.main()
