# 1. Two Sum

## Step 1
- 二重ループじゃ良くないなと思いつつ総当たりしか思いつきませんでした。
- 計算量はO(n^2)。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

        return []
```

## Step 2
- dictに今まで見た数とそのインデックスを登録しながら、新しい数に対して
欲しい差分がdictにないかチェックしていく。
- 線形探索で舐めていき、差分の確認はハッシュマップの確認で基本O(1)なので
トータルはO(n)。
- チェイン法のハッシュマップはハッシュ値 mod 配列長が等しいと
そこでリストを作る（アルゴリズム図鑑）のでO(1)とは限らないらしい。
そのうちPythonの辞書の実装を見てみたい。
- enumurate()を初めて知る。
- エラーケースに自分は空リストを返していたが、先達にあった
raise ValueErrorのほうがベターだと思い変更。

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[num] = i

        raise ValueError("can't find the solution")
```

## Step 3
- Step 2のコードを三回再現。
- num_to_indexがnum_to_idxになったくらいだった。
