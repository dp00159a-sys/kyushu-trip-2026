import streamlit as st
import pandas as pd

# --------------------------
# 1. 頁面基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州孝親行",
    page_icon="🎌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂 CSS: 優化手機按鈕與字體
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        font-weight: bold;
        border: 1px solid #ddd;
        background-color: #ffffff;
        color: #333333;
    }
    .stButton>button:hover {
        border-color: #FF4B4B;
        color: #FF4B4B;
    }
    /* 讓 Tab 標籤大一點，手指好點 */
    button[data-baseweb="tab"] {
        font-size: 16px;
        padding: 10px;
    }
    h1 { color: #FF4B4B; }
    h2 { border-bottom: 2px solid #FF4B4B; padding-bottom: 5px; margin-top: 20px;}
    .big-font { font-size: 18px; font-weight: bold; color: #2E86C1; }
    </style>
    """, unsafe_allow_html=True)

# 標題區
st.title("🎌 2026 北九州舒活孝親行")
st.caption("Family Trip: 2026/3/1 (日) - 3/6 (五)")

# --------------------------
# 2. 核心分頁
# --------------------------
tab1, tab2, tab3 = st.tabs(["📅 每日行程", "🛍️ 採買清單", "🎫 車票與預約"])

# === Tab 1: 每日行程細節 ===
with tab1:
    day = st.selectbox("請選擇日期查看導航：", 
        ["Day 1 (3/1): 啟程 & 飯店", 
         "Day 2 (3/2): 太宰府 & 燒肉", 
         "Day 3 (3/3): 海豚 & 天神", 
         "Day 4 (3/4): 門司港 & 超市", 
         "Day 5 (3/5): 熊本 & 鰻魚", 
         "Day 6 (3/6): 甜點 & 返台"])

    st.divider()

    if "Day 1" in day:
        st.header("Day 1: 啟程與補給")
        
        st.markdown("### 🚄 12:00 高鐵台中站出發")
        st.write("目標：桃園機場 T2 (BR102 / 16:25 起飛)")
        
        st.markdown("### 🚇 21:20 機場轉乘 (關鍵)")
        st.warning("⚠️ 博多站下車後，**不出站**！看綠色指標走連通道轉七隈線。")
        st.info("路線：福岡機場 → 博多 → **渡邊通 (2號出口)**")
        
        st.markdown("### 🏨 22:00 入住飯店")
        st.write("**Cross Life 博多柳橋**")
        st.link_button("📍 導航：Cross Life Hotel", "https://www.google.com/maps/search/?api=1&query=Cross+Life+Hakata+Yanagibashi")
        
        st.markdown("### 🏪 22:30 飯店旁採買")
        st.link_button("📍 導航：Sunny 超市 渡邊通店", "https://www.google.com/maps/search/?api=1&query=Sunny+Watanabe+Dori")
        st.write("📝 必買：大瓶水 (2L)、博多草莓、優格、明天早餐。")

        # 地圖：顯示飯店與超市
        map_data = pd.DataFrame({
            'lat': [33.5824, 33.5818],
            'lon': [130.4062, 130.4055],
            'name': ['飯店', 'Sunny超市']
        })
        st.map(map_data, zoom=15)

    elif "Day 2" in day:
        st.header("Day 2: 太宰府 & 燒肉")
        
        st.markdown("### 🥐 09:00 早餐 & 準備")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Go: DACOMECCA", "https://www.google.com/maps/search/?api=1&query=DACOMECCA")
        with col2:
            st.link_button("Go: 麥當勞 (博多)", "https://www.google.com/maps/search/?api=1&query=McDonalds+Hakata+Bus+Terminal")
            
        st.markdown("### ⛩️ 11:30 太宰府天滿宮")
        st.write("交通：天神站轉西鐵 (特急/急行)。")
        st.write("必吃：**梅枝餅** (卡薩乃家)、星巴克表參道店。")
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=Dazaifu+Tenmangu")
        
        st.markdown("### 🛍️ 17:10 天神購物 (PLST)")
        st.write("地點：Mina 天神 1F (UNIQLO 同棟)")
        st.link_button("📍 導航：Mina 天神", "https://www.google.com/maps/search/?api=1&query=Mina+Tenjin")
        
        st.markdown("### 🥩 19:00 晚餐：藥院燒肉 肉一")
        st.success("✅ 已預約：19:00 / 藥院店 (Yakuin)")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=Yakuin+Yakiniku+Nikuichi")
        
        with st.expander("🚨 晚餐備案 (若沒位子)"):
            st.write("1. **博多皮屋 (雞皮)**")
            st.link_button("Go: 皮屋 祇園店", "https://www.google.com/maps/search/?api=1&query=Hakata+Kawaya+Gion")
            st.write("2. 回飯店旁吃 **彌昂亭**")

        # 地圖：顯示太宰府與燒肉店
        map_data = pd.DataFrame({
            'lat': [33.5215, 33.5833],
            'lon': [130.5348, 130.4017], 
            'name': ['太宰府', '藥院燒肉']
        })
        st.map(map_data, zoom=10) # 縮放遠一點因為距離較遠

    elif "Day 3" in day:
        st.header("Day 3: 海洋世界 & 天神")
        st.info("🐬 11:00 海豚秀 (JR 海之中道站)")
        
        st.markdown("### 🐬 上午：海洋世界")
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=Marine+World+Uminonakamichi")
        
        st.markdown("### 🛍️ 下午：天神北攻略")
        st.write("1. **Full Full 麵包**：必買明太子法棍！")
        st.link_button("Go: Full Full 天神", "https://www.google.com/maps/search/?api=1&query=Full+Full+Hakata+Bakery")
        st.write("2. **AEON Shoppers**：超市補貨")
        st.link_button("Go: AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=AEON+Shoppers+Fukuoka")
        
        st.markdown("### 🍤 17:45 晚餐：天麩羅 Hirao")
        st.write("地點：大名店 (Daimyo)")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=Tempura+Hirao+Daimyo")

        # 地圖：顯示海洋世界
        map_data = pd.DataFrame({
            'lat': [33.6603, 33.5890],
            'lon': [130.3609, 130.3955],
            'name': ['海洋世界', '天神天婦羅']
        })
        st.map(map_data, zoom=11)

    elif "Day 4" in day:
        st.header("Day 4: 門司港 & 超市派對")
        st.warning("🚅 09:21 音速號 (博多站出發)")
        
        st.markdown("### 🐡 中午：唐戶市場")
        st.write("搭船前往。必吃：河豚壽司。")
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=Karato+Market")
        
        st.markdown("### 🍦 下午：門司港散策")
        st.write("推薦：Mooon 水果聖代、香蕉人像。")
        st.link_button("📍 導航：門司港站", "https://www.google.com/maps/search/?api=1&query=Mojiko+Station")
        
        st.markdown("### 🍕 晚上：LOPIA 超市熟食")
        st.write("地點：博多站筑紫口 Yodobashi 4F")
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=LOPIA+Hakata+Yodobashi")
        st.success("🎉 買完直接搭計程車回飯店開派對！")

        # 地圖：顯示門司港與唐戶
        map_data = pd.DataFrame({
            'lat': [33.9443, 33.9583],
            'lon': [130.9602, 130.9427],
            'name': ['門司港', '唐戶市場']
        })
        st.map(map_data, zoom=12)

    elif "Day 5" in day:
        st.header("Day 5: 熊本 & 鰻魚")
        st.error("🚅 08:30 新幹線 (記得帶 IC 卡)")
        
        st.markdown("### 🐷 11:20 午餐：勝烈亭豬排")
        st.write("地點：新市街本店 (辛島町站)")
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=Katsuretsu+Tei+Shinshigai")
        
        st.markdown("### 🏯 下午：熊本城")
        st.write("景點：水前寺成趣園、熊本城(城彩苑)。")
        st.link_button("📍 導航：熊本城", "https://www.google.com/maps/search/?api=1&query=Kumamoto+Castle")
        
        st.markdown("### 🍱 18:50 晚餐：吉塚鰻魚屋")
        st.info("🚕 建議：從博多站 **搭計程車** 直達門口！")
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=Yoshizuka+Unagiya")

        # 地圖：顯示熊本城與鰻魚屋(博多)
        map_data = pd.DataFrame({
            'lat': [32.8062, 33.5930],
            'lon': [130.7058, 130.4086],
            'name': ['熊本城', '吉塚鰻魚']
        })
        st.map(map_data, zoom=8) # 跨縣市縮放

    elif "Day 6" in day:
        st.header("Day 6: 甜點 & 返台")
        
        st.markdown("### 🍩 09:30 I'm donut ?")
        st.write("策略：飯店走過去 8 分鐘。開店前排隊，買完就走。")
        st.link_button("📍 導航：I'm donut ? 福岡店", "https://www.google.com/maps/search/?api=1&query=Im+donut+Fukuoka")
        
        st.divider()
        st.markdown("### ✈️ 12:15 BR105 起飛")
        st.write("10:15 搭計程車前往機場國際線。")
        st.link_button("📍 導航：福岡機場國際線", "https://www.google.com/maps/search/?api=1&query=Fukuoka+Airport+International+Terminal")

# === Tab 2: 採買清單 ===
with tab2:
    st.header("🛍️ 採買檢核表")
    st.write("勾選已買到的物品：")
    
    st.subheader("🏪 超市/便利商店")
    st.checkbox("博多甘王草莓 🍓")
    st.checkbox("大瓶水 (2L)")
    st.checkbox("優格/牛奶 (早餐用)")
    
    st.subheader("🎁 伴手禮")
    st.checkbox("Full Full 明太子法棍 🥖")
    st.checkbox("福砂屋 長崎蛋糕 (機場)")
    st.checkbox("明太子軟管 (Fukuya)")
    st.checkbox("博多通饅頭")
    
    st.subheader("💊 藥妝 (天神大國)")
    st.checkbox("合利他命")
    st.checkbox("感冒藥 (Pubロン)")
    st.checkbox("眼藥水")

# === Tab 3: 車票與預約 ===
with tab3:
    st.header("🎫 票券與預約資訊")
    
    with st.container():
        st.markdown("### 🚅 高鐵 (台灣)")
        st.code("去程：3/1 12:00 台中→桃園", language="text")
        st.code("回程：3/6 15:21 桃園→台中", language="text")
    
    st.divider()
    
    with st.container():
        st.markdown("### 🇯🇵 日本交通")
        st.warning("記得帶實體信用卡取票！")
        st.code("音速號：3/4 09:21 (博多→小倉)", language="text")
        st.code("新幹線：3/5 08:30 (博多→熊本)", language="text")
        
    st.divider()
    
    with st.container():
        st.markdown("### 🍽️ 餐廳預約")
        st.code("藥院燒肉 肉一：3/2 19:00 (4人)", language="text")
        st.caption("預約大名：鄭有浩 先生")

# 頁尾
st.divider()
st.caption("Made with ❤️ for 2026 Family Trip")
