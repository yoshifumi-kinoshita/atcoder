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
	k := string(slice[0])
	K, _ := strconv.Atoi(k)

	pair := K / 2
	var odd = 0
	if K%2 == 0 {
		odd = K / 2
	} else {
		odd = K/2 + 1
	}

	fmt.Println(pair * odd)

}
