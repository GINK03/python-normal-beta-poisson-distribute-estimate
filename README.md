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

### 正規分布の推定

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

### ベータ分布の推定

```console
$ python3 beta-fit.py
a=1.9950566139379418, b=4.987435163823774, loc=500.00146380353016, scale=9.990241431834761
```
うまくいく

##### 注意
a < 1.0, b < 1.0のような場合、ベータ分布は外側に大きくなるような性質があるのだが、このときにscipyのMLEではうまくフィットしない  
(初期条件やなんやらが影響していると思います)  

<div align="center">
  <img width="400px" src="https://user-images.githubusercontent.com/4949982/36629981-edfaca0c-19a1-11e8-9121-c6f9350ca777.png">
</div>

## ポアソン分布
### ポアソン分布作成
```python
import numpy as np

data = np.random.poisson(2, 10000)
```

<div align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/36630026-99695a3e-19a2-11e8-96c7-f7d18b78013c.png">
</div>

### ポアソン分布の推定
実は、[scipyのコミュニティ](http://thread.gmane.org/gmane.comp.python.scientific.user/31752)を見ると、poissonの分布の実装が議論され、見送られたという背景がありそうで、よく読んでいくと、poissonは連続値でなくて離散値だからとかで、この辺は私も悩むところなので、まあしょうがないのかなと

ではどうするのかというと、無理くりですが、離散値であるパラメータを未知の状態にして、curve_fitを行うことで求めることができます　　
```python
# set bin middle
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1])

# フィットに用いる関数をを設定することができるので、
# poassonを書く未知をパラメータ未知のママ扱う
def poisson(k, lamb):
  return (lamb**k/factorial(k)) * np.exp(-lamb)

# fit with curve_fit
# paramtersでポアソン分布のパラメータ(lamb,)が出る
parameters, cov_matrix = curve_fit(poisson, bin_middles, entries)
print(parameters, cov_matrix)
```
結果
```console
$ python3 poisson-fit.py
[2.02988975] [[9.1122801e-05]]
```
