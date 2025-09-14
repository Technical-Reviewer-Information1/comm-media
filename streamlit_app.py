import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import time

# Page configuration
st.set_page_config(
    page_title="コミュニケーションとメディア",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 20px 0;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 20px;
}

.step-container {
    border: 2px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
    background-color: #f8f9fa;
}

.message-box {
    background-color: #e3f2fd;
    border-left: 5px solid #2196f3;
    padding: 15px;
    margin: 10px 0;
    border-radius: 5px;
}

.sns-post {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.warning-box {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
}

.success-box {
    background-color: #d4edda;
    border: 1px solid #c3e6cb;
    border-radius: 5px;
    padding: 15px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Main title and captions
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("コミュニケーションとメディア（pp.201-202）")
st.caption("Created by Dit-Lab.(Daiki ITO)")
st.caption("Supported by Tomoaki ATSUMI")
st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1

if 'quiz_answered' not in st.session_state:
    st.session_state.quiz_answered = False

if 'fact_check_done' not in st.session_state:
    st.session_state.fact_check_done = False

# Navigation
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🚀 はじめに", key="step1"):
        st.session_state.step = 1
with col2:
    if st.button("📚 歴史の旅", key="step2"):
        st.session_state.step = 2
with col3:
    if st.button("💬 テキスト体験", key="step3"):
        st.session_state.step = 3
with col4:
    if st.button("🔍 ファクトチェック", key="step4"):
        st.session_state.step = 4
with col5:
    if st.button("🤖 AI体験", key="step5"):
        st.session_state.step = 5

st.markdown("---")

# Step 1: Introduction
if st.session_state.step == 1:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    
    st.header("🚀 ステップ1: はじめに - メッセージは時空を超える")
    
    st.subheader("コミュニケーションとメディアの世界へようこそ！")
    
    st.markdown("""
    私たちは、ニュースを見たり、友達とSNSで話したり、毎日たくさんのメディアに触れています。
    メディアは、人と人をつなぐ **「情報の乗り物」** のようなものです。
    
    この乗り物が、時代とともにどう進化してきたのか、一緒に旅をしてみましょう！
    """)
    
    # Interactive timeline
    timeline_data = pd.DataFrame({
        'Era': ['口コミ時代', '文字・印刷時代', 'ラジオ・テレビ時代', 'インターネット時代', 'SNS・AI時代'],
        'Year': [0, 1440, 1920, 1990, 2010],
        'Speed': [1, 10, 100, 1000, 10000],
        'Reach': [10, 1000, 100000, 1000000, 1000000000]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=timeline_data['Year'],
        y=timeline_data['Speed'],
        mode='markers+lines',
        name='情報伝達スピード',
        marker=dict(size=15, color='blue'),
        line=dict(width=3)
    ))
    
    fig.update_layout(
        title="メディアの進化：情報伝達スピードの変化",
        xaxis_title="年代",
        yaxis_title="相対的スピード",
        yaxis_type="log",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **ポイント**: 情報技術の進歩により、私たちのコミュニケーションは劇的に変化しました！")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Step 2: Media History Journey
elif st.session_state.step == 2:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    
    st.header("📚 ステップ2: メディアの歴史を旅しよう！ - 伝言ゲーム体験")
    
    st.subheader("昔の人はどう伝えた？メディアの変遷")
    st.markdown("もしあなたが「遠くの村でリンゴが豊作だ！」というニュースを伝えたいとしたら…？")
    
    tab1, tab2, tab3 = st.tabs(["🗣️ 口コミの時代", "📖 文字と印刷の時代", "📱 ネットとSNSの時代"])
    
    with tab1:
        st.subheader("口コミの時代")
        st.markdown("文字も電話もない時代。あなたのニュースは、人から人へと伝えられます。")
        
        # 伝言ゲーム体験
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="message-box">', unsafe_allow_html=True)
            st.markdown("**元の情報：**")
            st.markdown("「A村で、甘くて大きなリンゴが100個とれた」")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("伝言ゲームを見る", key="oral_game"):
                progress_bar = st.progress(0)
                message_placeholder = st.empty()
                
                messages = [
                    "「A村で、甘くて大きなリンゴが100個とれた」",
                    "「A村で、リンゴが100個とれたらしい」",
                    "「A村で、リンゴがたくさんとれたらしい」",
                    "「どこかの村で、リンゴがとれたって」",
                    "「B村で、スイカがとれたらしい…？」"
                ]
                
                for i, msg in enumerate(messages):
                    progress_bar.progress((i + 1) / len(messages))
                    message_placeholder.markdown(f"**{i+1}人目：** {msg}")
                    time.sleep(1)
        
        st.markdown("**解説：** 口コミ（口頭伝達）は、情報が変化しやすく、正確に遠くまで伝わりにくいという特徴がありました。")
    
    with tab2:
        st.subheader("文字と印刷の時代")
        st.markdown("文字が発明され、印刷技術が登場しました。")
        
        # Create a visualization of print media spread
        print_data = pd.DataFrame({
            'Year': [1440, 1500, 1600, 1700, 1800],
            'Books_Published': [1, 100, 1000, 5000, 20000],
            'Literacy_Rate': [5, 10, 20, 30, 50]
        })
        
        fig = px.line(print_data, x='Year', y='Books_Published', 
                     title='印刷技術の普及：出版された本の数')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("**解説：** 文字で記録することで、情報は正確に保存されるようになりました。さらに印刷によって、同じ情報を大量に、広く届けられるようになったのです。これは大きな革命でした。")
    
    with tab3:
        st.subheader("ネットとSNSの時代")
        st.markdown("そして現代。誰もが情報の発信者になれる時代です。")
        
        # SNS風の投稿表示
        st.markdown('<div class="sns-post">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("https://via.placeholder.com/50/4CAF50/FFFFFF?text=🍎", width=50)
        with col2:
            st.markdown("**リンゴ農家@A村** 🍎")
            st.markdown("今年のリンゴ、大豊作です！甘くて大きいのが100個とれました！写真を見てください！")
            st.markdown("#A村 #リンゴ")
            st.markdown("📷 [リンゴの写真]")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Social media metrics
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        with metrics_col1:
            st.metric("いいね", "127", "12")
        with metrics_col2:
            st.metric("リツイート", "34", "5")
        with metrics_col3:
            st.metric("コメント", "18", "3")
        
        st.info("**解説：** インターネットは、個人が写真や動画付きでリアルタイムに、世界中へ情報を発信できる双方向のメディアです。情報の量とスピードが爆発的に増えました。")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Step 3: Text Communication
elif st.session_state.step == 3:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    
    st.header("💬 ステップ3: テキストだけの会話、どう伝わる？")
    
    st.subheader("ネットの言葉のむずかしさ 🤔")
    st.markdown("友達からLINEでメッセージが来ました。あなたは相手がどんな気持ちだと思いますか？")
    
    # LINE風のメッセージ表示
    st.markdown('<div class="message-box">', unsafe_allow_html=True)
    st.markdown("**友達からのメッセージ：**")
    st.markdown("『じゃあ、それでいいよ。』")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ラジオボタンで選択
    feeling = st.radio(
        "相手の本当の気持ちはどれだと思う？",
        ["快くOKしてくれた！😊", "ちょっと怒ってるかも…😠", "特に何も考えていない。😐"],
        key="text_feeling"
    )
    
    if feeling:
        st.session_state.quiz_answered = True
        
        if not st.session_state.quiz_answered:
            st.write("")  # This won't execute due to the condition above
        else:
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.markdown("**解説：**")
            st.markdown("""
            そうですよね、判断に迷いませんか？
            
            テキストだけのコミュニケーションは、**表情や声のトーン（非言語情報）**が伝わらないため、
            意図が誤解されやすいという特徴があります。
            
            だからこそ、私たちは感情を補うために絵文字😊やスタンプを使うのですね！
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # 非言語コミュニケーションの重要性を可視化
    if st.session_state.quiz_answered:
        communication_data = pd.DataFrame({
            'Type': ['言語情報\n(話の内容)', '準言語情報\n(声のトーン)', '非言語情報\n(表情・身振り)'],
            'Percentage': [7, 38, 55],
            'Color': ['#ff9999', '#66b3ff', '#99ff99']
        })
        
        fig = px.pie(communication_data, values='Percentage', names='Type',
                     title='メラビアンの法則：コミュニケーションの構成要素',
                     color_discrete_sequence=['#ff9999', '#66b3ff', '#99ff99'])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 **ポイント**: 対面のコミュニケーションでは、言葉以外の情報が93%を占めます！")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Step 4: Fact Checking
elif st.session_state.step == 4:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    
    st.header("🔍 ステップ4: そのニュース、信じていい？ - ファクトチェック体験")
    
    st.subheader("情報の信頼性を見抜こう")
    st.markdown("SNSで、こんな投稿が流れてきました。あなたはこの情報をすぐに信じますか？")
    
    # SNS投稿風のカード
    st.markdown('<div class="sns-post">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://via.placeholder.com/50/FF5722/FFFFFF?text=🧅", width=50)
    with col2:
        st.markdown("**すごい健康ハック君** ✨")
        st.markdown("【超速報】専門家の研究で「タマネギの皮を枕元に置くと、快眠効果がある」ことが明らかに！今夜から試してみて！")
        st.markdown("👍 2.5万件のいいね")
    st.markdown('</div>', unsafe_allow_html=True)
    
    action = st.selectbox(
        "あなたならどうする？",
        ["すぐに友達に教える！", "ちょっと待って、調べてみる", "とりあえず「いいね」する"],
        key="fact_check_action"
    )
    
    if action:
        if action == "ちょっと待って、調べてみる":
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.markdown("**素晴らしい判断です！** 🎉")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-box">', unsafe_allow_html=True)
            st.markdown("**ちょっと待って！** ⚠️")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # ファクトチェックの方法を表示
        st.markdown("**ファクトチェックのポイント：**")
        
        checklist = st.columns(2)
        
        with checklist[0]:
            st.markdown("✅ **誰が言っているの？**")
            st.markdown("→ その「専門家」は実在する？")
            st.markdown("✅ **他の情報源は？**")
            st.markdown("→ 公的な機関や大手ニュースサイトも報じている？")
        
        with checklist[1]:
            st.markdown("✅ **証拠はある？**")
            st.markdown("→ 研究論文や公式発表はある？")
            st.markdown("✅ **いつの情報？**")
            st.markdown("→ 最新の情報？古い情報が再拡散？")
        
        # 情報の信頼性レーダーチャート
        if st.button("この投稿の信頼性を分析", key="analyze_post"):
            categories = ['情報源の信頼性', '証拠の有無', '専門性', '複数ソース確認', '時事性']
            values = [2, 1, 1, 1, 3]  # 低い信頼性を示すスコア
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=categories,
                fill='toself',
                name='この投稿の信頼性'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 5]
                    )
                ),
                title="情報の信頼性分析",
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            st.error("**結果：** この投稿は信頼性が低い情報です！複数の情報源を照らし合わせて事実を確認することをファクトチェックと言い、とても大切なスキルです。")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Step 5: AI Hallucination
elif st.session_state.step == 5:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    
    st.header("🤖 ステップ5: AIはウソをつく？ - ハルシネーションに注意！")
    
    st.subheader("AIとのコミュニケーション")
    st.markdown("話題の生成AIに、未来の質問をしてみましょう。")
    
    # AI質問のダミー
    question = st.text_input(
        "AIへの質問:",
        "2028年の夏季オリンピックはどこで開催されますか？",
        key="ai_question"
    )
    
    if st.button("AIに質問する", key="ask_ai"):
        # プログレスバーでAIが考えているような演出
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        
        # AI の偽の回答を表示
        st.markdown('<div class="message-box">', unsafe_allow_html=True)
        st.markdown("🤖 **AIの答え:**")
        st.markdown("""
        2028年の夏季オリンピックは、南アフリカのケープタウンで開催されます。
        美しい自然と都市が融合した素晴らしい大会になるでしょう。
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 警告メッセージ
        st.markdown('<div class="warning-box">', unsafe_allow_html=True)
        st.markdown("⚠️ **ちょっと待って！**")
        st.markdown("""
        これは、AIがもっともらしく作り出したウソの情報（**ハルシネーション**）です。
        
        **正解はアメリカのロサンゼルスです。**
        
        AIは、学習していない情報や未来のことについて聞かれると、
        平気でウソをつくことがあります。AIの答えもファクトチェックが欠かせません。
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # AI情報の信頼性について
        st.markdown("**AIの特徴と注意点：**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**✅ AIの得意なこと**")
            st.markdown("- 大量の情報の要約")
            st.markdown("- パターンの認識")
            st.markdown("- 創作支援")
            st.markdown("- 言語翻訳")
        
        with col2:
            st.markdown("**⚠️ AIの苦手なこと**")
            st.markdown("- 最新情報の提供")
            st.markdown("- 事実の正確性保証")
            st.markdown("- 専門的な判断")
            st.markdown("- 責任ある意思決定")
        
        # AIハルシネーション率の可視化
        hallucination_data = pd.DataFrame({
            'Question_Type': ['一般知識', '最新情報', '未来予測', '専門分野', '創作'],
            'Accuracy': [85, 30, 10, 60, 95],
            'Hallucination_Risk': [15, 70, 90, 40, 5]
        })
        
        fig = px.bar(hallucination_data, x='Question_Type', y=['Accuracy', 'Hallucination_Risk'],
                     title='AIの質問タイプ別精度とハルシネーションリスク',
                     barmode='group')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("### 🎓 まとめ")
st.success("""
**今日学んだこと：**
- メディアは時代とともに大きく進化してきた
- テキストコミュニケーションには非言語情報が不足するという課題がある
- 情報の信頼性を確認するファクトチェックが重要
- AIも間違いがあるため、批判的思考が必要

**これからのメディアリテラシー：**
情報を受け取るだけでなく、「誰が」「なぜ」「どのように」発信しているかを考え、
複数の情報源を比較検討する習慣を身につけましょう！
""")

# Interactive summary
if st.button("学習の振り返りクイズ", key="final_quiz"):
    st.balloons()
    st.markdown("**お疲れさまでした！** あなたは情報リテラシーの基礎を身につけました。🎉")
