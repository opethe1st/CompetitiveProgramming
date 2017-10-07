import sys
#  import bisect
q = int(raw_input().strip())
files = dict()
# Process each command


def create(filename):
    global files
    if filename not in files:
        files[filename] = ([], 1)
        return (filename)
    elif files[filename][0] != [] and files[filename][0][0] == 0:
        deleted, last = files[filename]
        deleted.pop(0)
        files[filename] = (deleted, last)
        return (filename)
    else:
        # print 'here'
        deleted, last = files[filename]
        if deleted == []:
            suffix = last
            last += 1
            files[filename] = (deleted, last)
            return '%s(%s)' % (filename, suffix)
        else:
            suffix = deleted.pop(0)
            files[filename] = (deleted, last)
            return '%s(%s)' % (filename, suffix)


def delete(filename):
    global files
    if '(' in filename:
        filename, number = filename.split('(')
        deleted, last = files[filename]
        if last == int(number[:-1]):
            files[filename] = (deleted, last - 1)
        else:
            deleted.append(int(number[:-1]))
            deleted.sort()
            files[filename] = (deleted, last)
    else:
        deleted, last = files[filename]
        deleted.append(0)  # deleted the first name
        deleted.sort()
        files[filename] = (deleted, last)
    return '%s' % (filename)


def rename(filename1, filenam2):
    # delete
    delete(filename1)
    val = create(filename2)


def executeCommand(command):
    if command[:3] == 'crt':
        filename = command[4:]
        print '+ %s' % (create(filename))

    elif command[:3] == 'del':
        filename = command[4:]
        delete(filename)
        print '- %s' % (filename)
    else:
        com, filename1, filename2 = command.split()
        delete(filename1)
        filename2 = create(filename2)
        print 'r %s -> %s' % (filename1, filename2)


for a0 in xrange(q):
    # Read the first string denoting the command type
    command = raw_input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    executeCommand(command)
