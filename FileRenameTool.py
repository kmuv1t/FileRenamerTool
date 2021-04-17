import os


while True:
    try:
        print('-- Welcome to the File Rename Tool --')
        file = str(input('Type the route of the file you want to rename: '))
        destination = str(input('The route of the file + the new file name: '))
        os.rename(file, destination)
    except:
        print('File could not be renamed.')
    action = str(input('Do you want to rename more files? (Y/n): ')).upper()
    if action == 'Y':
        pass
    if action == 'N':
        break
    else:
        print("Please answer with 'Y' or 'N'.")
