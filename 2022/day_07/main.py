from dataclasses import dataclass


def read_input(file_path):
    with open(file_path, 'r+') as f:
        return [line.strip() for line in f]


@dataclass
class FsNode(object):
    name: str


@dataclass
class Directory(FsNode):
    parent: FsNode = None
    children: list = None
    size: int = 0

    def __str__(self):
        return f'{self.name} (dir, size={self.size})'


@dataclass
class File(FsNode):
    parent: FsNode = None
    size: int = 0

    def __str__(self):
        return f'{self.name} (file, size={self.size})'


def find_node_by_name(nodes, name):
    for node in nodes:
        if node.name == name:
            return node


def print_tree(root, offset=0):
    tabs = '\t' * offset
    print(f"- {tabs}{root}")

    for node in root.children:
        if isinstance(node, Directory):
            print_tree(node, offset + 1)
        else:
            tabs = '\t' * (offset + 1)
            print(f"- {tabs}{node}")


def parse_console_log(console_log):
    THRESHOLD = 100000
    small_sizes = []
    current = None
    for line in console_log:
        if line.startswith('$ cd ..'):
            current.size = sum(node.size for node in current.children)
            if current.size <= THRESHOLD:
                small_sizes.append(current.size)

            current = current.parent

        elif line.startswith('$ cd '):
            _, name = line.split('$ cd ')
            if current:
                node = find_node_by_name(current.children, name)
                if not node:
                    node = Directory(name=name, parent=current, children=[])
                current = node
            else:
                # root dir
                current = Directory(name=name, parent=current, children=[])

        elif line.startswith('$ ls'):
            current.children = []
            current.size = 0

        elif line.startswith('dir'):
            file_type, name = line.split(' ')
            current.children.append(Directory(name=name, parent=current, children=[]))

        else:
            size, name = line.split(' ')
            current.children.append(File(name=name, parent=current, size=int(size)))

    prev = None
    while current:
        current.size = sum(node.size for node in current.children)
        if current.size <= THRESHOLD:
            small_sizes.append(current.size)
        prev = current
        current = current.parent

    return prev, sum(small_sizes)


def calc_dir(directory, small_sizes):
    THRESHOLD = 100000
    for child in directory.children:
        if isinstance(child, Directory):
            size = calc_dir(child, small_sizes)
        else:
            size = child.size
        directory.size += size

    if directory.size <= THRESHOLD:
        small_sizes[directory.name] = directory.size

    return directory.size


def gather_sizes(directory):
    sizes = []
    for child in directory.children:
        if isinstance(child, Directory):
            sizes.append(child.size)
            sizes += gather_sizes(child)
    return sizes


if __name__ == '__main__':
    console_log = read_input('input.txt')
    root, part1 = parse_console_log(console_log)
    print(f"The sum of the total sizes of directories with less than 100 000 size: {part1}")

    total_size = root.size
    disk_volume = 70000000
    free_space = disk_volume - total_size
    update_size = 30000000
    size_to_free = update_size - free_space

    dir_sizes = sorted(gather_sizes(root))
    diffs = {}
    for ds in dir_sizes:
        if ds - size_to_free >= 0:
            diffs[ds - size_to_free] = ds
    part2 = diffs[min(diffs.keys())]
    print(f"Size of the most satisfying directory: {part2}")
