# SciPyのMLE(Miximam Likelihood Estimate)を用いて分布推定

## ライブラリの中にMLEが実装されている関数
- Normal(正規分布)
- Beta

## 自分で関数を定義して求める分布
- ポアソンとか


## 正規分布

### 正規分布の作成
numpyのモジュールでわさっと作ることができます
```python
import numpy as np

mu, sigma = 0, 0.1 # mean and standard deviation

# sigmaは分散
# muは真ん中
sample = np.random.normal(mu, sigma, 100000) 
```
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36629733-bc97815c-199d-11e8-9b17-5a61c22abaa0.png">
</div>

正規分布の推定
```python
from scipy.stats import norm

loc1, scale1 = norm.fit(sample)
print(loc1, scale1)
```
推定結果
```console
$ python3 norm-fit.py
mu=0.0005376030751632528, sigma=0.09992080119122795
```
うまくいくことが確認できた


## ベータ分布
#### ベータ分布の作成
```python
import numpy as np

a, b = 2, 5 # mean and standard deviation

sample = np.random.beta(a, b, 1000000) * 10 + 500
```
<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36629808-a66999b4-199e-11e8-8e5a-9a8a93920964.png">
</div>
