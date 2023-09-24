import librosa
import os
from operator import itemgetter
from distutils.dir_util import copy_tree

# Export Dynamikstufe_RR(iteriert)_MICnr 
# Input: Anzahl Dynamikstufen
#   x x x x x x x x x x x x
#   a a a b b b c c c d d d 
total_dynamics = 7 





#Anzahl verwendeter Mikrofone
#Array Position if loudest Mic
loudest_mic=0
num_mics = 3

#Sample Name
sample_name = "Snr01"
sample_count = 169
#Audio Ordner
audio_dir = "/Users/thomassoellner/workspace/python/samplesort/Files/Export_Von_Cubase/Snr_01/"
sorted_dir = "/Users/thomassoellner/workspace/python/samplesort/Files/Sorted/Snr_01/"
copy_tree(audio_dir, sorted_dir)

# Funktion zur Messung der durchschnittlichen Lautstärke einer Audiodatei
def measure_volume(audio_file):
    y, sr = librosa.load(audio_file)
    rms = librosa.feature.rms(y=y)
    return rms.mean()

#Find all Audio files
count = 0
files = []

while count<=sample_count:
    fileToAppend = [f for f in os.listdir(audio_dir) if f.endswith('_ '+str(count)+'.wav')]
    fileToAppend.sort()
    files.append(fileToAppend)
    count += 1
#audio_files = [f for f in os.listdir(audio_dir) if f.startswith(sample_name+'__MIC1') & f.endswith('.wav')]
#
print('Sorting using the loudness of Mic: ',files[0][loudest_mic].split("_")[2])
for setOfSamples in files:
    full_path = os.path.join(audio_dir, setOfSamples[loudest_mic])
    volume = measure_volume(full_path)
    setOfSamples.append(volume)
sorted_files = sorted(files, key=itemgetter(3),reverse=False)
#print(sorted_files)

new_order= 0
dynamic_stage = 0
rr_value = 0
for setOfSamples in sorted_files:

    i = 0
    while i<num_mics:
        #print(setOfSamples[i].split(' ')[0]+str(new_order)+'.wav',setOfSamples[3])
        
        # name =str(dynamic_stage)+"_"+str(rr_value)
        # print(name)
        os.rename(sorted_dir+setOfSamples[i],sorted_dir+setOfSamples[i].split(' ')[0]+'_newOrder_'+str(new_order)+'.wav')
        i += 1
    new_order+=1

print('>>Sorted');
  #os.rename(setOfSamples[0])