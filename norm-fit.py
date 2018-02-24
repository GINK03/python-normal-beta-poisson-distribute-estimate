import numpy as np

mu, sigma = 0, 0.1 # mean and standard deviation

# sigmaは分散　
# muは真ん中
sample = np.random.normal(mu, sigma, 100000) 

obs_freq = {}
for s in sample.tolist():
  #print(s, s//0.001000)
  obs = s//0.01000
  if obs_freq.get(obs) is None:
    obs_freq[obs] = 0
  obs_freq[obs] += 1

for obs, freq in sorted(obs_freq.items(), key=lambda x:x[0]):
  #print(obs*0.01, freq)
  ...


from scipy.stats import norm

loc1, scale1 = norm.fit(sample)
print(f'mu={loc1}, sigma={scale1}')
