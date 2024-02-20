yyyy = "1990"
mm = "11"
dd = "17"

first_name = "takaaki"
last_name = "ohtomo"

# yyyy = input("yyyy=")
# mm = input("mm=")
# dd = input("dd=")

# first_name = input("first name ? ")
# last_name = input("last name ? ")

data_base = {1:"はじまり。独立。革新。リーダーシップ。男性原理。",
2:"調和。結合。人間関係。協力。女性原理。",
3:"真実を語る。イマジネーション。楽観主義。陽気。クリエイティヴな表現。",
4:"建設する。形づくる。ハード・ワーク。持久力。まじめ。実際的。",
5:"変化。移行。進歩的な考え。機知に富む。自由。多才。増進。",
6:"バランス。育てる。奉仕。責任と義務。家族の力。結婚と別れの数。家庭と仕事の問題。",
7:"分析。リサーチ。科学。テクノロジー。孤独。叡智。スピリチュアルな力。調査。神秘主義的。形而上学的。",
8:"権威。力。財力。ビジネス。成功。物質的価値。組織。自己制御。",
9:"終わり。ヴィジョン。寛大。変容。スピリチュアルな意識。宇宙。教え。全体性意識。完全性。"}

letter_to_number = {chr(j):str((i+1)%9) for i,j in enumerate(range(97, 123))}

def name_to_number(name):
    a = [letter_to_number[l] for l in name]
    return int("".join(a))

def mod_9(name_to_number):
    if name_to_number%9 == 0:
        return 9
    else
        return name_to_number%9


# ライフ・パス・ナンバー
print("ライフ・パス・ナンバーは、日本語に訳すと「人生の道の数」となりますが、自分自身が人生をどのような道を通って歩んでいくかを表すとされています。したがって、たとえば独力で人生を切り開いていくべきなのか、それとも他者とパートナーシップを組むことが大切なのか、あるいは目標に向かってひとつひとつ基礎を積み上げていくタイプなのか、といったようなことがそれぞれの数から導き出されます。")
life_path_number = int(yyyy+mm+dd)%9
print(f"life path number is {life_path_number}")
print(data_base[life_path_number])

# ディスティニー・ナンバー
print("ディスティニー・ナンバーは、これも日本語に訳すと「運命の数」となりますが、今生での自分の人生にはどんな目的があり、自分は生まれながらにどんな使命を与えられているのかといったことを表すとされています。したがって、たとえば自分にはクリエイティヴな活動を通して自己表現をおこなっていくことが必要なのか、それとも誰もがまだ足を踏み入れていない未知のことを切り開いていく使命を持っているのか、といったようなことがそれぞれの数から導き出されます。")
name = (first_name + last_name).lower()

destiny_number = name_to_number(name)%9
print(f"destiny number is {destiny_number}")
print(data_base[destiny_number])

# ソウル・ナンバー
print("ソウル・ナンバーは、人生のなかで自分が本当に求めていることはなんなのかを表す数だとされています。これは普段自分が意識している自分の欲求よりも、より深い根源的なレベルで求めているものを意味します。ですから、普段の生活でどこかしら満たされない何かを感じているのなら、自分が本当に求めているものはそれとは異なる別のなにかかもしれないことを、この数は教えてくれることになります。")
soul_name = ""
personality_name = ""
for l in name:
    if l in ["a","e","i","o","u"]:
        soul_name += l
    else:
        personality_name += l
print(soul_name)
print(personality_name)

soul_number = name_to_number(soul_name)%9

print(f"soul number is {soul_number}")
print(data_base[soul_number])

# パーソナリティー・ナンバー
print("パーソナリティー・ナンバーは、ソウル・ナンバーのようなその人の内奥にあるものとは異なり、普段の人間関係のなかで形作られていくその人の性格や傾向を表します。それはソウル・ナンバーのように、秘められたなにかを表すものではありませんが、日常生活において、他者と関係していくなかで自分が学んでいくべき大切なことがなにかを教えてくれます。")

personality_number = name_to_number(personality_name)%9

print(f"personality_number is {personality_number}")
print(data_base[personality_number])