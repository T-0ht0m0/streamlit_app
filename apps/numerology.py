import datetime
import streamlit as st


letter_to_number = {chr(j):str((i+1)%9) for i,j in enumerate(range(97, 123))}

data_base = {1:"はじまり。独立。革新。リーダーシップ。男性原理。",
2:"調和。結合。人間関係。協力。女性原理。",
3:"真実を語る。イマジネーション。楽観主義。陽気。クリエイティヴな表現。",
4:"建設する。形づくる。ハード・ワーク。持久力。まじめ。実際的。",
5:"変化。移行。進歩的な考え。機知に富む。自由。多才。増進。",
6:"バランス。育てる。奉仕。責任と義務。家族の力。結婚と別れの数。家庭と仕事の問題。",
7:"分析。リサーチ。科学。テクノロジー。孤独。叡智。スピリチュアルな力。調査。神秘主義的。形而上学的。",
8:"権威。力。財力。ビジネス。成功。物質的価値。組織。自己制御。",
9:"終わり。ヴィジョン。寛大。変容。スピリチュアルな意識。宇宙。教え。全体性意識。完全性。"}


def name_to_number(name):
    a = [letter_to_number[l] for l in name]
    return int("".join(a))

def mod_9(number):
    if number%9 == 0:
        return 9
    else:
        return number%9


def app():
    min_date = datetime.date(1900, 1, 1)
    max_date = datetime.date(2100, 12, 31)
    d = st.date_input("When's your birthday",datetime.date(1990, 1, 1), min_value=min_date, max_value=max_date)
    st.write('Your birthday is:', d)

    first_name = st.text_input('first name', 'taro')
    last_name = st.text_input('last name', 'yamada')
    st.write('Your name is ', first_name, last_name)

    yyyymmdd = str(d).replace("-","")
    name = (first_name + last_name).lower()

    soul_name = ""
    personality_name = ""
    for l in name:
        if l in ["a","e","i","o","u"]:
            soul_name += l
        else:
            personality_name += l



    if st.button(label='click me!'):
    
        st.subheader("ライフ・パス・ナンバー")

        st.write("ライフ・パス・ナンバーは、日本語に訳すと「人生の道の数」となりますが、自分自身が人生をどのような道を通って歩んでいくかを表すとされています。したがって、たとえば独力で人生を切り開いていくべきなのか、それとも他者とパートナーシップを組むことが大切なのか、あるいは目標に向かってひとつひとつ基礎を積み上げていくタイプなのか、といったようなことがそれぞれの数から導き出されます。")

        life_path_number = mod_9(int(yyyymmdd))
        st.write(f"あなたのライフ・パス・ナンバーは {life_path_number}")
        st.write("数秘術的な意味: ",data_base[life_path_number])

        st.subheader("ディスティニー・ナンバー")

        st.write("ディスティニー・ナンバーは、これも日本語に訳すと「運命の数」となりますが、今生での自分の人生にはどんな目的があり、自分は生まれながらにどんな使命を与えられているのかといったことを表すとされています。したがって、たとえば自分にはクリエイティヴな活動を通して自己表現をおこなっていくことが必要なのか、それとも誰もがまだ足を踏み入れていない未知のことを切り開いていく使命を持っているのか、といったようなことがそれぞれの数から導き出されます。")

        destiny_number = mod_9(name_to_number(name))
        st.write(f"あなたのディスティニー・ナンバーは {destiny_number}")
        st.write("数秘術的な意味: ",data_base[destiny_number])


        st.subheader("ソウル・ナンバー")

        st.write("ソウル・ナンバーは、人生のなかで自分が本当に求めていることはなんなのかを表す数だとされています。これは普段自分が意識している自分の欲求よりも、より深い根源的なレベルで求めているものを意味します。ですから、普段の生活でどこかしら満たされない何かを感じているのなら、自分が本当に求めているものはそれとは異なる別のなにかかもしれないことを、この数は教えてくれることになります。")

        soul_number = mod_9(name_to_number(soul_name))
        st.write(f"あなたのソウル・ナンバーは {soul_number}")
        st.write("数秘術的な意味: ",data_base[soul_number])


        st.subheader("パーソナリティー・ナンバー")

        st.write("パーソナリティー・ナンバーは、ソウル・ナンバーのようなその人の内奥にあるものとは異なり、普段の人間関係のなかで形作られていくその人の性格や傾向を表します。それはソウル・ナンバーのように、秘められたなにかを表すものではありませんが、日常生活において、他者と関係していくなかで自分が学んでいくべき大切なことがなにかを教えてくれます。")

        personality_number = mod_9(name_to_number(personality_name))

        st.write(f"あなたのパーソナリティー・ナンバーは {personality_number}")
        st.write("数秘術的な意味: ",data_base[personality_number])



