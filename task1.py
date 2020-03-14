import tempfile


def qsort(arr, left, right):
	if left >= right:
		return
	i = left
	j = right
	med = arr[(left + right) // 2]
	while i <= j:
		while arr[i] < med:
			i += 1
		while arr[j] > med:
			j -= 1
		if i <= j:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i += 1
			j -= 1
	if left < j:
		qsort(arr, left, j)
	if i < right:
		qsort(arr, i, right)


class Heap:
	def __init__(self):
		self.nodes = [None]
		self.size = 0

	def _upd(self, v):
		if v * 2 + 1 > len(self.nodes) or (self.nodes[v * 2] is None and self.nodes[v * 2 + 1] is None):
			return
		temp = self.nodes[v]
		if self.nodes[v * 2 + 1] is None or self.nodes[v * 2][0] <= self.nodes[v * 2 + 1][0]:
			if self.nodes[v * 2][0] > temp[0]:
				return
			self.nodes[v] = self.nodes[v * 2]
			self.nodes[v * 2] = temp
			self._upd(v * 2)
		else:
			if self.nodes[v * 2 + 1][0] > temp[0]:
				return
			self.nodes[v] = self.nodes[v * 2 + 1]
			self.nodes[v * 2 + 1] = temp
			self._upd(v * 2 + 1)

	def pop(self):
		if not self.size:
			return None
		root = self.nodes[1]
		self.size -= 1
		self.nodes[1] = self.nodes[self.size + 1]
		self.nodes[self.size + 1] = None
		self._upd(1)
		return root

	def push(self, x):
		v = self.size + 1
		if v >= len(self.nodes):
			self.nodes.extend([None] * len(self.nodes))
		self.nodes[v] = x
		self.size += 1
		while v > 1 and self.nodes[v][0] < self.nodes[v // 2][0]:
			temp = self.nodes[v]
			self.nodes[v] = self.nodes[v // 2]
			self.nodes[v // 2] = temp
			v //= 2


def sort_and_save(arr, files):
	qsort(arr, 0, len(arr) - 1)
	files += [tempfile.TemporaryFile('r+')]
	for x in arr:
		files[-1].write(str(x) + '\n')
	files[-1].seek(0)
	arr.clear()


def external_sort():
	max_size = 100000
	files = []
	with open('numbers.txt', 'r') as inf:
		a = []
		for line in inf.readlines():
			a += [int(line)]
			if len(a) > max_size:
				sort_and_save(a, files)
			inf.readline()
		if a:
			sort_and_save(a, files)

	with open('sorted.txt', 'w') as outf:
		heap = Heap()
		for i in range(len(files)):
			heap.push((int(files[i].readline()), i))
		x = heap.pop()
		while x:
			outf.write(str(x[0]) + '\n')
			try_add = files[x[1]].readline()
			if try_add:
				heap.push((int(try_add), x[1]))
			x = heap.pop()
	for file in files:
		file.close()


if __name__ == '__main__':
	external_sort()
