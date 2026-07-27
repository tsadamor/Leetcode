# 349. Intersection of Two Arrays

- ふたつのint配列が与えられる。積集合のリストを返せ。順番の制限はない。
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 1000


## Step 1
### 解法１
- ふたつの配列をsetにしてループで回せばすぐ終わりそう。
- 時間計算量は、nums1の走査でO(n)、nums2へのin判定はsetがハッシュ化されていることからmにつきO(1)で、O(n + m)。
- 空間計算量はセットやリストの確保分でO(n + m)。
```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        res = []
        for num in nums1_set:
            if num in nums2_set:
                res.append(num)

        return res
```
- Leetcodeのruntimeは0msになっていて、ほんとうにこれ信用できない代物だなあという感を新たにする。

### 解法２
- nums1を走査して出てきたものを辞書に{文字: 1}として登録。
- nums2を走査して、バリューが１の文字を結果にアペンド。同時にインクリメントして被りを防ぐ。
- 解法１に比べると、空間計算量がO(n)になる点が優れている。
```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_seen = {}
        res = []

        for num in nums1:
            num_to_seen[num] = 1

        for num in nums2:
            if num_to_seen.get(num) == 1:
                res.append(num)
                num_to_seen[num] += 1

        return res
```


## Step2
### AI
- `set1 & set2`か、`set1.intersection(set2)`で積集合が求められる。
- `return list(set(nums1) & set(nums2))`で終わる。
- `&`は初めて知った。`intersection()`は前勉強したのに忘れていたので反省。
- `a | b`か`a.union(b)`で和集合、`a - b`か`a.difference(b)`で差集合、`a ^ b`か`a.symmetric_difference(b)`で対称差（どちらか一方にだけあるもの）。
- 包含関係も表せる。`a <= b`か`a.issubset(b)`で部分集合、`a >= b`か`a.issuperset(b)`で上位集合、`a.isdisjoint(b)`で共通要素の判定。(https://docs.python.org/3/library/stdtypes.html#set.issuperset)

### コメント集
- https://github.com/quinn-sasha/leetcode/pull/13#discussion_r1960884543
    > この問題は問題文自体では終わっていなくて、解けた後に、いくつか追加の条件が出てきて、その下でのアルゴリズムとそれらの pros and cons が要求されると思います。
- たしかにこの問題は（Pythonだと）瞬殺なので、プラスアルファの学びにしたい。

- たとえば入力がソート済みなら、TwoPointersによるマージソートみたいなことをすると空間計算量がO(1)で済み（時間はO(n + m)のまま）、集合を作るやり方より優れている。
```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 入力がソート済みと仮定したいのでここでソート
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not res or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res
```

## Step3
`return list(set(nums1) & set(nums2))`は三回書くまでもないかと思い、上記Two Pointersのやり方で三回再現。