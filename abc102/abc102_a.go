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

	if N%2 == 0 {
		fmt.Println(N)
	} else {
		fmt.Println(N * 2)
	}
}
