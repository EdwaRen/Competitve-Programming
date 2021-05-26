package main

import (
	"fmt"
)

type ListNode struct {
	Val int 
	Next *ListNode
}

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var s1 []int
	var s2 []int

	l1Ptr := l1 
	for l1Ptr != nil {
		s1.append(l1Ptr.Val)
		l1Ptr = l1Ptr.Next 
	}

}