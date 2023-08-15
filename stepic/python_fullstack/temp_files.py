import os
import tempfile

print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

(tempfh, tempfp) = tempfile.mkstemp(".tmp", "test_temp", None, True)
f = os.fdopen(tempfh, "w+t")
f.write('Temp text data')
f.seek(0)
print(f.read())
f.close()
os.remove(tempfp)

with tempfile.TemporaryFile(mode='w+t') as tfp:
    tfp.write('Some more temp text data')
    tfp.seek(0)
    print(tfp.read())


with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp, "temp_text.txt")
    tfp = open(path, "w+t")
    tfp.write("The next temp text data")
    tfp.seek(0)
    print(tfp.read())
    tfp.close()