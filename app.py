import streamlit as st
import os

# --------------------------
# 1. App 基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州旅遊",
    page_icon="🎌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂 CSS：優化視覺與操作感 (手機友善版)
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
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #FF4B4B;
        color: #FF4B4B;
        background-color: #FFF0F0;
        transform: translateY(-2px);
    }
    .route-box {
        background-color: #F4F6F7;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #2980B9;
        margin-bottom: 10px;
        font-size: 0.95em;
    }
    .ticket-box {
        background-color: #E8F8F5;
        padding: 15px;
        border-radius: 10px;
        border: 2px dashed #1ABC9C;
        margin-bottom: 10px;
    }
    .shopping-box {
        background-color: #FEF9E7;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #F1C40F;
        margin-bottom: 10px;
    }
    .bento-box {
        background-color: #FFF3E0;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #FF9800;
        margin-bottom: 10px;
    }
    .time-badge {
        background-color: #ECEFF1;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        color: #455A64;
        margin-right: 5px;
    }
    .highlight {
        background-color: #FDEDEC;
        padding: 2px 5px;
        border-radius: 3px;
        color: #C0392B;
        font-weight: bold;
    }
    h1 { color: #C0392B; text-align: center; }
    h2 { border-bottom: 2px solid #E74C3C; padding-bottom: 5px; margin-top: 30px;}
    </style>
    """, unsafe_allow_html=True)

st.title("🎌 2026 北九州6日遊")
st.caption("Family Trip: 2026/3/1 (日) - 3/6 (五) | 全數票券確認 ✅")

# --------------------------
# 2. 核心分頁
# --------------------------
tab1, tab2, tab3 = st.tabs(["📅 詳細行程", "🛍️ 購物清單", "🎫 車票與預約"])

# === Tab 1: 每日行程 ===
with tab1:
    day = st.selectbox("請選擇日期查看詳情：", 
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
        
        st.markdown("##### <span class='time-badge'>12:00</span> 出發", unsafe_allow_html=True)
        st.write("高鐵台中站 → 桃園機場 T2 (BR102 / 16:25 起飛)")
        
        st.markdown("##### <span class='time-badge'>19:55</span> 抵達福岡機場", unsafe_allow_html=True)
        st.info("動線：出航廈大門左轉 → 1 號站牌 (接駁巴士) → 地鐵福岡機場站。")
        
        st.markdown("##### <span class='time-badge'>21:20</span> 地鐵轉乘 (關鍵)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 【福岡機場站】搭空港線 → <b>【博多站】</b><br>
        <b>Step 2:</b> 走連通道轉七隈線 (電動步道約 6 分鐘)。<br>
        <b>Step 3:</b> 搭七隈線 (往橋本方向 1 站) → <b>【渡邊通站】</b>。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>22:00</span> 入住飯店", unsafe_allow_html=True)
        st.write("出口：**2號出口** (有手扶梯)。出站左轉過橋即達。")
        st.link_button("📍 導航：Cross Life 博多柳橋", "https://www.google.com/maps/search/?api=1&query=Cross+Life+Hakata+Yanagibashi")
        
        st.markdown("##### <span class='time-badge'>22:30</span> 宵夜補給", unsafe_allow_html=True)
        st.write("購買大瓶水、草莓、優格、隔日早餐。")
        st.link_button("📍 導航：Sunny 超市", "https://www.google.com/maps/search/?api=1&query=Sunny+Watanabedori")

    # --- Day 2 ---
    elif "Day 2" in day:
        st.header("Day 2: 太宰府 & 燒肉")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### <span class='time-badge'>08:30</span> 早餐", unsafe_allow_html=True)
            st.write("挑戰排隊名店或吃麥當勞。")
            st.link_button("📍 DACOMECCA", "https://www.google.com/maps/search/?api=1&query=DACOMECCA")
        with col2:
            st.markdown("##### <span class='time-badge'>09:30</span> 移動", unsafe_allow_html=True)
            st.write("地鐵至【天神站】轉西鐵。")
            st.link_button("📍 麥當勞", "https://www.google.com/maps/search/?api=1&query=McDonald's+Hakata+Bus+Terminal")
            
        st.markdown("##### <span class='time-badge'>10:00</span> 前往太宰府 (西鐵)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>1. 搭車：</b> 西鐵天神站 (2F/3F) 搭特急/急行 (往大牟田)。<br>
        <b>2. 換車：</b> 在 <b>【西鐵二日市站】</b> 下車。<br>
        <b>3. 轉乘：</b> 同月台或換月台轉搭「太宰府線」。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=Dazaifu+Tenmangu")
        
        st.markdown("##### <span class='time-badge'>15:00</span> 天神地下街 & 購物", unsafe_allow_html=True)
        st.info("🛍️ **雨天/避暑備案：** 從西鐵天神站地下街一路逛到 Mina 天神，舒適不累。")
        st.link_button("📍 導航：天神地下街", "https://maps.app.goo.gl/x5cvCFQsm8CpkkUH9")
        st.write("**Mina 天神**：UNIQLO, LOFT, 3COINS")
        st.link_button("📍 導航：Mina 天神", "https://www.google.com/maps/search/?api=1&query=Mina+Tenjin")
        
        st.markdown("##### <span class='time-badge'>18:20</span> 前往晚餐", unsafe_allow_html=True)
        st.warning("🚕 **建議：** 從天神南搭計程車前往，保留體力。")
        
        st.markdown("##### <span class='time-badge'>19:00</span> 晚餐：藥院燒肉 肉一", unsafe_allow_html=True)
        st.success("✅ 已預約：19:00 / 4 位 / 鄭有浩先生")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=Yakuin+Yakiniku+Nikuichi")

    # --- Day 3 ---
    elif "Day 3" in day:
        st.header("Day 3: 海洋世界 & 天麩羅")
        
        st.markdown("##### <span class='time-badge'>09:10</span> 出發", unsafe_allow_html=True)
        st.write("步行至博多車站。")
        
        st.markdown("##### <span class='time-badge'>09:30</span> 前往海之中道 (JR)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 博多站 1或2號月台 (鹿兒島本線) → <b>【香椎站】</b> (約09:42發)。<br>
        <b>Step 2 (⚠️):</b> 香椎站下車，<b>走天橋換到 4/5 號月台</b> (香椎線)。<br>
        <b>Step 3:</b> 搭 10:05 左右列車 → <b>【海之中道站】</b>。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：JR 海之中道站", "https://www.google.com/maps/dir/Hakata+Station,+%E4%B8%AD%E5%A4%AE%E8%A1%97-%EF%BC%91-1+%E5%8D%9A%E5%A4%9A%E9%A7%85,+%E5%8D%9A%E5%A4%9A%E5%8C%BA+%E7%A6%8F%E5%B2%A1%E5%B8%82+%E7%A6%8F%E5%B2%A1%E7%9C%8C,+Japan/Uminonakamichi+Station,+Japan/data=!4m18!4m17!1m5!1m1!19sChIJdbP55seRQTURkIu5RT0r4i4!2m2!1d130.4207274!2d33.589727499999995!1m5!1m1!19sChIJ3TdSJLKNQTURNA6c41YcDMU!2m2!1d130.3615228!2d33.6641936!2m3!6e0!7e2!8j1772530200!3e3")
        
        st.markdown("##### <span class='time-badge'>11:00</span> 海豚表演", unsafe_allow_html=True)
        st.write("地點：Marine World (出口即達)")
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=Marine+World+Uminonakamichi")
        
        st.markdown("##### <span class='time-badge'>16:50</span> 天神北購物", unsafe_allow_html=True)
        st.write("1. **Full Full 明太子法棍** (天神店)")
        st.link_button("📍 導航：Full Full 天神", "https://www.google.com/maps/search/?api=1&query=Full+Full+Hakata")
        st.write("2. **AEON Shoppers** (超市補貨)")
        st.link_button("📍 導航：AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=AEON+Shoppers+Fukuoka")
        
        st.markdown("##### <span class='time-badge'>17:40</span> 晚餐：天麩羅 Hirao", unsafe_allow_html=True)
        st.info("策略：走路前往大名店，現場排隊 (預計 30-40 分)。")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=Tempura+Hirao+Daimyo")

    # --- Day 4 ---
    elif "Day 4" in day:
        st.header("Day 4: 門司港 & 博多站爆買")
        
        st.markdown("##### <span class='time-badge'>09:00</span> 抵達博多站", unsafe_allow_html=True)
        st.warning("⚠️ 記得帶 **實體信用卡** 去機台領票！")
        
        st.markdown("##### <span class='time-badge'>09:21</span> 去程：音速號 Sonic 11", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 09:21 → 小倉 10:10</b><br>
        座位：<span class="highlight">3 號車 3AB, 4AB</span> (記得轉椅子)
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:10</span> 小倉站轉乘 (免出站)", unsafe_allow_html=True)
        # 顯示使用者上傳的圖片 (請確認檔名為 kokura_transfer.jpg)
        if os.path.exists("kokura_transfer.jpg"):
            st.image("kokura_transfer.jpg", caption="💡 攻略：下車後直接走到對面或隔壁月台 (7轉8)", use_column_width=True)
        else:
            st.info("💡 攻略：下車後直接走到對面或隔壁月台 (通常是 7 號轉 8 號)，不用上下樓梯。")
        st.write("搭乘 **鹿兒島本線 (往門司港)** 普通車。")
        
        st.markdown("##### <span class='time-badge'>10:40</span> 抵達門司港 & 補票", unsafe_allow_html=True)
        st.error("🛑 **請走人工通道**：出示音速號車票 + 補 ¥280 現金/刷 IC 卡。")
        st.link_button("📍 導航：門司港站", "https://www.google.com/maps/dir/Kokura+Station,+%EF%BC%91%E4%B8%81%E7%9B%AE-%EF%BC%91-1+%E6%B5%85%E9%87%8E,+%E5%B0%8F%E5%80%89%E5%8C%97%E5%8C%BA+%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82+%E7%A6%8F%E5%B2%A1%E7%9C%8C,+Japan/Mojiko+Station,+%EF%BC%91%E4%B8%81%E7%9B%AE-%EF%BC%95-31+%E8%A5%BF%E6%B5%B7%E5%B2%B8,+%E9%96%80%E5%8F%B8%E5%8C%BA+%E5%8C%97%E4%B9%9D%E5%B7%9E%E5%B8%82+%E7%A6%8F%E5%B2%A1%E7%9C%8C,+Japan/data=!4m14!4m13!1m5!1m1!19sChIJG1BJ-Uu_QzURbLAH89m7GGk!2m2!1d130.88257579999998!2d33.8869679!1m5!1m1!19sChIJm7Lk-SiWQzURomPcFPli5vg!2m2!1d130.9615522!2d33.945112099999996!3e3")
        
        st.markdown("##### 🐡 門司港行程", unsafe_allow_html=True)
        st.write("燒咖哩、搭船去唐戶市場、香蕉人、Mooon 水果聖代。")
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=Karato+Market")
        st.link_button("📍 導航：Mooon de Retro", "https://www.google.com/maps/search/?api=1&query=Fruit+Factory+Mooon+de+Retro")
        
        st.markdown("##### <span class='time-badge'>16:50</span> 小倉站轉乘 (回程攻略)", unsafe_allow_html=True)
        st.info("🔄 **標準動作：** 先刷 IC 卡 **出站** (付門司港車資)，再用音速號車票 **進站**。")
        
        st.markdown("##### <span class='time-badge'>17:06</span> 回程：音速號 Sonic 42", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>小倉 17:06 → 博多 17:49</b><br>
        座位：<span class="highlight">2 號車 3AB, 4AB</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:00</span> 博多站黃金採買動線", unsafe_allow_html=True)
        st.markdown("""
        <div class="shopping-box">
        <b>1. 博多銘品藏 (博多口)：</b> 買 <b>努努雞</b> (冷炸雞)。<br>
        <b>2. AMU PLAZA 1F：</b> 買 <b>AMANBERRY</b> (草莓夾心)。<br>
        <b>3. LOPIA 超市 (筑紫口 Yodobashi 4F)：</b> 買熟食/披薩。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：博多銘品藏", "https://maps.app.goo.gl/2ZRq2nocpSEEV4LN6")
        st.link_button("📍 導航：AMANBERRY", "https://maps.app.goo.gl/AYnit2B9CUzZJh859")
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=LOPIA+Hakata+Yodobashi")
        
        st.markdown("##### <span class='time-badge'>19:30</span> 回飯店", unsafe_allow_html=True)
        st.write("於筑紫口搭計程車回飯店開派對。")

    # --- Day 5 ---
    elif "Day 5" in day:
        st.header("Day 5: 熊本 & 鰻魚")
        
        st.markdown("##### <span class='time-badge'>08:00</span> 出發 & 買便當", unsafe_allow_html=True)
        st.markdown("""
        <div class="bento-box">
        <b>🍱 早餐任務：駅弁当 (Ekiben Station)</b><br>
        地點：博多站筑紫口 (改札口旁)。<br>
        建議：08:10 前買好，進站候車。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>08:30</span> 去程：新幹線 Mizuho 601", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 08:30 → 熊本 09:02</b><br>
        座位：<span class="highlight">5 號車 5AB, 6AB</span><br>
        備註：在車上享用便當！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### 🏯 熊本行程", unsafe_allow_html=True)
        st.write("上午：熊本城、城彩苑。")
        st.markdown("##### <span class='time-badge'>11:30</span> 午餐：勝烈亭豬排", unsafe_allow_html=True)
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=Katsuretsu+Tei+Shinshigai")
        st.write("下午：下通商店街、鶴屋百貨 (熊本熊)。")
        
        st.markdown("##### <span class='time-badge'>17:10</span> 熊本車站採買", unsafe_allow_html=True)
        st.markdown("""
        <div class="bento-box">
        <b>🐻 必逛：肥後よかモン市場</b><br>
        地點：新幹線改札口正對面。<br>
        目標：熊本熊圓形便當 (收藏用)、阿蘇赤牛便當 (宵夜)。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>17:20</span> 回程：新幹線 Tsubame 328", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>熊本 17:20 → 博多 18:09</b><br>
        座位：<span class="highlight">5 號車 6AB, 7AB</span><br>
        備註：提早回博多，從容吃晚餐！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:35</span> 移動", unsafe_allow_html=True)
        st.write("博多口直接搭 **計程車** 前往餐廳。")
        
        st.markdown("##### <span class='time-badge'>18:50</span> 晚餐：吉塚鰻魚屋", unsafe_allow_html=True)
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=Yoshizuka+Unagiya")

    # --- Day 6 ---
    elif "Day 6" in day:
        st.header("Day 6: 甜點 & 返台")
        
        st.markdown("##### <span class='time-badge'>08:50</span> 退房", unsafe_allow_html=True)
        st.write("行李寄放櫃台。")
        
        st.markdown("##### <span class='time-badge'>09:10</span> 最後衝刺", unsafe_allow_html=True)
        st.write("走路去排 **I'm donut ?** (天神店)。")
        st.info("備案：買完可去對面 **大丸百貨** (10:00開) 上廁所/晃晃。")
        st.link_button("📍 導航：I'm donut ?", "https://www.google.com/maps/search/?api=1&query=I'm+donut+Fukuoka")
        st.link_button("📍 導航：大丸福岡天神", "https://maps.app.goo.gl/ozKorXfoFtVUXPB37")
        
        st.markdown("##### <span class='time-badge'>10:15</span> 前往機場", unsafe_allow_html=True)
        st.warning("🚕 **交通：** 回飯店拿行李，請飯店叫車直奔「福岡機場國際線」。")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 機場採買", unsafe_allow_html=True)
        st.write("報到後逛免稅店 (福砂屋、明太子)。")
        st.write("**航班：** BR105 (12:15 起飛)。")

# === Tab 2: 購物清單 ===
with tab2:
    st.header("🛍️ 採買檢核表")
    
    st.subheader("📍 博多站 (Day 4 必買)")
    st.checkbox("努努雞 (Ming/銘品藏) - 冷著吃！ 🍗")
    st.checkbox("AMANBERRY 草莓夾心 (AMU 1F) 🍓")
    st.checkbox("LOPIA 熟食/披薩 (筑紫口)")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏪 超市/超商")
        st.checkbox("博多甘王草莓")
        st.checkbox("大瓶水 (2L)")
        st.checkbox("優格/牛奶")
    with col2:
        st.subheader("🎁 伴手禮")
        st.checkbox("Full Full 明太子法棍")
        st.checkbox("福砂屋 長崎蛋糕")
        st.checkbox("明太子軟管")
        st.checkbox("博多通饅頭")
        st.checkbox("熊本熊便當 (空盒)")

# === Tab 3: 車票與預約 ===
with tab3:
    st.header("🎫 票券管理中心 (已全數確認)")
    
    st.markdown("### ✅ Day 4: 音速號 (已購買)")
    st.success("博多 ↔ 小倉")
    st.markdown("""
    <div class="ticket-box">
    <b>去程 (Sonic 11):</b> 09:21 → 10:10<br>
    座位：<span class="highlight">3號車 3AB, 4AB</span><br>
    <hr style="margin:5px 0; border-top: 1px dashed #1ABC9C;">
    <b>回程 (Sonic 42):</b> 17:06 → 17:49<br>
    座位：<span class="highlight">2號車 3AB, 4AB</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ✅ Day 5: 新幹線 (已購買)")
    st.success("博多 ↔ 熊本")
    st.markdown("""
    <div class="ticket-box">
    <b>去程 (Mizuho 601):</b> 08:30 → 09:02<br>
    座位：<span class="highlight">5號車 5AB, 6AB</span><br>
    <hr style="margin:5px 0; border-top: 1px dashed #1ABC9C;">
    <b>回程 (Tsubame 328):</b> 17:20 → 18:09<br>
    座位：<span class="highlight">5號車 6AB, 7AB</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🍽️ 餐廳預約")
    st.success("藥院燒肉 肉一：3/2 19:00 (4人)")
    st.caption("預約大名：鄭又豪 先生")


