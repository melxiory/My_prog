def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))



print(increment_string("foo"))
print(increment_string("foobar001"))
print(increment_string("foobar99"))
print(increment_string('000000000653431929'))

