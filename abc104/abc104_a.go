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
	R, _ := strconv.Atoi(s)

	if R < 1200 {
		fmt.Println("ABC")
	} else if R < 2800 {
		fmt.Println("ARC")
	} else {
		fmt.Println("AGC")
	}

}
