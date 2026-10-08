package com.qx.perf;

import java.security.KeyPairGenerator;
import java.security.Signature;

public class LegacySigner49808 {
    public static byte[] sign(byte[] d) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        Signature s = Signature.getInstance("SHA256withRSA");
        s.initSign(kpg.generateKeyPair().getPrivate());
        s.update(d);
        return s.sign();
    }
}
