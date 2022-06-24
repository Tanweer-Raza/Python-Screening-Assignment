# 1.Create a function in python to read the text file and replace specific content of the file.

old_string = "placement"
new_string = "screening"

try:

    with open('example.txt', 'r+') as f:
        content = f.read()
        replaced_content = content.replace(old_string, new_string)

except Exception as e:
    print(e)

try:
    with open('example.txt', 'w') as f_rep:
        f_rep.write(replaced_content)
        print("Replacement of the specific string has been done.")

except Exception as e:
    print(e)
