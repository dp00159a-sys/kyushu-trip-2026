import streamlit as st
import pandas as pd

# --------------------------
# 1. 頁面基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州孝親行",
    page_icon="✈️",
    layout="centered", # 手機版面集中比較好看
    initial_sidebar_state="collapsed"
)

# 自訂 CSS 讓手機按鈕更好按
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    /* 讓 Tab 字體大一點 */
    button[data-baseweb="tab"] {
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 標題區
st.title("🇯🇵 2026 北九州舒活孝親行")
st.caption("Family Trip: 2026/3/1 - 3/6")

# --------------------------
# 2. 核心分頁 (Tabs)
# --------------------------
tab1, tab2, tab3 = st.tabs(["📅 每日行程", "🛍️ 採買清單", "🎫 車票與預約"])

# === Tab 1: 每日行程細節 ===
with tab1:
    day = st.selectbox("請選擇日期查看：", 
        ["Day 1 (3/1): 啟程 & 超市", 
         "Day 2 (3/2): 太宰府 & 燒肉", 
         "Day 3 (3/3): 海豚 & 天神", 
         "Day 4 (3/4): 門司港 & 超市", 
         "Day 5 (3/5): 熊本 & 鰻魚", 
         "Day 6 (3/6): 甜點 & 返台"])

    st.divider()

    if "Day 1" in day:
        st.header("Day 1: 啟程與補給")
        st.info("💡 重點：飯店轉乘要走連通道、晚上去超市")
        
        st.markdown("### 🚄 12:00 高鐵台中站出發")
        st.write("搭乘 BR102 班機 (16:25 起飛)")
        
        st.markdown("### 🚇 21:20 機場轉乘 (關鍵)")
        st.warning("博多站下車後，不出站！走連通道轉七隈線。")
        st.text("路線：福岡機場 → 博多 → 渡邊通 (2號出口)")
        
        st.markdown("### 🏪 22:30 飯店旁採買")
        st.link_button("📍 導航：Sunny 超市 渡邊通店", "https://maps.app.goo.gl/example") # 範例連結
        st.write("必買：大瓶水、草莓、優格、明天早餐。")

    elif "Day 2" in day:
        st.header("Day 2: 太宰府 & 燒肉")
        st.success("🍖 晚餐：19:00 藥院燒肉 肉一 (已預約)")
        
        st.subheader("🥐 09:00 早餐")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("Go: DACOMECCA", "https://www.google.com/maps/search/?api=1&query=DACOMECCA")
        with col2:
            st.link_button("Go: 麥當勞", "https://www.google.com/maps/search/?api=1&query=McDonalds+Hakata")
            
        st.subheader("⛩️ 11:30 太宰府")
        st.write("搭西鐵電車前往。必吃：**梅枝餅** (卡薩乃家)。")
        
        st.subheader("🛍️ 17:10 天神購物")
        st.write("地點：Mina 天神 1F (PLST/Uniqlo)")
        
        st.subheader("🥩 19:00 晚餐：藥院燒肉 肉一")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=Yakuin+Yakiniku+Nikuichi")
        
        with st.expander("🚨 晚餐備案 (若沒位子)"):
            st.write("1. **博多皮屋 (雞皮)**")
            st.write("2. 回飯店吃彌昂亭")

    elif "Day 3" in day:
        st.header("Day 3: 海洋世界 & 天神")
        st.info("🐬 11:00 海豚秀 (JR 海之中道站)")
        
        st.markdown("### 🐬 上午：海洋世界")
        st.write("交通：博多站搭 JR 鹿兒島本線轉香椎線")
        
        st.markdown("### 🛍️ 下午：天神北")
        st.checkbox("買 Full Full 明太子法棍", value=True)
        st.checkbox("逛 AEON Shoppers 超市")
        
        st.markdown("### 🍤 17:45 晚餐：天麩羅 Hirao")
        st.link_button("📍 導航：天麩羅處 Hirao 大名店", "https://www.google.com/maps/search/?api=1&query=Tempura+Hirao+Daimyo")

    elif "Day 4" in day:
        st.header("Day 4: 門司港 & 超市派對")
        st.warning("🚅 09:21 音速號 (博多站出發)")
        
        st.markdown("### 🐡 中午：唐戶市場")
        st.write("必吃：河豚壽司、炸河豚。")
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=Karato+Market")
        
        st.markdown("### 🍦 下午：門司港甜點")
        st.write("推薦：Mooon 水果聖代、燒咖哩、門司港布丁。")
        
        st.markdown("### 🍕 晚上：LOPIA 超市熟食")
        st.write("地點：博多友都八喜 4F")
        st.link_button("📍 導航：LOPIA 博多店", "https://www.google.com/maps/search/?api=1&query=LOPIA+Hakata")
        st.success("買完直接搭計程車回飯店開派對！")

    elif "Day 5" in day:
        st.header("Day 5: 熊本 & 鰻魚")
        st.error("🚅 08:30 新幹線 (記得帶 IC 卡)")
        
        st.markdown("### 🐷 11:20 午餐：勝烈亭豬排")
        st.write("地點：新市街本店 (辛島町站)")
        st.link_button("📍 導航：勝烈亭", "https://www.google.com/maps/search/?api=1&query=Katsuretsu+Tei+Shinshigai")
        
        st.markdown("### 🏯 下午：熊本城")
        st.write("甜點：城彩苑 Tente 霜淇淋、陣太鼓。")
        
        st.markdown("### 🍱 18:50 晚餐：吉塚鰻魚屋")
        st.write("從博多站直接 **搭計程車** 過去最快！")
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=Yoshizuka+Unagiya")

    elif "Day 6" in day:
        st.header("Day 6: 甜點 & 返台")
        
        st.markdown("### 🍩 09:30 I'm donut ?")
        st.write("策略：開店前去排，買了直接走。")
        st.link_button("📍 導航：I'm donut ? 福岡店", "https://www.google.com/maps/search/?api=1&query=I'm+donut+Fukuoka")
        
        st.divider()
        st.markdown("### ✈️ 12:15 BR105 起飛")
        st.write("10:15 搭計程車前往機場。")

# === Tab 2: 採買清單 (互動式) ===
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
    
    st.subheader("💊 藥妝")
    st.checkbox("合利他命")
    st.checkbox("感冒藥 (Pubロン)")
    st.checkbox("眼藥水")

# === Tab 3: 車票與預約 ===
with tab3:
    st.header("🎫 票券與預約資訊")
    
    with st.container():
        st.markdown("### 🚅 高鐵 (台灣)")
        st.code("去程：3/1 12:xx 台中→桃園", language="text")
        st.code("回程：3/6 15:21 桃園→台中", language="text")
    
    st.divider()
    
    with st.container():
        st.markdown("### 🇯🇵 日本交通")
        st.info("💡 記得帶實體信用卡取票！")
        st.code("音速號：3/4 09:21 (博多→小倉)", language="text")
        st.code("新幹線：3/5 08:30 (博多→熊本)", language="text")
        
    st.divider()
    
    with st.container():
        st.markdown("### 🍽️ 餐廳預約")
        st.success("請截圖保存預約信件")
        st.code("藥院燒肉 肉一：3/2 19:00 (4人)", language="text")

# 頁尾
st.divider()
st.caption("Designed for 2026 North Kyushu Trip ❤️")