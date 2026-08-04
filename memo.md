# 121. Best Time to Buy and Sell Stock

- `prices`というint配列が与えられ、`prices[i]`はi番目の日における株価である。
- 得られる最大の利益を返せ。必ず赤字になる場合は0を返せ。
- 入力: 
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4


## Step1
- 愚直に二重ループで購入と売却のすべての組み合わせを試せば、O(n^2) = 10^10ステップとなり、現実的なソリューションでない。
- 配列を一回舐めるだけにすればO(n)になる。そのために必要な（とっておくべき）情報は、
    - 現時点での利益。これがないと今売るべきかの判断基準がない。
    - 現時点での購入金額。それより安いものにあたったら、（現時点での利益は変えないまま）買い替え候補をアップデートすべき。

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        current_buy = prices[0]

        for price in prices[1:]:
            if price < current_buy:
                current_buy = price
            elif price - current_buy > profit:
                profit = price - current_buy

        return profit
```
- 線形探索になったので、時間計算量は`O(n)`、空間計算量は入力量にかかわらず`profit`と`current_buy`だけなのでO(1)。


## Step2
### AI
- `current_buy`は`min_price`のほうがよいのでは
- `profit`は`max_profit`のほうがよいのでは

### [秒での判断](https://github.com/rimokem/arai60/pull/37/changes#diff-08b43bf1aed8bb6b426efa399de6161b7e4ce5815cfae7387f1b32d8b3c88712)
- `if`での比較に対し`min`, `max`を呼ぶ方法は関数呼び出しのオーバーヘッドがあるが、今回の問題設定などを考えると絶対視するほどのものではない、という議論。面白かった。
- 自分自身はそもそも`min`, `max`での実装方法を考えてもいなかったので、書いてみる。
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
```
- リンク先のコードは`min_price`を`float("inf")`で初期化していた。ダイクストラっぽくて面白いと思ったが、Step1で選んだ、最初の株を買うという意味で`prices[0]`を継続した。

### [`prices`の長さが0のとき](https://github.com/h-masder/Arai60/pull/40/changes#diff-f87426cc46e157af84f5177a8fd56c038a8cdeb24e723aa0aafaa096c23eec77R42-R49)
- たしかに今のコードでは`IndexError`になる。
- 問題の制約は`1 <= prices.length`なので0ではないことが保証されている。が、それを把握してエラーハンドリングを削ったわけでもない。エッジケースの想定が足りない。
- エラーを`raise`するより、`if len(prices) == 0: return 0`を追加すればいいだろう。
- それはそれとして、リンク先のコードはまったくべつの解法で驚いた。subarrayなるものは知らなかったので勉強になったが、計算量は現行のものと等しく、可読性は現行のもののほうが高いと感じられた。

### [後ろから見る](https://github.com/kazuki-official/leetcode/pull/37/changes)
- i日目以降の最大値を先に埋めておく方法。
- 前から見るやり方はストリートアルゴリズム（全データが揃っていなくても処理可能、入力を保存する必要がない）、後ろから見るやり方はバッチ型（全データを手元に置く、追加空間が必要）

### ブラッシュアップ
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
```

## Step3
上記コードを三回再現。
