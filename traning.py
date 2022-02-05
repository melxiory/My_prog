import sys


def get_page(logical_addr: int):
    pml4 = (logical_addr >> 39) & 0x1ff
    dir_ptr = (logical_addr >> 30) & 0x1ff
    directory = (logical_addr >> 21) & 0x1ff
    table = (logical_addr >> 12) & 0x1ff
    offset = logical_addr & 0xfff

    return (pml4, dir_ptr, directory, table, offset)


def get_page_phy_addr(value: int):
    return (value & ((0xffffffffff) << 12))


def get_phy_addr(page: tuple, mem_struct: dict, cr3: int):
    value = cr3

    for i in range(len(page) - 1):
        index = page[i] * 8
        value = mem_struct.get(index + value, 0)

        if value & 1 == 0:
            print("fault")
            return

        value = get_page_phy_addr(value)

    print(value + page[-1])

f = open('dataset_44327_15.txt', 'r')

m, q, r = tuple(map(int, f.readline().strip().split()))
m_str = dict([[int(i) for i in f.readline().strip().split()] for _ in range(m)])
log_addr = [int(f.readline().strip()) for _ in range(q)]

for i in log_addr:
    p = get_page(i)
    get_phy_addr(p, m_str, r)



