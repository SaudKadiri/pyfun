class Node:
  def __init__(self, val=0, left=None, right=None):
        """Initializes the vals and nxt"""
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        """For user-friendly output"""
        return 'Node({})'.format(self.val)
    
