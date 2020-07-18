from Crypto.Cipher import ARC4
 
def encrypt(message, key):
    des = ARC4.new(key)
    cipher_text = des.encrypt(message)
    return cipher_text
 
def decrypt(cipher_text, key):
    des3 = ARC4.new(key)
    message = des3.decrypt(cipher_text)
    return message

f = open('ha.pyc', 'wb')
data =  b'\x7A\xA2\xA7\xFE\x8C\x08\xF8\x4B\xA4\xA1\x4E\x02\x16\x56\x6C\xAB\x32\xEF\x39\xEC\x12\x46\x3A\x44\x91\xB2\x47\x26\x2A\xAA\xDB\xB8\x2F\x78\x0A\x16\x55\x09\xFE\x16\x50\xC6\xF5\x01\x0D\x1B\x48\x01\x16\x7C\x1A\xD7\x44\xBF\xDC\x83\x22\x9A\x9B\x9A\xD5\x2F\xAA\xEA\x27\x2C\xF5\x13\x0B\xA2\xE6\xCA\x2C\x1C\x18\x1B\x9F\xDC\xEB\x94\x0A\xDC\x7D\xBF\x35\x6F\xB9\xC0\x45\x97\x18\xE8\xB5\xCD\x9E\x51\xCF\x08\x68\xE4\xB7\x66\x19\x56\x65\x44\xCC\xF2\x7C\x55\xFD\x8A\x15\xDB\x6A\xD8\xF9\x08\x3F\x5E\x60\x3D\x3C\x99\x6A\x3C\x5D\x24\xAC\x66\xC5\xF9\x4D\x04\xCB\x2D\x25\x18\x8B\xEB\xA5\x6A\xE6\x65\x43\xCB\xA3\xCD\x57\x87\xE6\x0F\x22\x19\x59\x59\x2E\x7E\xC5\x6A\x07\x27\x18\x82\x4A\x5C\xDC\xAF\x57\x55\x6A\xE3\xB7\x04\x5E\x3E\x21\xBF\x86\xE6\x46\x5A\xDD\x88\x19\x84\x1D\x61\x18\x4B\x6D\xC6\xBE\x87\x2E\x44\xA6\xA2\x6D\x6B\xA3\x53\x93\x16\x50\xC6\x2D\xB2\x92\xD8\x58\xDC\x31\xBA\xD0\x55\x5C\xAE\xB3\xA4\xC9\x36\x79\xAA\xD1\xFD\x8D\xC9\x80\x30\x85\xD1\x6F\xF2\x85\x34\xEB\x63\xB2\xBF\x65\x9D\xEC\x24\xD6\x22\x81\x78\x1F\x07\x50\xD7\xB0\xBB\xDE\xEB\xF3\x43\x97\x2B\x4C\x40\x25\xDC\xD0\x0D\x25\x85\x5C\x86\x0D\xAD\xB7\x7B\x22\x41\x03\x88\x00\xB8\xC8\x56\x90\x8D\xF9\x71\x4A\x11\x37\x0C\xA1\x73\x29\xDE\x28\xF4\x3E\xD2\x74\x89\x12\xA3\x3D\x8F\x11\x9A\x08\x95\x11\x9D\xE2\xCF\x2F\x79\x80\xA2\xDB\x71\x99\x25\x96\x63\x2B\x5A\x93\x02\x4C\x7E\x0C\xCE\x96\x3D\x7C\x38\x2F\x96\x1C\x76\xEF\xB4\x6C\x44\x15\x32\xB5\x7A\x34\x73\x02\x94\x75\xA1\xBA\xDD\x43\x17\x6A\x6B\xE0\x3D\x5A\xB3\xCB\xFB\xD1\x1D\x0A\x65\x9E\x1A\xF1\x2D\x79\xB1\xBD\x53\x6C\x43\xF0\x29\x13\x6F\xE7\x9F\x42\xA1\xEE\xE8\x71\x0B\x6D\xA9\x93\xB9\xD1\x89\xA1\xA5\x92\x69\xD7\x50\x70\xD4\x41\xB2\x68\x19\xC9\xCB\x71\xA4\x6E\x38\xD7\x8F\x50\xEE\xE5\xBD\x97\x02\x2A\xDC\xD0\xCC\x04\x71\xF4\x7C\x1F\xCA\xF9\xF7\x7E\x61\xE1\x6F\xD1\xFA\xBC\x94\x86\x67\xEF\x31\x6D\xFD\x86\x3D\xD5\x78\xBD\x53\x5A\xCB\xD6\xE4\x62\x19\x3A\x2C\xC7\x87\x2B\xF5\xA2\x89\xD0\x48\x2F\xAC\x0C\xAF\x8E\x50\xB5\x21\x11\x84\x46\x75\xED\x2A\x47\x08\xFF\xAA\xD9\x00\xBA\xB3\xBB\x3E\xBF\x81\x7A\x20\x01\xE3\x13\x8A\x48\xA9\x7F\x56\xD1\x85\x5F\xE6\x4D\xAB\x0C\x33\x33\x5C\xAC\xE2\xFB\x45\xBA\xE4\xE1\x12\x7B\xE0\x0A\xDA\x3F\x43\xAF\xA7\x78\x8E\xA8\xE5\xA5\xE9\x71\x47\x26\x72\x6D\x09\xA0\x18\xAA\xCE\x0F\x89\xDD\xAD\xA1\xFD\xE1\xC4\x83\x6B\x2E\x69\xCC\x9B\xA9\x1F\x0C\xC9\x57\x93\x8A\x42\x36\x69\xA1\xC0\x03\xE1\xC4\x58\xB9\xF4\x09\x79\x01\x6B\xA8\x5C\x4E\xF6\x45\x57\x29\xF0\xAF\x16\xDA\xFD\x3A\x93\x76\xEC\xCA\x69\x13\x11\x15\xAC\x85\x19\xCC\xDA\x6B\x60\x65\xAF\x9B\x22\xE2\xF2\x20\xF7\xCE\xE3\xA8\x71\x87\x0C\x67\xE3\x4B\x54\xCA\x2F\x68\x72\x62\xB6\x5D\x89\x07\x71\xA0\x7D\xBA\xD9\x80\x15\x43\xCC\x73\xE2\x31\xAA\x31\x8F\x73\xE0\xDB\x55\xAA\xA4\x00\x8A'
key = b'\x01\x03\x03\x07\x03\x03\x08\x01'
plain = decrypt(data, key)
f.write(plain)
f.close()