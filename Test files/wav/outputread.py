import numpy
f1 = numpy.fromfile(open("/media/prabathbk/EDUCATION/Acedemics/Sem 3/Com design project/Project/Test files/wav/output.py"), dtype=numpy.uint8)
print(f1)

import wave

w = wave.open("Salli - Sarith and Surith - Tune.lk.wav", "rb")
binary_data = w.readframes(w.getnframes())
w.close()