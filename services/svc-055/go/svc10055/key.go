package svc10055

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
)

func NewKey10055() (*ecdsa.PrivateKey, error) {
	return ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
}
