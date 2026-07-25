# 929. Unique Email Addresses

- localname@domainnameのメールアドレスが与えられる。
- **localname**について、
	- ピリオド（'.'）が含まれるなら、含まれていないアドレスと同じアドレスと認識される。
	- ex. "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
	- プラス（'+'）が含まれるなら、プラス以降の文字列がないアドレスと同じアドレスと認識される。
	- "m.y+name@email.com" will be forwarded to "my@email.com".
- メールアドレスのリストが与えられたとき、実際にメールを受け取る（ユニークと認識される）アドレスの数を返せ。


## Step1
1. リストを回しながら、各アドレス@でsplit
2. localnameを走査して、ドットがあったら無視、プラスがあったらbreakしながらアップデートしたアドレスをつくる。
3. それらをsetに放り込んで、その長さを返せば良さそう。

```python
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            email = email.split('@')
            local = email[0]
            domain = email[1]

            parsed_email = []
            for c in local:
                if c == '.':
                    continue
                elif c == '+':
                    break
                else:
                    parsed_email.append(c)
            parsed_email.extend(domain)
            unique_emails.add(tuple(parsed_email))

        return len(unique_emails)
```

- set()にlistを渡そうとしたらunhashableと怒られて、tuple()にした。勉強になった。
- 時間計算量はリストの入力をN、文字列の長さをMとしてO(NM)、空間計算量は再生成分でO(n)。リストもアドレスもlength <= 100なので特に問題なさそう。


## Step2
### AI
- split()はアンパックにすべき。
```python
email = email.split('@')
local = email[0]
domain = email[1]
↓
local, domain = email.split('@')
```
- `elif`, `else`は不要。
    `continue`, `break`でそのループを抜けるから。
- タプル変換と文字列連結で処理量は同じなので、データ型も文字列に合わせたほうがよい。
    文字列連結を絶対悪だと思っていたが、たしかに今回は`+=`による再生成ではなく、素直につなぐほうが見やすそう。
```python
parsed_email.extend(domain)
unique_emails.add(tuple(parsed_email))
↓
parsed_local = ''.join(parsed_local)
unique_emails.add(parsed_local + '@' + domain)
```

### 先達
- [ユースケースの想定](https://discord.com/channels/1084280443945353267/1251052599294296114/1254245440690589787)
    - この次元では考えられていなかった。
    - 今回の自分のコードはエラーを吐いていないので（結果として）サービス向け、[データサイエンスならそうでもない](https://discord.com/channels/1084280443945353267/1355903616032178327/1370028729186910269)
    - 同じような話として、今回は'@'がひとつと保証されているけれど、実際の使用を想定するなら`split('@', 1)`にしたほうがよさそう

- [正規表現](https://github.com/X-XsleepZzz/leetcode/pull/15/changes)
    ```python
    plus_ignored_local_name = re.sub(r"\+.*", "", local_name)
            dot_removed_local_name = re.sub(r"\.", "", plus_ignored_local_name)

            normalized_set.add(f"{dot_removed_local_name}@{domain_name}")
    ```
    - 正規表現を知っていれば処理内容を追いやすいかも？

### ブラッシュアップ
```python
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@', 1)

            parsed_local = []
            for c in local:
                if c == ".":
                    continue
                if c == "+":
                    break
                parsed_local.append(c)
            parsed_local = "".join(parsed_local)
            unique_emails.add(parsed_local + '@' + domain)

        return len(unique_emails)
```

## Step3
上記コードを三回再現。
