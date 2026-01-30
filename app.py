import streamlit as st
import pandas as pd

# --------------------------
# 1. App 基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州孝親行",
    page_icon="🎌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂 CSS：優化手機閱讀體驗與按鈕大小
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
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        border-color: #FF4B4B;
        color: #FF4B4B;
        background-color: #FFF0F0;
    }
    /* 強調關鍵字 */
    .highlight {
        color: #E74C3C;
        font-weight: bold;
        background-color: #FDEDEC;
        padding: 2px 5px;
        border-radius: 4px;
    }
    /* 路線指引區塊 */
    .route-box {
        background-color: #F4F6F7;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2980B9;
        margin-bottom: 10px;
    }
    h1 { color: #C0392B; }
    h2 { border-bottom: 2px solid #E74C3C; padding-bottom: 5px; margin-top: 30px; font-size: 24px;}
    h3 { color: #2E86C1; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 標題
st.title("🎌 2026 北九州舒活孝親行")
st.caption("Family Trip: 2026/3/1 (日) - 3/6 (五)")
st.info("💡 點擊按鈕可直接開啟 Google Maps 導航")

# --------------------------
# 2. 核心分頁
# --------------------------
tab1, tab2, tab3 = st.tabs(["📅 詳細行程", "🛍️ 購物清單", "🎫 票券與備忘"])

# === Tab 1: 每日行程導航 ===
with tab1:
    day = st.selectbox("請選擇日期：", 
        ["Day 1 (3/1): 啟程 & 飯店補給", 
         "Day 2 (3/2): 太宰府 & 燒肉", 
         "Day 3 (3/3): 海豚 & 天神購物", 
         "Day 4 (3/4): 門司港 & 超市派對", 
         "Day 5 (3/5): 熊本 & 鰻魚飯", 
         "Day 6 (3/6): 甜點 & 返台"])

    st.divider()

    # --- Day 1 ---
    if "Day 1" in day:
        st.header("Day 1: 啟程與補給")
        
        st.markdown("### 🚄 12:00 高鐵台中站")
        st.write("目標：桃園機場 T2 (BR102 / 16:25 起飛)")
        
        st.markdown("### 🛬 19:55 抵達福岡 (接駁)")
        st.info("1. 出國際航廈大門，左轉找 **1號站牌**。\n2. 搭乘藍色 **「國際線-國內線接駁巴士」** (約15分)。\n3. 終點站下車即是地鐵入口。")
        
        st.markdown("### 🚇 21:20 地鐵轉乘 (關鍵!)")
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 【福岡機場站】搭空港線 (往姪浜/唐津) → <b>【博多站】</b><br>
        <b>Step 2 (不出站):</b> 下車找地上綠色貼紙<b>「七隈線」</b>，走連通道 (電動步道約6分)。<br>
        <b>Step 3:</b> 搭七隈線 (往橋本) → <b>【渡邊通站】</b> (1站)。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🏨 22:00 入住飯店")
        st.markdown("""
        <div class="route-box">
        <b>出口：</b> 找 <b>【2 號出口】</b> (有手扶梯)。<br>
        <b>動線：</b> 出站左轉，直走過橋 (雷橋)，飯店在左手邊。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：Cross Life 博多柳橋", "https://www.google.com/maps/search/?api=1&query=Cross+Life+Hakata+Yanagibashi")
        
        st.markdown("### 🏪 22:30 宵夜採買")
        st.write("**Sunny 超市 渡邊通店** (飯店出門右轉1分鐘)")
        st.link_button("📍 導航：Sunny 超市", "https://www.google.com/maps/search/?api=1&query=Sunny+Watanabedori")
        st.success("📝 必買：大瓶水(2L)、博多草莓、優格、明天早餐。")

    # --- Day 2 ---
    elif "Day 2" in day:
        st.header("Day 2: 太宰府 & 燒肉")
        
        st.markdown("### 🥐 09:00 早餐 & 準備")
        st.write("地鐵：【渡邊通】→【博多站】(往博多口出站)")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("📍 DACOMECCA (麵包)", "https://www.google.com/maps/search/?api=1&query=DACOMECCA")
        with col2:
            st.link_button("📍 麥當勞 (博多站)", "https://www.google.com/maps/search/?api=1&query=McDonald's+Hakata+Bus+Terminal")
            
        st.markdown("### ⛩️ 10:30 前往太宰府")
        st.markdown("""
        <div class="route-box">
        <b>1. 地鐵：</b> 博多站 → <b>【天神站】</b><br>
        <b>2. 轉乘 (不出站)：</b> 依黃色指標「西鐵電車」走地下街上2樓。<br>
        <b>3. 西鐵：</b> 搭特急/急行 → <b>【二日市】</b> 換車 → <b>【太宰府】</b>。
        </div>
        """, unsafe_allow_html=True)
        st.write("🌸 **必吃甜點：** 梅枝餅 (卡薩乃家)、星巴克表參道店。")
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=Dazaifu+Tenmangu")
        
        st.markdown("### 🛍️ 17:10 天神購物 (PLST)")
        st.write("回程：西鐵回到【天神站】→ 走往 **北口**。")
        st.write("地點：**Mina 天神** 1F (Uniqlo同棟)")
        st.link_button("📍 導航：Mina 天神", "https://www.google.com/maps/search/?api=1&query=Mina+Tenjin")
        
        st.markdown("### 🥩 19:00 晚餐：藥院燒肉 肉一")
        st.info("🚕 **移動建議：** 帶著戰利品，直接從 Mina 天神門口 **搭計程車** (約¥1000)。")
        st.success("✅ 已預約：19:00 / 藥院店 (Yakuin)")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=Yakuin+Yakiniku+Nikuichi")
        
        with st.expander("🚨 晚餐備案 & 宵夜"):
            st.write("1. **博多皮屋 (雞皮)**：祇園附近，適合宵夜。")
            st.link_button("📍 導航：博多皮屋 祇園店", "https://www.google.com/maps/search/?api=1&query=Hakata+Kawaya+Gion")
            st.write("2. 回飯店旁吃 **彌昂亭** 定食。")

    # --- Day 3 ---
    elif "Day 3" in day:
        st.header("Day 3: 海洋世界 & 天神")
        st.info("🐬 11:00 海豚秀 (JR 海之中道站)")
        
        st.markdown("### 🚃 09:30 JR 移動")
        st.markdown("""
        <div class="route-box">
        <b>1. 進站：</b> 博多站 JR 中央改札口 (1、2月台)。<br>
        <b>2. 搭車：</b> 鹿兒島本線(快速) → <b>【香椎站】</b>。<br>
        <b>3. 轉乘：</b> 換月台搭香椎線 → <b>【海之中道站】</b>。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=Marine+World+Uminonakamichi")
        
        st.markdown("### 🛍️ 16:30 天神北攻略")
        st.write("交通：JR回博多 → 轉地鐵到【天神站】(往東口/1號出口)。")
        st.write("🥖 **必買：Full Full 明太子法棍** (Mina天神對面)")
        st.link_button("📍 導航：Full Full 天神", "https://www.google.com/maps/search/?api=1&query=Full+Full+Hakata")
        st.write("🍰 **下午茶：** 天神地下街 BAKE 起司塔 / RINGO 蘋果派")
        
        st.markdown("### 🍤 17:45 晚餐：天麩羅 Hirao")
        st.write("地點：大名店 (Daimyo)")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=Tempura+Hirao+Daimyo")
        
        st.markdown("### 🛒 19:30 超市補貨")
        st.write("**AEON Shoppers 福岡店** (天神北)")
        st.link_button("📍 導航：AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=AEON+Shoppers+Fukuoka")
        st.info("🚕 **回程：** 東西太多直接搭計程車回飯店。")

    # --- Day 4 ---
    elif "Day 4" in day:
        st.header("Day 4: 門司港 & 超市派對")
        st.warning("🚅 09:21 音速號 (博多站出發)")
        
        st.markdown("### 🐡 10:30 門司港 & 唐戶市場")
        st.markdown("""
        <div class="route-box">
        <b>1. 去程：</b> 音速號 → <b>【小倉】</b> 轉普通車 → <b>【門司港】</b>。<br>
        <b>2. 渡輪：</b> 出站左轉搭船 → 下關唐戶。<br>
        <b>3. 午餐：</b> 唐戶市場 2F 海轉唐戶 (河豚壽司)。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=Karato+Market")
        
        st.markdown("### 🍦 14:00 下午茶")
        st.write("**Mooon de Retro** (水果聖代) 或 門司港布丁。")
        st.link_button("📍 導航：Mooon de Retro", "https://www.google.com/maps/search/?api=1&query=Fruit+Factory+Mooon+de+Retro")
        
        st.markdown("### 🍕 18:30 晚餐：LOPIA 超市")
        st.markdown("""
        <div class="route-box">
        <b>地點：</b> 博多站 <b>筑紫口</b> (Yodobashi 電器行 4F)。<br>
        <b>攻略：</b> 買披薩、壽司、熟食、草莓。<br>
        <b>回程：</b> 筑紫口排班處搭計程車回飯店開派對。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=LOPIA+Hakata+Yodobashi")
        
        with st.expander("🛍️ 逛街備案"):
            st.write("若想逛街，博多站樓上 AMU Plaza 6F 也有 **PLST**。")

    # --- Day 5 ---
    elif "Day 5" in day:
        st.header("Day 5: 熊本 & 鰻魚")
        st.error("🚅 08:30 新幹線 (記得帶 IC 卡)")
        
        st.markdown("### 🏯 上午：熊本移動")
        st.markdown("""
        <div class="route-box">
        <b>1. 新幹線：</b> 博多(筑紫口改札) → <b>【熊本站】</b>。<br>
        <b>2. 電車：</b> 白川口搭A系統 → <b>【水前寺公園】</b>。<br>
        <b>3. 移動：</b> 電車回頭搭至 <b>【辛島町】</b> 吃午餐。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🐷 11:20 午餐：勝烈亭豬排")
        st.write("地點：新市街本店 (辛島町步行2分)")
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=Katsuretsu+Tei+Shinshigai")
        
        st.markdown("### 🍦 下午：熊本城")
        st.write("搭接駁車上城彩苑/天守閣。")
        st.write("甜點：**Tente 鮮果霜淇淋**、香梅庵陣太鼓。")
        
        st.markdown("### 🍱 18:50 晚餐：吉塚鰻魚屋")
        st.markdown("""
        <div class="route-box">
        <b>交通：</b> 18:23 回到博多站 → 走到博多口。<br>
        <b>移動：</b> <b>搭計程車</b> 直達餐廳 (最舒服)。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=Yoshizuka+Unagiya")
        
        with st.expander("🚨 晚餐備案 (若不想跑)"):
            st.write("**Tanya 牛舌 (たんや)**：博多站一番街 B1。")
            st.link_button("📍 導航：Tanya HAKATA", "https://www.google.com/maps/search/?api=1&query=Tanya+Hakata")

    # --- Day 6 ---
    elif "Day 6" in day:
        st.header("Day 6: 甜點 & 返台")
        
        st.markdown("### 🍩 09:30 I'm donut ?")
        st.write("策略：飯店走過去 8 分鐘 (大丸百貨對面)。開店前排隊，買完就走。")
        st.link_button("📍 導航：I'm donut ? 福岡店", "https://www.google.com/maps/search/?api=1&query=I'm+donut+Fukuoka")
        
        st.markdown("### ✈️ 10:15 前往機場")
        st.info("🚕 **交通：** 路邊攔計程車 → **福岡機場國際線**。")
        st.write("航班：BR105 (12:15 起飛)")
        st.link_button("📍 導航：福岡機場國際線", "https://www.google.com/maps/search/?api=1&query=Fukuoka+Airport+International+Terminal")

# === Tab 2: 購物清單 ===
with tab2:
    st.header("🛍️ 採買檢核表")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏪 超市/超商")
        st.checkbox("博多甘王草莓 🍓")
        st.checkbox("大瓶水 (2L)")
        st.checkbox("優格/牛奶")
        st.checkbox("布丁/泡芙")
        
    with col2:
        st.subheader("🎁 伴手禮")
        st.checkbox("Full Full 明太子法棍")
        st.checkbox("福砂屋 長崎蛋糕")
        st.checkbox("明太子軟管 (Fukuya)")
        st.checkbox("博多通饅頭")
        st.checkbox("I'm donut ? 甜甜圈")
    
    st.divider()
    st.subheader("💊 藥妝 (天神大國/Cosmos)")
    st.checkbox("合利他命")
    st.checkbox("感冒藥 (Pubロン)")
    st.checkbox("眼藥水 / 貼布")

# === Tab 3: 票券與備忘 ===
with tab3:
    st.header("🎫 關鍵票券")
    
    st.info("💡 日本取票記得帶：**預約信用卡** + **護照**")
    
    st.markdown("### 🚄 台灣高鐵")
    st.code("去程：3/1 12:00 (台中→桃園)", language="text")
    st.code("回程：3/6 15:21 (桃園→台中)", language="text")
    
    st.markdown("### 🇯🇵 JR 九州")
    st.code("音速號：3/4 09:21 (博多→小倉)", language="text")
    st.code("新幹線：3/5 08:30 (博多→熊本)", language="text")
    
    st.markdown("### 🍽️ 餐廳預約")
    st.success("藥院燒肉 肉一：3/2 19:00 (4人)")
    st.caption("預約大名：鄭有浩 先生")

# 頁尾
st.divider()
st.caption("Made with ❤️ for 2026 Family Trip")
