package main

import (
	"bufio"
	"fmt"
	"os"
	//"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	v := 0
	for i := 0; i < len(s); i++ {
		if '+' == s[i] {
			v += 1
		} else if '-' == s[i] {
			v -= 1
		}
	}
	fmt.Println(v)

}
