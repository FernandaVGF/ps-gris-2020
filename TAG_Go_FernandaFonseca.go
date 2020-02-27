// PROCESSO SELETIVO - Grupo de Resposta a Incidentes de Segurança

// Nome: Fernanda Veiga Gomes da Fonseca
// TAG - Segurança Web I - Entrega: 27/02/2020

package main

import (
	"fmt"
	"net"
	"sync"
)

func scan (worker int, port int, waitGroup *sync.WaitGroup) error {
	address := fmt.Sprintf ("scanme.nmap.org: %d", port)
	conn, err := net.Dial ("tcp", address)

	fmt.Printf ("Worker %d\n", worker)

	if err != nil {
		fmt.Printf ("%d: %s\n", port, err.Error ())
		return err
	}

	conn.Close ()

	fmt.Printf ("%d: open\n", port)

	defer waitGroup.Done ()
	return nil
}

func main() {
	var waitGroup sync.WaitGroup

	for i := 20; i < 30; i++ {
		waitGroup.Add (1)
		go scan (1, i, &waitGroup) // Goroutine #1

		if i < 30 {
			i++
			waitGroup.Add (1)
			go scan (2, i, &waitGroup) // Goroutine #2
		}
	}

	waitGroup.Wait ()
}