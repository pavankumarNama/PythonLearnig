# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values


def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them. 
    print(s + b.decode("utf-8"))
    # TODO: Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    print(s + b.decode("utf-16"))
    # TODO: encode the string as UTF-32
    print(s.encode('utf-8') + b)
    print(s.encode('utf-16') + b)
    print(s.encode('utf-32') + b)


if __name__ == "__main__":
    main()
