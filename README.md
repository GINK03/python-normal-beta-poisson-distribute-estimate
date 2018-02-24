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

# sigmaは大きさ
# muは真ん中
sample = np.random.normal(mu, sigma, 100000) * 1000
```
<div align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/36629733-bc97815c-199d-11e8-9b17-5a61c22abaa0.png">
</div>
