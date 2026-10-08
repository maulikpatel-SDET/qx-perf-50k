package svc31865

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
)

func NewKey31865() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}
