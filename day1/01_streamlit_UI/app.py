import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# 言語設定
# ============================================
if "lang" not in st.session_state:
    st.session_state["lang"] = "ja"

# 言語切り替え機能実装
st.sidebar.markdown("## 🌐 言語切り替え")
lang_option = st.sidebar.radio("Language", ["日本語", "English", "中文"], horizontal=True)

lang_map = {
    "日本語": "ja",
    "English": "en",
    "中文": "zh"
}

st.session_state["lang"] = lang_map[lang_option]
lang = st.session_state["lang"]

# 言語別テキスト辞書
TEXTS = {
    "ja": {
        "title": "Streamlit 初心者向けデモ",
        "desc1": "### コメントを解除しながらStreamlitの機能を学びましょう",
        "desc2": "このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。",
        "sidebar_header": "デモのガイド",
        "sidebar_info": "コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。",
        "ui_section": "基本的なUI要素",
        "text_input": "あなたの名前",
        "greeting": "こんにちは、{name}さん！",
        "usage_subheader": "このデモの使い方",
        "usage_steps": """
1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
2. 確認したい機能のコメントを解除します（先頭の#を削除）
3. 変更を保存して、ブラウザで結果を確認します
4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
""",
        "code_example": "コメントアウトされた例: \n# if st.button('クリックしてください'): \n#     st.success('ボタンがクリックされました！')\n\nコメントを解除した例:\nif st.button('クリックしてください'):\n    st.success('ボタンがクリックされました！')"
    },
    "en": {
        "title": "Streamlit Beginner Demo",
        "desc1": "### Learn Streamlit features by uncommenting sections",
        "desc2": "In this demo, you can observe UI changes by gradually uncommenting the code.",
        "sidebar_header": "Demo Guide",
        "sidebar_info": "Uncomment the code to explore various Streamlit features.",
        "ui_section": "Basic UI Elements",
        "text_input": "Your name",
        "greeting": "Hello, {name}!",
        "usage_subheader": "How to use this demo",
        "usage_steps": """
1. Find the commented-out sections in the code editor (lines starting with #).
2. Uncomment the feature you want to try (remove the leading #).
3. Save the changes and check the result in your browser.
4. Try various combinations and see how the UI changes.
""",
        "code_example": "Example of a commented-out code:\n# if st.button('Click me'):\n#     st.success('Button was clicked!')\n\nExample after uncommenting:\nif st.button('Click me'):\n    st.success('Button was clicked!')"
    },
    "zh": {
        "title": "Streamlit 新手演示",
        "desc1": "### 通过取消注释学习 Streamlit 功能",
        "desc2": "在这个演示中，可以逐步取消注释来查看 UI 的变化。",
        "sidebar_header": "演示指南",
        "sidebar_info": "取消代码注释以探索各种 Streamlit 功能。",
        "ui_section": "基本 UI 元素",
        "text_input": "你的名字",
        "greeting": "你好，{name}！",
        "usage_subheader": "如何使用这个演示",
        "usage_steps": """
1. 在代码编辑器中找到注释掉的部分（以#开头的行）。
2. 取消你想尝试的功能的注释（删除前面的#）。
3. 保存更改并在浏览器中查看结果。
4. 尝试不同的组合，看看UI如何变化。
""",
        "code_example": "注释掉的代码示例：\n# if st.button('点击我'):\n#     st.success('按钮被点击！')\n\n取消注释后的示例：\nif st.button('点击我'):\n    st.success('按钮被点击！')"
    }
}

t = TEXTS[lang]


# ============================================
# タイトルと説明
# ============================================
st.title(t["title"])
st.markdown(t["desc1"])
st.markdown(t["desc2"])

# ============================================
# サイドバー 
# ============================================
st.sidebar.header(t["sidebar_header"])
st.sidebar.info(t["sidebar_info"])

# ============================================
# 基本的なUI要素
# ============================================
st.header(t["ui_section"])

# テキスト入力
st.subheader(t["text_input"])
name = st.text_input(t["text_input"], "ゲスト")
st.write(t["greeting"].format(name=name))

# ============================================
# デモの使用方法
# ============================================
st.divider()
st.subheader(t["usage_subheader"])
st.markdown(t["usage_steps"])

st.code(t["code_example"])

# ============================================
# 基本的なUI要素
# ============================================
# st.header("基本的なUI要素")

# # テキスト入力
# st.subheader("テキスト入力")
# name = st.text_input("あなたの名前", "ゲスト")
# st.write(f"こんにちは、{name}さん！")

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
# st.title("Streamlit 初心者向けデモ")
# st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")
# st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")

# ============================================
# サイドバー 
# ============================================
# st.sidebar.header("デモのガイド")
# st.sidebar.info("コードのコメントを解除して、Streamlitのさまざまな機能を確認しましょう。")

# ボタン
# st.subheader("ボタン")
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")

# チェックボックス
# st.subheader("チェックボックス")
# if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
#     st.info("これは隠れたコンテンツです！")

# スライダー
# st.subheader("スライダー")
# age = st.slider("年齢", 0, 100, 25)
# st.write(f"あなたの年齢: {age}")

# セレクトボックス
# st.subheader("セレクトボックス")
# option = st.selectbox(
#     "好きなプログラミング言語は?",
#     ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
# )
# st.write(f"あなたは{option}を選びました")

# ============================================
# レイアウト
# ============================================
# st.header("レイアウト")

# カラム
# st.subheader("カラムレイアウト")
# col1, col2 = st.columns(2)
# with col1:
#     st.write("これは左カラムです")
#     st.number_input("数値を入力", value=10)
# with col2:
#     st.write("これは右カラムです")
#     st.metric("メトリクス", "42", "2%")

# タブ
# st.subheader("タブ")
# tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
# with tab1:
#     st.write("これは第1タブの内容です")
# with tab2:
#     st.write("これは第2タブの内容です")

# エクスパンダー
# st.subheader("エクスパンダー")
# with st.expander("詳細を表示"):
#     st.write("これはエクスパンダー内の隠れたコンテンツです")
#     st.code("print('Hello, Streamlit！')")

# ============================================
# データ表示
# ============================================
# st.header("データの表示")

# サンプルデータフレームを作成
# df = pd.DataFrame({
#     '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
#     '年齢': [25, 30, 22, 28, 33],
#     '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']
# })

# データフレーム表示
# st.subheader("データフレーム")
# st.dataframe(df, use_container_width=True)

# テーブル表示
# st.subheader("テーブル")
# st.table(df)

# メトリクス表示
# st.subheader("メトリクス")
# col1, col2, col3 = st.columns(3)
# col1.metric("温度", "23°C", "1.5°C")
# col2.metric("湿度", "45%", "-5%")
# col3.metric("気圧", "1013hPa", "0.1hPa")

# ============================================
# グラフ表示
# ============================================
# st.header("グラフの表示")

# ラインチャート
# st.subheader("ラインチャート")
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['A', 'B', 'C'])
# st.line_chart(chart_data)

# バーチャート
# st.subheader("バーチャート")
# chart_data = pd.DataFrame({
#     'カテゴリ': ['A', 'B', 'C', 'D'],
#     '値': [10, 25, 15, 30]
# }).set_index('カテゴリ')
# st.bar_chart(chart_data)

# ============================================
# インタラクティブ機能
# ============================================
# st.header("インタラクティブ機能")

# プログレスバー
# st.subheader("プログレスバー")
# progress = st.progress(0)
# if st.button("進捗をシミュレート"):
#     for i in range(101):
#         time.sleep(0.01)
#         progress.progress(i / 100)
#     st.balloons()

# ファイルアップロード
# st.subheader("ファイルアップロード")
# uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
# if uploaded_file is not None:
#     # ファイルのデータを表示
#     bytes_data = uploaded_file.getvalue()
#     st.write(f"ファイルサイズ: {len(bytes_data)} bytes")
#     
#     # CSVの場合はデータフレームとして読み込む
#     if uploaded_file.name.endswith('.csv'):
#         df = pd.read_csv(uploaded_file)
#         st.write("CSVデータのプレビュー:")
#         st.dataframe(df.head())

# ============================================
# カスタマイズ
# ============================================
# st.header("スタイルのカスタマイズ")

# カスタムCSS
# st.markdown("""
# <style>
# .big-font {
#     font-size:20px ！important;
#     font-weight: bold;
#     color: #0066cc;
# }
# </style>
# """, unsafe_allow_html=True)
# 
# st.markdown('<p class="big-font">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)

# ============================================
# デモの使用方法
# ============================================
# st.divider()
# st.subheader("このデモの使い方")
# st.markdown("""
# 1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
# 2. 確認したい機能のコメントを解除します（先頭の#を削除）
# 3. 変更を保存して、ブラウザで結果を確認します
# 4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
# """)

# st.code("""
# # コメントアウトされた例:
# # if st.button("クリックしてください"):
# #     st.success("ボタンがクリックされました！")

# # コメントを解除した例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")
# """)