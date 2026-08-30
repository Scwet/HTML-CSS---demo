import numpy as np
import librosa as lb #读取音频文件

path = "E:\\桌面\\项目\\基于骨传导的低成本无人机炸机预警系统\\sound\\1.mp3"
data, sr = lb.load(path,sr=None) #表示使用原始采样率

N = len(data)
fft_data = np.fft.fft(data)
freqs = np.fft.fftfreq(N, 1)

mag = np.abs(fft_data[:N//2]) / N * 2 # 计算幅度谱

#print(mag)
print(sr)