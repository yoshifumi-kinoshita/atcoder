package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	if 'A' <= s[0] && s[0] <= 'Z' {
		fmt.Println("A")
	} else if 'a' <= s[0] && s[0] <= 'z' {
		fmt.Println("a")
	}
}
