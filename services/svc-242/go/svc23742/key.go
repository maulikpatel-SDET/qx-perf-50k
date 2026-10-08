package svc23742

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
)

func NewKey23742() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}
