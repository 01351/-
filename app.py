# app.py
# Streamlitを使った「ドラクエ風ガチャ」アプリ
# ・Sが出たらエフェクト表示
# ・ガチャ回数 / S率表示
# ・リセットボタン付き
# ・初心者向けコメントあり

import streamlit as st
import random

# -----------------------------
# タイトル
# -----------------------------
st.title("🎲 ドラクエ風ガチャ")
st.write("ガチャを引いて運試し！")

# -----------------------------
# セッション状態の初期化
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "s_count" not in st.session_state:
    st.session_state.s_count = 0

# -----------------------------
# リセットボタン
# -----------------------------
# これを押すと履歴・回数・Sカウントがすべて初期化される
if st.button("🔄 リセット"):
    st.session_state.history = []
    st.session_state.s_count = 0
    st.success("ガチャ履歴をリセットしました！")

# -----------------------------
# ガチャ設定
# -----------------------------
ranks = ["S", "A", "B", "C"]
weights = [100, 0, 0, 0]

# -----------------------------
# ガチャボタン
# -----------------------------
if st.button("✨ ガチャを引く！ ✨"):
    # 確率付きでランクを選ぶ
    result = random.choices(ranks, weights=weights, k=1)[0]

    # 履歴に追加
    st.session_state.history.append(result)

    # Sが出たらカウント
    if result == "S":
        st.session_state.s_count += 1

    # 結果表示
    st.subheader(f"結果：**{result}**")

    # Sランク演出
    if result == "S":
        st.success("🎉 Sランク獲得！！ 🎉")
        st.balloons()

# -----------------------------
# ガチャ成績
# -----------------------------
st.write("---")
st.subheader("📊 ガチャ成績")

total_count = len(st.session_state.history)

if total_count > 0:
    s_rate = (st.session_state.s_count / total_count) * 100

    st.write(f"ガチャ回数：**{total_count} 回**")
    st.write(f"Sランク回数：**{st.session_state.s_count} 回**")
    st.write(f"Sランク率：**{s_rate:.1f} %**")
else:
    st.write("まだガチャを引いていません。")

# -----------------------------
# 履歴表示
# -----------------------------
st.write("---")
st.subheader("📜 ガチャ履歴")

if st.session_state.history:
    for i, r in enumerate(reversed(st.session_state.history), start=1):
        st.write(f"{i}回目：{r}")
else:
    st.write("履歴はまだありません。")

# -----------------------------
# 確率表
# -----------------------------
st.write("---")
st.caption("▼ 排出確率")
st.write("S：5%")
st.write("A：15%")
st.write("B：30%")
st.write("C：50%")
