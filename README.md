# 7-FSK with raised_cosine pulses

## Decoding steps (variable name of each step):

1. **raw_symbols[160]** = list of the audio snipets of all the symbols sounds as raw recorded.

2. **filtered_symbol[7]** = for ONE given symbol (among the 160), this contains the 7 arrays reprensenting the 7 filtered audio snippets, 1 per frequency.

3. **freq_cosine[7]** = the list of the 7 arrays representing the 7 (clean) raised cosines frequencies that may (or not) compose the sent signal.

4. **correlated_symbol[7]** = list of 7 arrays corresponding to the 7 cross-correlations of the filtered audio snippets of a symbol, with the 7 clean raised-cosines.

5. **amplitude_symbol[7]** = list of 7 floats reprensenting the average amplitude of the 7 cross-correlations (if large, then the very frequency was sent, else it wasn't).

6. **decoded_symbol[7]** = list of the 7 bits (representing 1 symbol) that were sent during the symbol duration, going from the lowest freq to the highest.