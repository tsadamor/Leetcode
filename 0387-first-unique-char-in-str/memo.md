# 387. First Unique Character in a String

## Step 1
- 一回文字列を頭から舐めて文字：出現数で辞書に登録
- もう一度文字列を走査して、出現数が１の文字のインデックス（かなければ-1）を返す
- 時間、空間ともにO(n)
- 入力が<= 10^5であることを考えるとPythonでも0.1秒収まるくらい？（平均的な処理能力を10^8/sec、Pythonがそこから最悪100倍で見積もっています、初めてなので勘違いしている点やリファレンスがあればコメントください）

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        appearences: dict[str, int] = {}
        
        for c in s:
            if c in appearences:
                appearences[c] += 1
            else:
                appearences[c] = 1
                
        for c in s:
            if appearences[c] == 1:
                return s.index(c)
        
        return -1
```

## Step 2
- enumerate()を使っている人が多かった。str.index()は文字列を走査し直す（当然でした）のでここで最悪O(n^2)になっている。
- collections.Counter()という便利なやつがいる。
```python
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        appearences = Counter(s)
        
        for i, c in enumerate(s):
             if appearences[c] == 1:
                 return i
        
        return -1
```

- OrderDictという要素の順番を保持してくれるものがある。辞書の値に出現回数ではなく最初に見つけたインデックスを保存し、二回目以降の出現があればそれを潰しておく。二回目のループのとき、辞書は文字列に登場した順番通りになっているので、潰れていないインデックスが出た瞬間それを返して問題ない。
- Python3.7以降ふつうのdictも追加順を保持しているらしく(Dictionaries preserve insertion order.(https://docs.python.org/3/library/stdtypes.html#mapping-types-dict))、そのままdictで実装した。OrderDictをインポートしたほうがいいんでしょうか？
- 2回目のループが最長26回で済むのでだいぶ効率的。

```python
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        seen_index:dict[str, int] = {}
        duplicated = -1

        for i, c in enumerate(s):
            if c in seen_index:
                seen_index[c] = duplicated
            else:
                seen_index[c] = i

        for idx in seen_index.values():
            if idx != duplicated:
                return idx

        return -1  
```

## Step 3
- OrderDictのほうが効率的かつ明示的だと思ったのでそちらで三回実装。