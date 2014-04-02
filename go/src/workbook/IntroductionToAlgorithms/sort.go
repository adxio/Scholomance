package main

import (
	"fmt"
)

func insertionSort(l []int) {
	for i := 1; i < len(l); i++ {
		key := l[i]
		for j := i - 1; j >= 0 && l[j] > key; j-- {
			l[j+1] = l[j]
			l[j] = key
		}
	}
}

func merge(l []int, p, q, r int) {
	left := make([]int, q-p)
	copy(left[:], l[p:q])
	right := make([]int, r-q)
	copy(right[:], l[q:r])

	i := 0
	j := 0
	for k := p; k <= r; k++ {
		if i == len(left) && j == len(right) {
			break
		}
		if i == len(left) {
			l[k] = right[j]
			j++
			continue
		}
		if j == len(right) {
			l[k] = left[i]
			i++
			continue
		}

		if left[i] > right[j] {
			l[k] = right[j]
			j++
		} else {
			l[k] = left[i]
			i++
		}
	}
}

func mergeSort(l []int, p, r int) {
	if p+1 < r {
		q := (p + r) / 2
		mergeSort(l, p, q)
		mergeSort(l, q, r)
		merge(l, p, q, r)
	}
}

func bubbleSort(l []int) {
	for i, _ := range l {
		for j := len(l) - 1; j > i; j-- {
			if l[j] < l[j-1] {
				l[j], l[j-1] = l[j-1], l[j]
			}
		}
	}
}

func main() {
	var l []int
	l = []int{53, 39, 6, 81, 1, 8, 32}
	insertionSort(l)
	fmt.Println("InsertionSort:", l)

	l = []int{53, 39, 6, 81, 1, 8, 32}
	mergeSort(l, 0, len(l))
	fmt.Println("MergeSort:", l)

	l = []int{53, 39, 6, 81, 1, 8, 32}
	bubbleSort(l)
	fmt.Println("BubbleSort:", l)
}
