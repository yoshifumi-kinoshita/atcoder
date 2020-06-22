package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	if s[2] == s[3] && s[4] == s[5] {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
