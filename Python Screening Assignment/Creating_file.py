# Creating example.txt file.

Original_file_content = "This is a placement assignment."

try:

    with open('example.txt', 'w') as f_write:
        f_write.writelines(Original_file_content)

except Exception as e:
    print(e)
