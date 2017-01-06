"""
@author: sourabh garg
"""
import words_tagging
from Tokenize import *
 

class Node( object ):
	def __init__( self, end_node = False ):
		self.end_node = end_node
		self.prefix_count = 0
		self.children = {}
	
class Trie( object ):
	def __init__( self ):
		self.root = Node()
	
	def insert( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				current.children[k] = Node()
			current = current.children[k]
			current.prefix_count += 1
		current.end_node = True
	
	def exist( self, key ):
		current = self.root
		
		for k in key:
			if k not in current.children:
				return False
			current = current.children[k]
		return current.end_node
	
	def count( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				return 0
			current = current.children[k]
		return current.prefix_count

	def _walk( self, root, prefix ):
		out = []
		if root.end_node:
			out.append( prefix )
		
		for ch in root.children:
			if isinstance( prefix, tuple ):
				tmp = self._walk( root.children[ch], prefix + (ch,) )
			elif isinstance( prefix, list ):
				tmp = self._walk( root.children[ch], prefix + [ch] )
			else:
				tmp = self._walk( root.children[ch], prefix + ch )
			out.extend( tmp )
		return out

	def find( self, key ):
		current = self.root
		for k in key:
			if k not in current.children:
				return []
			current = current.children[k]
		
		return self._walk( current, key )
  
if __name__ == '__main__':
    mytrie=Trie()
    for stem_cls in words_tagging.all_noun:
        for word in stem_cls:
#            print(word)
#            print(complete_tokenize(word))
            mytrie.insert(complete_tokenize(word))
    
    print(mytrie.exist(['र्', 'आ', 'म्', 'अ']))
    print(mytrie.count(['र्']))
    print (mytrie.find( ['र्']))