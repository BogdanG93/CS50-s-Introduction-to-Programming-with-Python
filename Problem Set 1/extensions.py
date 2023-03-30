"""In a file called extensions.py, implement a program that prompts the user for the name of a file
and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.

Here’s how to test your code manually:

Type happy.jpg and press Enter. Your program should output:
image/jpeg
Type document.pdf and press Enter. Your program should output:
application/pdf
Be sure to test each of the other file formats, vary the casing of your input, and “accidentally” add spaces on either
side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively."""

file_ext = input('File name: ').lower().strip()
if '.gif' in file_ext:
    print('image/gif')
elif '.jpg' in file_ext or '.jpeg' in file_ext:
    print('image/jpeg')
elif '.png' in file_ext:
    print('image/png')
elif '.pdf' in file_ext:
    print('application/pdf')
elif '.txt' in file_ext:
    print('text/plain')
elif '.zip' in file_ext:
    print('application/zip')
else:
    print('application/octet-stream')
