# V3
import torch

language = 'en'
model_id = 'v3_en'
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

print(dir(audio))


audio_paths = model.save_wav(text=example_text,
    speaker=speaker,
    sample_rate=sample_rate)

print(audio_paths)
