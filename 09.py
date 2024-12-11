data = "2333133121414131402"


def build_sparse_list(data):
    sparse = []
    empty_positions = []
    it = iter(data)
    id = 0
    cur_pos = 0
    while True:
        try:
            block_length = int(next(it))
            sparse.extend([id] * block_length)
            cur_pos += block_length
            id += 1
            empty_length = int(next(it))
            sparse.extend([None] * empty_length)
            empty_positions.extend(range(cur_pos, cur_pos + empty_length))
            cur_pos += empty_length
        except StopIteration:
            break

    return sparse, empty_positions


def build_dense_list(data):
    dense = []
    it = iter(data)
    id = 0
    while True:
        try:
            block_length = int(next(it))
            dense.append((id, block_length))
            id += 1
            empty_length = int(next(it))
            dense.append((None, empty_length))
        except StopIteration:
            break

    return dense


def part_one(data):
    sparse, empty_positions = build_sparse_list(data)
    # print(sparse)
    # print(empty_positions)
    for pos in empty_positions:
        while (block := sparse.pop()) is None:
            pass
        try:
            sparse[pos] = block
        except IndexError:
            sparse.append(block)
            break

    # print(''.join(str(x) for x in sparse))

    checksum = 0
    for i, id in enumerate(sparse):
        checksum += i * id

    return checksum


def gc(dense):
    i = 0
    while i < len(dense):
        id, length = dense[i]
        if id is not None:
            continue
        try:
            while dense[i + 1][0] is None:
                lengthh = dense[i + 1][1]
                dense.pop(i + 1)
                length += lengthh
                dense[i] = (None, length)
        except IndexError:
            continue


def part_two(data):
    dense = build_dense_list(data)
    i = len(dense) - 1
    while i >= 0:
        id, length = dense[i]
        if id is None:
            i -= 1
            continue

        for j, (idd, lengthh) in enumerate(dense[:i]):
            if idd is not None:
                continue
            if length <= lengthh:
                dense.pop(i)
                dense.insert(j, (id, length))
                dense.insert(i, (None, length))
                dense[j + 1] = (None, lengthh - length)
                break
            else:
                continue
            
            gc(dense)

        i -= 1

    checksum = 0
    cur_pos = 0
    for id, length in dense:
        for i in range(cur_pos, cur_pos + length):
            # print(id or '.', end="")
            checksum += i * (id or 0)
        cur_pos += length

    print()

    return checksum


# print(part_one(data))
# print(part_two(data))


with open("09.txt") as inf:
    data = inf.read().strip()
    print(part_one(data))
    print(part_two(data))
