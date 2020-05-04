package main

const (
	mod = 2048
)

type MyHashMap struct {
	set [mod]*listNode
}

type listNode struct {
	key  int
	val  int
	next *listNode
}

/** Initialize your data structure here. */
func Constructor() MyHashMap {
	arr := [mod]*listNode{}
	return MyHashMap{set: arr}
}

/** value will always be non-negative. */
func (this *MyHashMap) Put(key int, value int) {
	i := key % mod
	ptr := this.set[i]
	for ptr != nil {
		if ptr.key == key {
			ptr.val = value
			return
		} else {
			ptr = ptr.next
		}
	}
	node := &listNode{key: key, val: value, next: this.set[i]}
	this.set[i] = node
	// node := &listNode{key: key, val: value, next: this.set[i]}

}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
func (this *MyHashMap) Get(key int) int {
	ptr := this.set[key%mod]
	for ptr != nil {
		if ptr.key == key {
			return ptr.val
		} else {
			ptr = ptr.next
		}
	}
	return -1
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
func (this *MyHashMap) Remove(key int) {
	i := key % mod
	ptr := this.set[i]
	prev := &listNode{next: ptr}
	head := prev

	for ptr != nil {
		if ptr.key == key {
			prev.next = ptr.next
			break
		} else {
			prev = prev.next
			ptr = ptr.next
		}
	}
	// fmt.Println("removing ", head.next, ptr.next, ptr)
	this.set[i] = head.next
}

func main() {
	obj := Constructor()
	obj.Put(1, 10)
	obj.Put(2, 20)

	// param_2 := obj.Get(1)
	// fmt.Println(obj, param_2)

	obj.Remove(1)
	// fmt.Println(obj, param_2)
}
