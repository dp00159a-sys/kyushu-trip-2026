import streamlit as st
import os

# --------------------------
# 1. App 基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州行",
    page_icon="🎌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂 CSS：原版清爽配色
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

st.title("🎌 2026 北九州行")
st.caption("Family Trip: 2026/3/1 (日) - 3/6 (五) | 全數票券與詳細動線已鎖定 ✅")

# --------------------------
# 2. 核心分頁
# --------------------------
tab1, tab2, tab3 = st.tabs(["📅 詳細行程", "🛍️ 購物清單", "🎫 車票與預約"])

# === Tab 1: 每日行程 ===
with tab1:
    day = st.selectbox("請選擇日期查看詳情：", 
        ["Day 1 (3/1): 啟程 & 福岡安頓", 
         "Day 2 (3/2): 太宰府賞梅 & 天神購物", 
         "Day 3 (3/3): 海豚相伴 & 天神北美食", 
         "Day 4 (3/4): 門司港跨海 & 博多爆買", 
         "Day 5 (3/5): 熊本一日遊 & 頂級鰻魚", 
         "Day 6 (3/6): 甜點衝刺 & 滿載而歸"])

    st.divider()

    # --- Day 1 ---
    if "Day 1" in day:
        st.header("Day 1: 啟程與福岡安頓")
        if os.path.exists("出國前最終確認：Day 1 (週日).jpg"):
            st.image("出國前最終確認：Day 1 (週日).jpg", use_column_width=True)
            
        st.info("💡 領隊廣播：記得提醒家人要帶悠遊卡 (Suica/ICOCA等)！雖然現場買票也可以，但有卡最方便。")
        
        st.markdown("##### <span class='time-badge'>12:00</span> 台灣出發", unsafe_allow_html=True)
        st.write("高鐵台中站 → 桃園機場 T2 (長榮航空 BR102 / 16:25 起飛)")
        
        st.markdown("##### <span class='time-badge'>19:55</span> 抵達日本 (福岡機場出關)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>🚌 機場移動動線：</b><br>
        拿好行李出關後，請從 <b>「A3 出口」</b> 離開航廈並 <b>「往右邊走」</b>，搭乘前往國內線的免費接駁巴士（車程約10分鐘），直達地鐵站入口。
        </div>
        """, unsafe_allow_html=True)
        
        # 新增的 YouTube 影片教學
        st.caption("🎥 實景走法請參考以下影片（從下飛機到搭巴士）：")
        st.video("https://www.youtube.com/watch?v=pRwDSFJskzQ")
        
        st.markdown("##### <span class='time-badge'>21:20</span> 市區移動 (地鐵轉乘)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 【福岡機場站】搭空港線 → <b>【博多站】</b> (2站)<br>
        <b>Step 2 (站內轉乘):</b> 下車跟著綠色指標走連通道轉七隈線 (有電動步道，慢慢走約6分鐘)。<br>
        <b>Step 3:</b> 搭七隈線往橋本方向 → <b>【渡邊通站】</b> (僅1站)。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>22:00</span> 飯店入住 (Cross Life 博多柳橋)", unsafe_allow_html=True)
        st.write("⚠️ **重要：在【渡邊通站】下車後，請務必尋找「2號出口」(有手扶梯)。** 出站後左轉過橋即達飯店。")
        st.link_button("📍 導航：Cross Life 博多柳橋", "https://www.google.com/maps/search/?api=1&query=Cross+Life+博多柳橋")
        
        st.markdown("##### <span class='time-badge'>22:30</span> 夜間補給 (Sunny 超市)", unsafe_allow_html=True)
        st.write("採買大瓶裝礦泉水 (2L)、博多甘王草莓、優格、隔日早餐備品。")
        st.link_button("📍 導航：Sunny 超市 渡邊通店", "https://www.google.com/maps/search/?api=1&query=Sunny+渡邊通店")

    # --- Day 2 ---
    elif "Day 2" in day:
        st.header("Day 2: 太宰府賞梅 & 天神購物")
        if os.path.exists("出國前最終確認：Day 2 (週一).jpg"):
            st.image("出國前最終確認：Day 2 (週一).jpg", use_column_width=True)
            
        st.markdown("##### <span class='time-badge'>08:00</span> 晨間散步：柳橋連合市場", unsafe_allow_html=True)
        st.write("飯店隔壁就是「博多的廚房」，長輩早起可去逛傳統市場買甜不辣當早餐 (視體力彈性安排)。")
        st.link_button("📍 導航：柳橋連合市場", "https://www.google.com/maps/search/?api=1&query=柳橋連合市場")
            
        st.markdown("##### <span class='time-badge'>08:30</span> 早餐 & 移動", unsafe_allow_html=True)
        st.write("吃飽後，搭地鐵至【天神站】，前往 2F/3F 的【西鐵福岡(天神)站】。")
            
        st.markdown("##### <span class='time-badge'>10:00</span> 前往太宰府 (西鐵電車)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>✨ 列車選擇攻略：</b><br>
        1. <b>直達車 (首選)：</b> 尋找平日早上直達太宰府的「旅人號」或直達急行，免轉乘！<br>
        2. <b>一般急行 (備案)：</b> 搭往大牟田方向，在 <b>【西鐵二日市站】</b> 下車，同月台/換月台轉太宰府線。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:45</span> 太宰府散策", unsafe_allow_html=True)
        st.write("🌸 必看亮點：藤本壯介設計的「臨時本殿」(漂浮森林屋頂) 與 3月盛開的飛梅。參道吃現烤梅枝餅。")
        st.info("💡 為了下午保留體力，建議放棄周邊需爬坡的九州博物館或竈門神社。")
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=太宰府天滿宮")
        
        st.markdown("##### <span class='time-badge'>14:30</span> 下午逛街：天神地下街 ➡ Mina 天神", unsafe_allow_html=True)
        st.write("搭西鐵回天神後，從地下街(免曬太陽/避雨)一路往北逛到 Mina 天神 (UNIQLO, LOFT)。")
        st.link_button("📍 導航：Mina 天神", "https://www.google.com/maps/search/?api=1&query=Mina+天神")
        
        st.markdown("##### <span class='time-badge'>18:20</span> 前往晚餐", unsafe_allow_html=True)
        st.warning("🚕 **強烈建議：** 逛完 Mina 天神後，直接搭計程車前往燒肉店 (車資約 ¥1000 出頭)，長輩會覺得您是最棒的導遊。")
        
        st.markdown("##### <span class='time-badge'>19:00</span> 晚餐：藥院燒肉 肉一", unsafe_allow_html=True)
        st.success("✅ 已預約：19:00 / 4 位 / 鄭又豪先生")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=薬院焼肉+肉一")

    # --- Day 3 ---
    elif "Day 3" in day:
        st.header("Day 3: 海豚相伴 & 天神北美食")
        if os.path.exists("出國前最終確認：Day 3 (週二) .jpg"):
            st.image("出國前最終確認：Day 3 (週二) .jpg", use_column_width=True)
        
        st.markdown("##### <span class='time-badge'>08:00</span> 飯店出發 (交通升級)", unsafe_allow_html=True)
        st.warning("🚕 **首選交通：** 絕對不要讓長輩走 20 分鐘！請直接在飯店叫計程車直達博多站 (約 ¥1000)。備案是走到柳橋站牌搭西鐵巴士。")
        
        st.markdown("##### <span class='time-badge'>08:25</span> 前往海之中道 (JR)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 博多站 1或2號月台 (鹿兒島本線) → <b>【香椎站】</b> (約08:30發)。<br>
        <b>Step 2 (⚠️):</b> 香椎站下車，<b>走天橋換到 4/5 號月台</b> (香椎線)。<br>
        <b>Step 3:</b> 搭 08:50~09:00 左右列車 → <b>【海之中道站】</b>。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>09:30</span> 福岡海洋世界 Marine World", unsafe_allow_html=True)
        st.success("🎫 門票預約：09:30 準時掃碼入場 (4 位成人)")
        st.write("黃金動線：先看沙丁魚風暴與企鵝，10:45 提早前往劇場找位子，**11:00 觀賞海豚秀**。午餐推薦館內水下玻璃餐廳！")
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=マリンワールド海の中道")
        
        st.markdown("##### <span class='time-badge'>14:30</span> 提早離開 & 返回市區", unsafe_allow_html=True)
        st.info("💡 體力衡量：若長輩累了，果斷放棄旁邊的海濱公園，直接搭 JR 返回天神 (可在千早站轉西鐵)。")
        
        st.markdown("##### <span class='time-badge'>15:30</span> 天神北購物", unsafe_allow_html=True)
        st.write("1. **Full Full 明太子法棍** (剛出爐必買)")
        st.link_button("📍 導航：Full Full 天神", "https://www.google.com/maps/search/?api=1&query=フルフル天神パン工房")
        st.write("2. **AEON Shoppers** (B1 超市買零食茶包伴手禮)")
        st.link_button("📍 導航：AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=イオンショッパーズ福岡店")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 晚餐：天麩羅 Hirao", unsafe_allow_html=True)
        st.info("策略：這家當地靈魂美食不能訂位！提早 17:20 去排隊避開下班人潮，必吃柚子花枝醃鹽辛！")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=天麩羅処ひらお+大名店")

    # --- Day 4 ---
    elif "Day 4" in day:
        st.header("Day 4: 門司港跨海 & 博多爆買")
        if os.path.exists("出國前最終確認：Day 4 (週三) .jpg"):
            st.image("出國前最終確認：Day 4 (週三) .jpg", use_column_width=True)
            
        st.info("💡 領隊廣播：早上務必帶實體信用卡去博多站領車票！轉乘全靠交通卡，請確保有千元餘額。")
        
        st.markdown("##### <span class='time-badge'>09:21</span> 去程：音速號 Sonic 11", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 09:21 → 小倉 10:10</b><br>
        座位：<span class="highlight">3 號車 3AB, 4AB</span> (記得轉椅子)
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:10</span> 小倉站去程轉乘 (先出再進神技)", unsafe_allow_html=True)
        if os.path.exists("kokura_transfer.jpg"):
            st.image("kokura_transfer.jpg", caption="下車後搭手扶梯上樓，準備執行轉乘動作", use_column_width=True)
        st.write("1. 放入「音速號車票」出閘門。 2. 轉身嗶「交通卡」進站。 3. 去 8 號月台搭普通車往門司港。")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 抵達門司港 & 跨海午餐", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>🌟 選項 A (推薦：下關側歷史巡禮)：</b><br>
        搭 11:00 聯絡船去唐戶市場 (2F吃海鮮定食) → 散步至日清講和紀念館 (馬關條約現場) & 赤間神宮 → <b>最晚搭 14:10 的船回門司港。</b><br>
        <hr style="margin:5px 0;">
        <b>🌟 選項 B (備案：留在門司港)：</b> 吃著名的「燒咖哩」。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=唐戸市場")
        st.link_button("📍 導航：日清講和紀念館", "https://www.google.com/maps/search/?api=1&query=日清講和記念館")
        st.link_button("📍 導航：赤間神宮", "https://www.google.com/maps/search/?api=1&query=赤間神宮")
        
        st.markdown("##### <span class='time-badge'>14:20</span> 門司港懷舊區散策", unsafe_allow_html=True)
        st.write("拍香蕉人、舊門司稅關休息、看藍翼橋開橋 (14:00/15:00)，去 Mooon de Retro 吃下午茶。")
        st.link_button("📍 導航：門司港車站", "https://www.google.com/maps/search/?api=1&query=門司港駅")
        
        st.markdown("##### <span class='time-badge'>16:30</span> 回程轉乘 (門司港 ➡ 小倉)", unsafe_allow_html=True)
        st.write("嗶交通卡進門司港站。抵達小倉後：1. 嗶交通卡出站。 2. 放入音速號車票進站！")
        
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
        <b>1. 博多銘品藏 (博多口)：</b> 買 <b>努努雞</b> (冷吃炸雞)。<br>
        <b>2. AMU PLAZA 1F：</b> 買 <b>AMANBERRY</b> (草莓夾心)。<br>
        <b>3. LOPIA 超市 (筑紫口 Yodobashi 4F)：</b> 買熟食/披薩回飯店開派對！
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=ロピア+博多ヨドバシ店")
        
        st.markdown("##### <span class='time-badge'>19:30</span> 回飯店", unsafe_allow_html=True)
        st.write("於筑紫口搭計程車回飯店享用超市大餐！")

    # --- Day 5 ---
    elif "Day 5" in day:
        st.header("Day 5: 熊本一日遊 & 頂級鰻魚")
        if os.path.exists("出國前最終確認：Day 5 (週四) .jpg"):
            st.image("出國前最終確認：Day 5 (週四) .jpg", use_column_width=True)
            
        st.info("💡 領隊廣播：大件行李留飯店，今天輕裝上陣！市電刷交通卡即可，免買一日券。")
        
        st.markdown("##### <span class='time-badge'>08:00</span> 飯店出發 & 買便當", unsafe_allow_html=True)
        st.write("搭計程車直達「博多站 筑紫口」。")
        st.markdown("""
        <div class="bento-box">
        <b>🍱 早餐任務：駅弁当 (Ekiben Station) 筑紫口店</b><br>
        進新幹線閘門前先買好鐵路便當，帶上新幹線吃。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：駅弁当 筑紫口店", "https://www.google.com/maps/search/?api=1&query=駅弁当+博多駅")
        
        st.markdown("##### <span class='time-badge'>08:30</span> 去程：新幹線 Mizuho 601", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 08:30 → 熊本 09:02</b><br>
        座位：<span class="highlight">5 號車 5AB, 6AB</span><br>
        備註：車程僅 32 分鐘，請盡情享用便當！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>09:40</span> 上午景點：城彩苑 & 熊本城", unsafe_allow_html=True)
        st.write("搭市電 A 系統到【熊本城・市役所前】。逛完城彩苑後，**務必搭免費接駁巴士**上去熊本城天守閣，保護長輩膝蓋！")
        st.link_button("📍 導航：櫻之馬場 城彩苑", "https://www.google.com/maps/search/?api=1&query=桜の馬場+城彩苑")
        st.link_button("📍 導航：熊本城", "https://www.google.com/maps/search/?api=1&query=熊本城")
        
        st.markdown("##### <span class='time-badge'>11:30</span> 午餐：勝烈亭豬排 (新市街本店)", unsafe_allow_html=True)
        st.write("提早抵達避開上班族人潮，必點「六白黑豚」炸豬排定食，肉質軟嫩。")
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=勝烈亭+新市街本店")
        
        st.markdown("##### <span class='time-badge'>13:30</span> 午後散策：下通商店街 & 尋找熊本熊", unsafe_allow_html=True)
        st.write("一路逛到鶴屋百貨。若想看熊本熊部長本尊，請提早在 14:30 去辦公室卡位。")
        st.link_button("📍 導航：熊本熊部長辦公室", "https://www.google.com/maps/search/?api=1&query=Kumamon+Square")
        
        st.markdown("##### <span class='time-badge'>17:00</span> 熊本車站採買：肥後よかモン市場", unsafe_allow_html=True)
        st.write("搭市電回熊本站，進站前在改札口正對面的市場買 **熊本熊圓形便當 (空盒可微波)** 或阿蘇赤牛便當當宵夜。")
        st.link_button("📍 導航：肥後よかモン市場", "https://www.google.com/maps/search/?api=1&query=肥後よかモン市場")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 回程：新幹線 Tsubame 328", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>熊本 17:20 → 博多 18:09</b><br>
        座位：<span class="highlight">5 號車 6AB, 7AB</span><br>
        備註：燕子號木質內裝極美，提早回博多從容吃晚餐。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:50</span> 終極晚餐：吉塚鰻魚屋", unsafe_allow_html=True)
        st.write("博多口搭計程車直達。福岡第一的百年老店，點「鰻重」享受極致酥脆與軟嫩的口感！")
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=吉塚うなぎ屋")

    # --- Day 6 ---
    elif "Day 6" in day:
        st.header("Day 6: 甜點衝刺 & 滿載而歸")
        if os.path.exists("出國前最終確認：Day 6 (週五) .jpg"):
            st.image("出國前最終確認：Day 6 (週五) .jpg", use_column_width=True)
            
        st.warning("⚠️ **行李大魔王提醒：** 明太子與果凍屬於液體膏狀，必須放進托運行李！")
        
        st.markdown("##### <span class='time-badge'>07:30</span> 早鳥專屬：柳橋連合市場", unsafe_allow_html=True)
        st.write("長輩若早起，可去旁邊市場買手工甜不辣或感受早晨活力。")
        
        st.markdown("##### <span class='time-badge'>08:50</span> 辦理退房", unsafe_allow_html=True)
        st.write("整理大件行李，寄放於一樓櫃台 (Luggage keep)，帶隨身小包出門衝刺。")
        
        st.markdown("##### <span class='time-badge'>09:10</span> 甜點任務：I'm donut ? (天神店)", unsafe_allow_html=True)
        st.write("福岡最紅生甜甜圈。**戰術：** 年輕人排隊，請長輩去對面大丸百貨坐著等。若人太多直接進大丸 B2 買地下街高級和菓子。")
        st.link_button("📍 導航：I'm donut ? 天神店", "https://www.google.com/maps/search/?api=1&query=I'm+donut+天神店")
        st.link_button("📍 導航：大丸福岡天神店", "https://www.google.com/maps/search/?api=1&query=大丸福岡天神店")
        
        st.markdown("##### <span class='time-badge'>10:20</span> 返回飯店領行李 & 叫車赴機場", unsafe_allow_html=True)
        st.error("🛑 **絕對不要搭地鐵！** 請直接請飯店叫計程車去「福岡空港 國際線」，只需 15-20 分鐘，免去轉接駁巴士的地獄。")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 機場報到 & 免稅店大採購", unsafe_allow_html=True)
        st.write("長榮航空報到托運後，進免稅店鎖定：**福砂屋長崎蛋糕、保冷袋明太子**。")
        
        st.markdown("##### <span class='time-badge'>12:15</span> 班機起飛 (BR105)", unsafe_allow_html=True)
        st.write("滿載而歸！13:50 降落桃園機場 T2。慢慢拿行李出關，搭機捷至桃園高鐵站。")
        
        st.markdown("##### <span class='time-badge'>16:34</span> 平安返家：高鐵 841 車次", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>桃園 16:34 → 台中 17:15</b><br>
        班次：841 車次<br>
        備註：時間非常充裕，可在高鐵站喝咖啡休息，圓滿結束北九州行！
        </div>
        """, unsafe_allow_html=True)

# === Tab 2: 購物清單 ===
with tab2:
    st.header("🛍️ 採買檢核表")
    
    st.subheader("📍 博多站 (Day 4 必買)")
    st.checkbox("努努雞 (Ming/銘品藏) - 冷著吃！ 🍗")
    st.checkbox("AMANBERRY 草莓夾心 (AMU 1F) 🍓")
    st.checkbox("LOPIA 熟食/披薩 (筑紫口 Yodobashi 4F)")
    
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
        st.checkbox("福砂屋 長崎蛋糕 (機場)")
        st.checkbox("明太子 (需托運)")
        st.checkbox("熊本熊便當 (空盒)")

# === Tab 3: 車票與預約 ===
with tab3:
    st.header("🎫 票券管理中心 (已全數確認)")
    
    st.markdown("### ✅ Day 3: 海洋世界門票 (已購買)")
    st.success("🎫 預約入場：09:30 (4 位成人)")
    
    st.markdown("### ✅ Day 4: 音速號 (已購買)")
    st.success("博多 ↔ 小倉 (記得帶刷卡用實體信用卡領票)")
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
    
    st.markdown("### ✅ Day 6: 台灣高鐵 (已購買)")
    st.success("桃園 ↔ 台中")
    st.markdown("""
    <div class="ticket-box">
    <b>車次 (841):</b> 16:34 → 17:15<br>
    備註：桃園機場 T2 搭機捷前往高鐵站。
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🍽️ 餐廳預約")
    st.success("藥院燒肉 肉一：3/2 19:00 (4人)")
    st.caption("預約大名：鄭又豪 先生")
