import hashlib

BLOCK_SIZE = 64
HASH_SIZE = 32

def compression_function(state, block):
    hash_object = hashlib.sha256()
    hash_object.update(state)
    hash_object.update(block)
    return hash_object.digest()

def hash_function(message):
    padded_message = message.encode() + b'\x80' + b'\x00' * (BLOCK_SIZE - (len(message.encode()) + 1) % BLOCK_SIZE)
    padded_message += (len(message.encode()) * 8).to_bytes(BLOCK_SIZE, 'big')

    state = b'\x00' * HASH_SIZE  # Use a unique IV

    for i in range(0, len(padded_message), BLOCK_SIZE):
        block = padded_message[i:i+BLOCK_SIZE]
        state = compression_function(state, block)

    return state

message = input("Enter the input: ")
hash_value = hash_function(message)
print('Encoded Hash:', hash_value.hex())
