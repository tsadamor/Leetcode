# 283. Move Zeroes
- 受け取ったint配列のなかのすべてのゼロを配列の後ろに移動させる。
- 非ゼロの数はそのままの順番を保つ。また、配列のコピーなどはつくらずin-placeでやること。

## Step1

- 手作業で考える
	- 大人と子供がランダムに並んでいて、大人たちを後ろにやりたい＝子どもたちを前にやりたい。子供の順番は保ったまま。
	- 列の左右に担当者AとBを置いて、
		- Aは先頭から普通にひとりずつ進んでいく。Bは最初、先頭で止まっておく。
		- Aが子供を見つけたら、Bの位置の人とスワップしてもらう。スワップしたときだけBもひとりぶん進む。
	- Bはそれまで確定させた子供たちの次の位置に常にいるようになるはず。
	- 大人が続くほどAとBの間が開いていくイメージ。

- 失敗
```python
class Solution:
	def moveZeroes(self, nums: list[int]) -> None:
		end_of_nonzeroes = 0
		
		for num in nums:
			if num != 0:
				tmp = nums[end_of_nonzeroes]
				nums[end_of_nonzeroes] = num
				num = tmp
				end_of_nonzeroes += 1
```
	
- for num in nums: の num は、配列の要素のコピー（要素への参照を受け取ったローカル変数）であって、配列の場所そのものではない
- num = xとしても、ループの中で捨てられていくローカル変数に代入しているだけ。
- この時点では動かないのでwhileにしようという意識でつぎへ。


```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        end_of_nonzeroes = 0

        while i < len(nums):
            if nums[i] != 0:
                tmp = nums[end_of_nonzeroes]
                nums[end_of_nonzeroes] = nums[i]
                nums[i] = tmp
                
                end_of_nonzeroes += 1
            i += 1
```

- 計算量
	- 時間O(n)
	- 空間O(1) ∵インデックスとtmpの保持のみ


## Step2
- AI
	- > whileよりforのほうがよい
		
		最初にforで動かなかった＋42で初期はfor禁止だった。
		失敗の原因はわかり、特にこだわることもないので、forを使う。
	- > swapにtmpは不要
		
		`nums[end_of_nonzeroes], nums[i] = nums[i], nums[end_of_nonzeroes]`Pythonではこちらが定番。Cの学習内容で書いたtmpだったので以後改善する。
	- > Two Pointerが同じ場所を指すときswapは不要
		
		インデントが一段深くなるけれど、最適化と明示化のために悪くないと思った。ただ、スワップが減るぶん、`if i != end_of_nonzeroes`の比較が毎回走る。そこまでは変わらないんじゃないか。

- [先人１](https://github.com/Manato110/LeetCode-arai60/pull/55/changes)
	- `in-place`とは、
	> 引数で受け取ったオブジェクトに対して変更を加えて目的を達成すること
	
	> in-placeではない場合は、引数で受けとったものは不変で、返り値として値を返すことで目的を達成
	
	> それに加えて空間計算量が入力サイズに比例しないこと

	べつで配列を用意したりしてはいけないものだと思っていた。正直最初は非ゼロをべつに避けて、もとの配列の頭にそれを詰める＋もとの長さマイナス詰めたぶんのゼロで埋める、がぱっと浮かんだのだけれど、それはin-placeではないかと思い捨てた。ただ、それだと空間計算量がO(n)になるので最後の条件でアウトか。

	- せっかくなので書いてみる（Step１でやるべきことでしたが）
	```python
	class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zeroes = []

        for num in nums:
            if num != 0:
                non_zeroes.append(num)

        i = 0
        for non_zero in non_zeroes:
            nums[i] = non_zero
            i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1
	```
	- 空間計算量はTwo Pointers方式とLeetcode上では変わらなかった、なぜだろう？あまり信頼できない指標とは聞くが...

- [先人２](https://github.com/fhiyo/leetcode/pull/54/changes/BASE..40f6172e4c7a6b29303a6b66464dd512300ac477#diff-2f8b85074aa38861aa9dd6fbe0c5f1b540a06f8618d7552b4ffd05da21f795d3R138)
	- `if nums[i] == 0: continue`で弾いてしまえば、本処理のインデントを一段浅くできる。


- ブラッシュアップ
```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        end_of_nonzeroes = 0

        for i, num in enumerate(nums):
            if num == 0:
                continue

            nums[end_of_nonzeroes], nums[i] = nums[i], nums[end_of_nonzeroes]
            end_of_nonzeroes += 1
```

## Step3
- 上記ブラッシュアップのコードを三回再現。