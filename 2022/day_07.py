from utils import parse_input


def do_walk(commands):
    files = {}
    folders = ['/']

    path = ['/'] # start in root

    for cmd in commands:
        # command
        if cmd.startswith('$ '):
            # change dir
            if cmd.startswith('$ cd'):
                dir = cmd[5:]
                if dir == '/':
                    path = ['/']
                elif dir == '..': # go back
                    path = path[:-1]
                else:
                    path.append(dir)
                    folder_path = '/'.join(path)
                    if folder_path not in folders:
                        folders.append(folder_path)
            # otherwise do nothing
        # file or directory
        else:
            # file
            if not cmd.startswith('dir'):
                cmd = cmd.split()
                file_path = '/'.join(path)+f'/{cmd[1]}'
                if file_path not in files:
                    files[file_path] = int(cmd[0])
    
    return files, folders


def find_sum(contents, max_size):
    files, folders = do_walk(contents)

    total_size = 0
    for folder in folders:
        folder_size = 0
        for path, size in files.items():
            if path.startswith(folder):
                folder_size += size
        if folder_size <= max_size:
            total_size += folder_size

    return total_size


def find_folder_sizes(contents):
    files, folders = do_walk(contents) 
    sizes = []

    for folder in folders:
        folder_size = 0
        for path, size in files.items():
            if path.startswith(folder):
                folder_size += size
        sizes.append(folder_size)

    return sizes


def to_delete(contents):
    folder_sizes = find_folder_sizes(contents)
    required_space = 30000000 - (70000000 - max(folder_sizes))

    larger_sizes = [size for size in folder_sizes if size >= required_space]

    larger_sizes.sort()

    return larger_sizes[0]


def __main__():
    contents, test = parse_input(__file__.split('/')[-1].replace('.py', ''))
    
    assert find_sum(test, 100000) == 95437, 'failed part 1 test'
    print(f'Part 1: {find_sum(contents, 100000)}')

    assert to_delete(test) == 24933642, 'failed part 2 test'
    print(f'Part 2: {to_delete(contents)}')

if __name__ == '__main__':
    __main__()
