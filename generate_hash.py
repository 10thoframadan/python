import hashlib
def generate_hash(data, algorithm):
  hasher = hashlib.new(algorithm)
  data_bytes = data.encode('utf-8')
  hasher.update(data_bytes)
  hash_digest = hasher.hexdigest()
  return hash_digest
data = input("Enter the data to hash: ")
print("Choose a hash algorithm:")
print("1. MD5")
print("2. SHA-1")
print("3. SHA-256")
print("4. SHA-512")
choice = input("Enter your choice (1-4): ")
algorithm_map = {
  "1": "md5",
  "2": "sha1",
  "3": "sha256",
  "4": "sha512"
}
algorithm = algorithm_map.get(choice)
if algorithm:
  hash_result = generate_hash(data, algorithm)
  print("Hash:", hash_result)
else:
  print("Invalid choice.")
