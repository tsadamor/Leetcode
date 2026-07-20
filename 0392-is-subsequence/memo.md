# 392. Is Subsequence

## Step1
- ふたつのstr、sとtが与えられて、tのなかにsの各文字が順番通り入っていればtrueを返す。
- sをインデックスi、tを走査して、
    - s[i] == t[j]なら両方進める
    - != ならtだけ進める
- tを走査し終わったとき(len(t) == j)、sも最後まで走査が進んでいれば(len(s) == i)、OK。

- 二重ループではなく、単にふたつのループが並走するので時間計算量はO(n)。
- 条件`0 <= t.length <= 10^4`を満たすには十分。
- 空間計算量は、インデックスの保持だけなので、O(1)。

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False
```


## Step2
- returnは`return i==len(s)`でよさそう。
- よく言及されているsやtの長さが0のときの早期リターンは、明示的ではあるものの、ループの条件ですぐ弾けるので不要かと思う。
- `if len(s) > len(t):
            return False`
    (https://github.com/kazuki-official/leetcode/blob/392-is-subsequence/memo.md)はやる価値があるか。ただここで削れるのも高々100ステップなので必須とはいえないかと思う。
- `s_index`, `t_index`という変数名も多かったが、`i`, `j`もループがふたつのときにおけるインデックスとしてメジャーだと考える。
- 正規表現でも書ける（https://github.com/lightbanana/leetcode/pull/3/changes）。やってることがわかりやすいので割と好き。
    ```python
    import re

    class Solution:
        def isSubsequence(self, s: str, t: str) -> bool:
            pattern = ""
            for c in s:
                pattern += ".*" + c #任意の連続しうる文字をsの構成文字の間に挟む

            Match = re.match(pattern, t)
            return True if Match else False
    ```
    - ただnodchipさんがコメントしている通り、Pythonでは文字列の+=で再構築が走るので避けたほうがよい。
- 変更点はreturn文くらいとした。
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
```

## Step3
- 上記コードを三回再現。