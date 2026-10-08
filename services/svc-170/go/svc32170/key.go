package svc32170

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
)

func NewKey32170() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}
