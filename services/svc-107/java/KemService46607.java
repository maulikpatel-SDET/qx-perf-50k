package com.qx.perf;

import java.security.KeyPairGenerator;
import java.security.Security;
import org.bouncycastle.jcajce.spec.MLKEMParameterSpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class KemService46607 {
    public static Object keys() throws Exception {
        Security.addProvider(new BouncyCastleProvider());
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM", "BC");
        kpg.initialize(MLKEMParameterSpec.ml_kem_768);
        return kpg.generateKeyPair();
    }
}
