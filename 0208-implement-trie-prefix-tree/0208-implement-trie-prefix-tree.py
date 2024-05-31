class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        current=self.root
        for character in word:
            if character not in current:
                current[character]={}
            current=current[character]
        current["IsEnd"]=True      
                

    def search(self, word: str) -> bool:
         current=self.root
         for character in word:
            if character not in current:
                return False
            current=current[character]
         if "IsEnd" in current:
            return True
         return False           
                

    def startsWith(self, prefix: str) -> bool:
         current=self.root
         for character in prefix:
            if character not in current:
                return False
            current=current[character]

         return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
   