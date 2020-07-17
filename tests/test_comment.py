import unittest
from app.models import Comment

def setUp(self):
    self.new_comment = Comment(id=2, pitch_id=100, pitch_comment='Test Comment', user_id=11)
    
def tearDown(self):
    Comment.query.delete()

def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.id, 2)
    self.assertEquals(self.new_comment.pitch_id=100)
    self.assertEquals(self.new_comment.pitch_comment, 'Test comment')
    self.assertEquals(self.new_comment.user_id, 11)

def test_comment_save(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all()) > 0)

def test_get_comment_by_id(self):
    self.new_comment.save_comment()
    got_comments = Comment.get_comments(2)