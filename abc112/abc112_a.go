package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	N, _ := strconv.Atoi(s)

	if N == 1 {
		fmt.Println("Hello World")
	} else if N == 2 {
		s, _ = r.ReadString('\n')
		s = strings.TrimRight(s, " \t\n")
		A, _ := strconv.Atoi(s)
		s, _ = r.ReadString('\n')
		s = strings.TrimRight(s, " \t\n")
		B, _ := strconv.Atoi(s)
		fmt.Println(A + B)
	}

}
