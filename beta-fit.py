import numpy as np

a, b = 2, 5 # mean and standard deviation

# sigmaは大きさ
# muは真ん中
sample = np.random.beta(a, b, 1000000) * 10 + 500

obs_freq = {}
for s in sample.tolist():
  #print(s, s//0.001000)
  obs = s//0.1000
  if obs_freq.get(obs) is None:
    obs_freq[obs] = 0
  obs_freq[obs] += 1

for obs, freq in sorted(obs_freq.items(), key=lambda x:x[0]):
  #print(obs*0.1, freq)
  ...


from scipy.stats import beta

a1, b1, loc1, scale1 = beta.fit(sample)
print(f'a={a1}, b={b1}, loc={loc1}, scale={scale1}')
