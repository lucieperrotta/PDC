import numpy as np
import scipy.signal as sgn

def raised_cosine(shifted_freq, time_per_symb, samp_freq, roll_off=0.5):
    shifted_freq /= 2
    np.seterr(invalid='ignore')
    
    pulse = np.linspace(- time_per_symb, time_per_symb, samp_freq * time_per_symb)
    
    numerator = np.cos((1 + roll_off) * np.pi * pulse / time_per_symb) + \
              (1 - roll_off) * np.pi / (4 * roll_off) * np.sinc((1 - roll_off) * pulse / time_per_symb)
    denominator = 1 - (4 * roll_off * pulse / time_per_symb) ** 2
    
    limit_case = roll_off / (np.pi * np.sqrt(2 * time_per_symb)) * ((np.pi + 2) * np.sin(np.pi / (4 * roll_off)) + \
             (np.pi - 2) * np.cos(np.pi / (4 * roll_off)))
    
    out = 4 * roll_off / (np.pi * np.sqrt(time_per_symb)) * numerator / denominator
    out[np.isnan(out)] = limit_case
    out *= np.cos(2 * np.pi * shifted_freq * pulse)
    
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