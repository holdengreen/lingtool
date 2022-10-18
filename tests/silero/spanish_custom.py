# V3
import torch

language = 'es'
model_id = 'v3_es'
sample_rate = 48000
speaker = 'random'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)  # gpu or cpu

audio = model.apply_tts(text=example_text,
                        speaker=speaker,
                        sample_rate=sample_rate)

#print(dir(audio))

#print(str(audio[0][0]), str(audio[1]), str(audio[25]))

example_text = """VIAJE AL CENTRO DE LA TIERRA
JULIO VERNE
El domingo 24 de mayo de 1863, mi tío, el profesor Lidenbrock, regresó precipitadamente a su casa, situada en el número 19 de la König-strasse, una de las calles más antiguas del barrio viejo de Hamburgo.

Marta, su excelente criada, se azaró de un modo extraordinario, creyendo que se había retrasado, pues apenas si empezaba a cocer la comida en el hornillo.

“Bueno” pensé para mí, “si mi tío viene con hambre, se va a armar la de San Quintín porque dificulto que haya un hombre de menos paciencia.”"""

#audio_paths = model.save_wav(text=example_text,
#    speaker=speaker,
#    sample_rate=sample_rate)

#print(audio_paths)

from scipy.io import wavfile
import numpy as np
MAX_WAV_VALUE = 32768.0

audio *= MAX_WAV_VALUE
wavfile.write("newtest.wav", sample_rate, np.asarray(audio, dtype=np.int16))#audio.tolist())#.astype(np.int16))
