import math


class Container:

    def __init__(self, capacity, radius):
        self.radius = radius
        self.capacity = capacity

    def __lt__(self, other):
        return (self.radius, self.capacity) < (other.radius, other.capacity)

    def __repr__(self):
        return 'Container(capacity={capacity}, radius={radius})'.format(capacity=self.capacity, radius=self.radius)


class Package:

    def __init__(self, length, copies):
        self.copies = copies
        self.length = length

    def __lt__(self, other):
        return (self.length, self.copies) < (other.length, other.copies)

    def __repr__(self):
        return 'Package(length={length}, copies={copies})'.format(length=self.length, copies=self.copies)


def maximum_packages(s_arr, k_arr , r_arr, c_arr):
    packages = sorted([Package(length=s_arr[i], copies=k_arr[i]) for i in range(len(s_arr))], reverse=True)
    # print(packages)
    containers = sorted([Container(radius=r_arr[i], capacity=c_arr[i]) for i in range(len(r_arr))], reverse=True)
    # print(containers)
    packages_in_containers = 0
    for container in containers:
        while packages and container.radius <= packages[0].length/math.sqrt(2):
            packages.pop(0)
        while packages and packages[0].copies <= container.capacity and container.radius > packages[0].length/math.sqrt(2):
            packages_in_containers += packages[0].copies
            container.capacity -= packages[0].copies # capacity left
            packages.pop(0) # remove all containers of this type
            # print(container)
        if not(container.capacity):
            continue
        while packages and packages[0].copies > container.capacity and container.radius > packages[0].length/math.sqrt(2):
            packages_in_containers += container.capacity
            packages[0].copies -= container.capacity
            continue
    return packages_in_containers


n, m = list(map(int, input().split()))
S = list(map(int, input().split()))
K = list(map(int, input().split()))
R = list(map(int, input().split()))
C = list(map(int, input().split()))
print(maximum_packages(s_arr=S, k_arr=K, r_arr=R, c_arr=C))
