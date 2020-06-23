package main

import (
	"bufio"
	"fmt"
	//"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	s, _ := r.ReadString('\n')
	s = strings.TrimRight(s, " \t\n")
	slice := strings.Split(s, " ")
	n := string(slice[0])
	i := string(slice[1])
	N, _ := strconv.Atoi(n)
	I, _ := strconv.Atoi(i)

	fmt.Println(N + 1 - I)
}
