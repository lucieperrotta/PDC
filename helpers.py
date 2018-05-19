import numpy as np
import scipy.signal as sgn

def raised_cosine(freq, pulse_dt, rate, beta=0.5):
    freq /=2
    np.seterr(invalid='ignore')
    pulse_t = np.linspace(- pulse_dt, pulse_dt , rate * pulse_dt)
    p_const = 4 * beta / (np.pi * np.sqrt(pulse_dt))
    p_cos = np.cos((1 + beta) * np.pi * pulse_t / pulse_dt) 
    p_sinc = (1 - beta) * np.pi / (4 * beta) * np.sinc((1 - beta) * pulse_t / pulse_dt)
    p_denomin = 1 - (4 * beta * pulse_t / pulse_dt) ** 2
    p_hosp = beta / (np.pi * np.sqrt(2 * pulse_dt)) * ((np.pi + 2) * np.sin(np.pi / (4 * beta)) + (np.pi - 2) * np.cos(np.pi / (4 * beta)))
    out = p_const * (p_cos + p_sinc) / p_denomin
    out[np.isnan(out)] = p_hosp
    out *= np.cos(2 * np.pi * freq * pulse_t)
    assert not any(np.isnan(out))    
    np.seterr(invalid='warn')
    return out

# Do not use this one, it's only used in the next function!!!
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = sgn.butter(order, [low, high], btype='band')
    return b, a

# Bandpass filter applied on array "data"
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = sgn.lfilter(b, a, data)
    return y