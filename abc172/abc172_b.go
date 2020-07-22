package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	S, _ := r.ReadString('\n')
	T, _ := r.ReadString('\n')
	S = strings.TrimRight(S, " \t\n")
	T = strings.TrimRight(T, " \t\n")

	count := 0

	for i := 0; i < len(S); i++ {
		if S[i] != T[i] {
			count++
		}
	}
	fmt.Println(count)

}
