class HashTable:
    def __init__(self):
        self.table = {}  # Initializes an empty dictionary to represent the hash table

    def set_password(self, username, password):
        self.table[username] = password  # Stores the username as the key and password as the value

    def get_password(self, username):
        return self.table.get(username, None)  # Retrieves the password for the given username; returns None if not found

    def remove_user(self, username):
        if username in self.table:
            del self.table[username]  # Removes the username and its password from the hash table

# Demonstration
hash_table = HashTable()
hash_table.set_password("user1", "pass1234")
hash_table.set_password("user2", "abcd1234")

print("Password for user1:", hash_table.get_password("user1"))  # Should print pass1234
print("Password for user2:", hash_table.get_password("user2"))  # Should print abcd1234

hash_table.remove_user("user1")
print("Password for user1 after removal:", hash_table.get_password("user1"))  # Should print None
