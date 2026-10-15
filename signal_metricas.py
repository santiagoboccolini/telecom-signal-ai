import numpy as np
    
    def calculate_snr(signal_power_watts, noise_power_watts):
        """Calcula la relacion senal a ruido (SNR) en decibeles (dB)."""
        if noise_power_watts <= 0:
            raise ValueError("La potencia de ruido debe ser mayor que 0.
  ")
        snr_linear = signal_power_watts / noise_power_watts
        return 10 * np.log10(snr_linear)

    if __name__ == "__main__":
        snr = calculate_snr(signal_power_watts=0.05, 
  noise_power_watts=0.001)
        print(f"SNR calculado: {snr:.2f} dB")
    EOF
