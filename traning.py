import sys

pattern = sys.stdin.readline().strip()
string = sys.stdin.readline().strip()

n, m = len(string), len(pattern)
x = 1
hpattern, acc, hstring = 0, 1, 0
for l in range(len(pattern)):
    hpattern += ord(pattern[l])
    hstring += ord(string[l])
if hstring == hpattern:
    if string[:m] == pattern:
        print(0, end=' ')
for i in range(1, n - m+1):
    hstring = (hstring - ord(string[i-1]))+ord(string[i+m-1])
    if hstring == hpattern:
        if string[i:i + m] == pattern:
            print(i, end=' ')
