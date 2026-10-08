package svc11895

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
)

func NewKey11895() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}
