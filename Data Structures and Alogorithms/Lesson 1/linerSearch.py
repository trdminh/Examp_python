def linerSearch(arr : list[int], target: int):
    condition = 0
    while condition <= len(arr):
        if arr[condition] == target:
            return condition
        else:
            condition += 1