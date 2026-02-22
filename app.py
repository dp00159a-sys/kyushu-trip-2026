import streamlit as st
import os
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --------------------------
# 1. App 基礎設定
# --------------------------
st.set_page_config(
    page_title="2026 北九州行",
    page_icon="APP圖示.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自訂 CSS：原版清爽配色 (適合淺色模式)
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
    .account-box {
        background-color: #F9EBEA;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #C0392B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎌 2026 北九州行")
st.caption("Family Trip: 2026/3/1 (日) - 3/6 (五) | 全數票券與詳細動線已鎖定 ✅")

# --------------------------
# 2. 核心分頁
# --------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📅 詳細行程", "🛍️ 購物清單", "🎫 車票與預約", "💰 旅費與記帳"])

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
            
        st.info("""
        💡 **出發前溫馨提醒 (領隊廣播)：**
        請務必提醒家人要帶上「日本的交通卡」(Suica、ICOCA 等)。雖然現場買實體票也可以，但帶著長輩拉行李，能直接「嗶」卡進出站，絕對會讓旅程一開始就順暢無比！
        """)
        
        st.markdown("##### <span class='time-badge'>12:00</span> 【台灣出發】前往機場", unsafe_allow_html=True)
        st.write("**動作：** 從高鐵台中站出發。搭乘 **630 車次 (12:00 發車)** 前往高鐵桃園站，轉乘機捷抵達航廈。")
        st.write("**航班：** 長榮航空 BR102 (桃園機場 T2 / 16:25 準時起飛)。")
        
        st.markdown("##### <span class='time-badge'>19:55</span> 【抵達日本】福岡機場出關與接駁", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>🚌 機場移動動線 (重要更新)：</b><br>
        1. 拿好行李出關後，請尋找並從 <b>「A3 出口」</b> 離開航廈。<br>
        2. 出 A3 出口後 <b>「往右邊走」</b>，就會看到前往國內線航廈的「免費接駁巴士」站牌。<br>
        3. <b>搭乘接駁巴士 (車程約 10 分鐘)</b>，巴士會直接載您抵達國內線航廈的「福岡機場地鐵站」入口。
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🎥 機場實景走法參考影片 (從下飛機到搭巴士)"):
            st.video("https://www.youtube.com/watch?v=pRwDSFJskzQ")
        
        st.markdown("##### <span class='time-badge'>21:20</span> 【市區移動】地鐵轉乘 (機場 ➡ 飯店)", unsafe_allow_html=True)
        st.write("**進站：** 拿出準備好的交通卡 (Suica/ICOCA) 感應進站。")
        st.markdown("""
        <div class="route-box">
        <b>第一段：福岡市地下鐵 空港線 (Kuko Line)</b><br>
        從【福岡機場站】搭乘地下鐵空港線（往姪濱/唐津方向）。搭乘 2 站在 <b>【博多站】</b> 下車。<br><br>
        <b>🚶 博多站內轉乘動線：</b><br>
        在博多站下車後，請跟著綠色指標 <b>「七隈線 (Nanakuma Line)」</b> 走。<br>
        這段連通道設有<b>「電動步道」</b>，請讓長輩站上去順順地滑過去，慢慢走大約需要 6 分鐘。<br><br>
        <b>第二段：福岡市地下鐵 七隈線 (Nanakuma Line)</b><br>
        走到七隈線月台後，搭乘往「橋本」方向的列車。<br>
        僅搭乘 1 站，在 <b>【渡邊通站 (Watanabedori)】</b> 下車。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>22:00</span> 【飯店入住】Cross Life 博多柳橋", unsafe_allow_html=True)
        st.write("**車站出口指引：**")
        st.write("在【渡邊通站】下車後，請務必尋找 **「2號出口」**！為什麼選這出口？因為 2 號出口有 **「手扶梯」**，絕對不要讓家人第一天就扛行李爬樓梯。")
        st.write("**步行至飯店：**")
        st.write("從 2 號出口一到地面，**直接左轉**。往前走會過一座小橋（橋下是那珂川），過橋後馬上就會看到飯店在您的右手邊。")
        st.link_button("📍 導航：Cross Life 博多柳橋", "https://www.google.com/maps/search/?api=1&query=Cross+Life+博多柳橋")
        
        st.markdown("##### <span class='time-badge'>22:30</span> 【夜間補給】Sunny 超市 (24小時營業)", unsafe_allow_html=True)
        st.write("**地點：** 飯店附近的 Sunny 超市 (渡邊通店)。")
        st.write("**採買任務：** 大瓶裝礦泉水 (2L)、博多甘王草莓 (九州必吃宵夜)、優格/牛奶，以及若隔日不想排隊名店可先買好的早餐備品。")
        st.link_button("📍 導航：Sunny 超市 渡邊通店", "https://www.google.com/maps/search/?api=1&query=Sunny+渡邊通店")

    # --- Day 2 ---
    elif "Day 2" in day:
        st.header("Day 2: 太宰府賞梅 & 天神購物")
        st.caption("今日核心目標：早上看限定版神殿與梅花，下午逛街，晚上吃和牛燒肉！")
        if os.path.exists("出國前最終確認：Day 2 (週一).jpg"):
            st.image("出國前最終確認：Day 2 (週一).jpg", use_column_width=True)
            
        st.markdown("##### <span class='time-badge'>08:00</span> 【晨間散步】柳橋連合市場 (視體力彈性安排)", unsafe_allow_html=True)
        st.write("**出發：** 從飯店走出來約 2 分鐘即達「博多的廚房」。")
        st.write("**看點：** 早上市場最有活力，可以看在地海鮮、買個現做的魚漿天婦羅（甜不辣）或玉子燒當早點。")
        st.info("💡 **備註：** 如果長輩想睡晚一點，這個點可以隨時取消，或是移到 Day 6 早上。")
        st.link_button("📍 導航：柳橋連合市場", "https://www.google.com/maps/search/?api=1&query=柳橋連合市場")
            
        st.markdown("##### <span class='time-badge'>08:30</span> 【早餐】在地暖胃湯麵 或 輕鬆吃", unsafe_allow_html=True)
        st.write("視長輩早上的胃口，從以下三個方案靈活挑選：")
        st.markdown("""
        * **選項 A (🌟 在地暖胃首選)：麺処・三喜春吉 本店**
          距離飯店非常近！早上帶長輩來吃碗熱騰騰的烏龍麵或蕎麥麵，暖胃又舒服，是在地人也很愛的早餐選擇。
        * **選項 B (網美挑戰)：DACOMECCA 麵包店**
          博多站旁超人氣排隊名店，需搭地鐵過去排隊，適合喜歡嚐鮮的年輕人。
        * **選項 C (輕鬆路線)：周邊超市或超商**
          直接在飯店附近吃麥當勞、超商，或去超市買小吃墊墊胃。
        """)
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("📍 導航：三喜春吉 本店", "https://maps.app.goo.gl/eY1B8GeZ2wA84xZp9")
        with col2:
            st.link_button("📍 導航：飯店周邊超市備案", "https://maps.app.goo.gl/DuySWvfGregfzPVN9")
        
        st.markdown("##### <span class='time-badge'>09:00</span> 【景點】櫛田神社", unsafe_allow_html=True)
        st.write("**動線：** 吃飽後前往櫛田神社參拜，這裡是博多總鎮守，有巨大的裝飾山笠可以看。")
        st.link_button("🗺️ 路線：住宿地 ➡ 櫛田神社", "https://maps.app.goo.gl/aJ2i48juTxBv3sd16")
            
        st.markdown("##### <span class='time-badge'>09:40</span> 【市區移動】前往西鐵天神站", unsafe_allow_html=True)
        st.write("**動線：** 參拜完後，前往西鐵福岡(天神)站準備搭車。沿著地下街的指標，往上走到 2F/3F 的【西鐵福岡(天神)站】。")
        st.link_button("🗺️ 路線：櫛田神社 ➡ 西鐵福岡(天神)站", "https://maps.app.goo.gl/3UNNjEkgfMiTyCjq5")
            
        st.markdown("##### <span class='time-badge'>10:00</span> 【前往太宰府】搭乘西鐵電車", unsafe_allow_html=True)
        st.write("**交通方式：** 直接刷實體交通卡進站 (Suica/ICOCA)。不用買套票！")
        st.link_button("🗺️ 路線：西鐵福岡(天神)站 ➡ 太宰府", "https://maps.app.goo.gl/WRuenQ4sic7QknZS9")
        st.markdown("""
        <div class="route-box">
        <b>✨ 列車選擇攻略 (西日本鐵道 Nishitetsu)：</b><br>
        1. <b>直達車 (首選)：</b> 平日早上 (約 09:46 左右，依現場班表為準) 尋找直達太宰府的<b>「旅人號 (Tabito)」或直達急行</b>，如果遇到，請直接跳上去，不用換車！<br>
        2. <b>一般急行 (備案)：</b> 如果沒遇到直達車，就搭「天神大牟田線」往大牟田方向的特急/急行，在 <b>【西鐵二日市站】</b> 下車，同月台或換月台轉搭「西鐵太宰府線」。
        </div>
        """, unsafe_allow_html=True)

        with st.expander("🎥 太宰府交通與行程參考影片 (點擊展開)"):
            st.markdown("""
            * 🌟 **主要推薦：** [福岡&太宰府美食之旅｜⛩️太宰府天滿宮交通攻略](https://www.youtube.com/watch?v=0jVJzLYuCuk)
            * **次要推薦：** [到福岡觀光必去景點太宰府天滿宮 參拜與美食散步](https://www.youtube.com/watch?v=UnXoxvTQzvo)
            """)
        
        st.markdown("##### <span class='time-badge'>10:45</span> 【太宰府散策】賞梅與參拜", unsafe_allow_html=True)
        st.markdown("""
        * **必看亮點 1：** 期間限定「臨時本殿」 (漂浮森林屋頂，非常特別！)。
        * **必看亮點 2：** 3 月初正值太宰府的梅花季，整個天滿宮會有粉白相間的梅花，非常適合幫長輩拍照。
        """)
        st.info("💡 **備用景點 (強烈建議 PASS)：** 九州國立博物館或光明禪寺/竈門神社距離較遠需爬坡或轉公車。為了下午逛街保留體力，強烈建議直接 PASS！")
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=太宰府天滿宮")

        st.markdown("##### <span class='time-badge'>12:00</span> 【午餐與點心彈性安排】太宰府美食圖鑑", unsafe_allow_html=True)
        st.write("參道上美食眾多，您可以視長輩當下的胃口與排隊人潮，從以下清單自由挑選（若人太多，就搭車回天神再吃正餐）：")
        
        st.markdown("🍱 **【鹹食與正餐推薦】**")
        st.markdown("""
        * **福太郎 太宰府店：** 喜歡米飯的長輩首選！招牌是「明太子烤飯糰」與明太子茶泡飯（めんたいボウル），熱呼呼的非常暖胃。
        * **YAMAYA BASE 太宰府：** 主打明太子輕食！必吃熱騰騰的「明太子法國麵包」跟酥脆的明太子炸雞，適合不想吃太飽的時候。
        * *(原備案)* 一蘭拉麵（太宰府限定合格五角形碗）或 暖暮拉麵。
        """)
        col3, col4 = st.columns(2)
        with col3:
            st.link_button("📍 導航：福太郎 太宰府店", "https://maps.app.goo.gl/F1qeeGWbN7Ax1iCr8")
        with col4:
            st.link_button("📍 導航：YAMAYA BASE", "https://maps.app.goo.gl/btwPzM5aTmoiSqG98")

        st.markdown("🍵 **【甜點與長輩休息好去處】**")
        st.markdown("""
        * **咖啡·梅枝餅 松屋 (Matsuya)：** 🌟 **強烈推薦帶長輩來！** 這裡不僅能吃現烤梅枝餅配咖啡，最棒的是店內深處有一個非常漂亮的「日式中庭花園」，可以讓長輩坐著悠哉賞景休息，避開參道人潮。
        * **草莓最中·大福 天山 本店：** 打卡必吃！超巨大的甘王草莓夾在「鬼瓦最中」或大福裡，酸甜解膩，視覺跟味覺都滿分。
        """)
        col5, col6 = st.columns(2)
        with col5:
            st.link_button("📍 導航：咖啡·梅枝餅 松屋", "https://maps.app.goo.gl/1J98ZsPpm8fYQBTv7")
        with col6:
            st.link_button("📍 導航：天山 本店", "https://maps.app.goo.gl/1kM6ic3THcrJWPnN7")

        st.markdown("##### <span class='time-badge'>14:30</span> 【下午逛街】天神地下街 ➡ Mina 天神", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：太宰府 ➡ Mina 天神", "https://maps.app.goo.gl/VidKxg6SQzkzp3Va6")
        st.write("**動線 (不曬太陽/不淋雨)：** 搭西鐵回天神後，直接鑽進【天神地下街】。這裡有洗手間、椅子可休息，還能買 BAKE 起司塔、RINGO 蘋果派。一路往北走到底，直接連通【Mina 天神】。")
        st.write("**主力戰場 (Mina 天神)：** UNIQLO (九州最大旗艦店)、GU、LOFT、Seria (百元店)。長輩可以坐在服飾店的沙發區等您結帳。")
        
        st.info("""
        💡 **領隊明太子雷達：**
        您們現在所在的「Mina 天神」距離 **《Full Full》天神店** 非常近（步行約 3 分鐘）！如果長輩逛街時想吃點點心，或是想先買傳說中的「明太子法國麵包」當明天的早餐，推薦趁現在順路去買買看！
        """)
        st.link_button("🍞 順路導航：《Full Full》天神店", "https://maps.app.goo.gl/Kx3dmDgkdGHVp24K9")
        
        st.markdown("##### <span class='time-badge'>18:20</span> 【前往晚餐】兩種移動方案", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：Mina 天神 ➡ 藥院燒肉 肉一", "https://maps.app.goo.gl/tuiCUiYwKxf2w82n7")
        st.markdown("""
        <div class="route-box">
        這時候您們人在 Mina 天神 (天神最北邊)，但餐廳在藥院 (偏南邊)。<br><br>
        <b>方案 A (您的提議 - 搭西鐵)：</b> 沿著地下街慢慢走回【西鐵天神站】，搭一站到【西鐵藥院站】，再走 3-5 分鐘到餐廳。(缺點：要先走回天神站，這段路對走了一下午的長輩來說有點折磨)。<br><br>
        <b>方案 B (🚕 我的強烈建議 - 搭計程車)：</b> 逛完 Mina 天神，直接請百貨櫃檯幫忙叫車，或是走到大馬路上攔車。4 個人平分車資約 ¥1,000 日圓出頭，直達燒肉店門口，長輩會覺得您是世界上最棒的導遊。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>19:00</span> 【重頭戲晚餐】藥院燒肉 肉一 (Yakiniku Nikuichi)", unsafe_allow_html=True)
        st.success("✅ 確認事項：已預約 19:00 / 4 位 / 鄭又豪先生。")
        st.write("**必點：** 豪華黑毛和牛拼盤、盛岡冷麵 (解膩神物)。如果長輩牙口不好，這家肉質很軟嫩，絕對沒問題。")

        st.markdown("##### <span class='time-badge'>21:00</span> 【返回飯店】", unsafe_allow_html=True)
        st.write("**交通：** 餐廳門口直接搭計程車回 Cross Life 博多柳橋（超近，起步價左右就到了），結束完美的一天。")

    # --- Day 3 ---
    elif "Day 3" in day:
        st.header("Day 3: 海豚相伴 & 天神北美食")
        st.caption("今日核心目標：09:30 準時入園、看海豚秀、順利買到明太子法棍、提早排隊吃天麩羅！")
        if os.path.exists("出國前最終確認：Day 3 (週二) .jpg"):
            st.image("出國前最終確認：Day 3 (週二) .jpg", use_column_width=True)
        
        st.markdown("##### <span class='time-badge'>08:00</span> 【飯店出發】前往博多車站 (交通升級)", unsafe_allow_html=True)
        st.write("**早餐建議：** 因為要提早出發，建議前一晚在 Sunny 超市買好早餐，在飯店房間悠哉吃完再下樓。")
        st.info("""
        💡 **領隊早餐雷達 (備用)：**
        如果長輩這天起得特別早，可以搭計程車直接殺去博多站 B1 的 **「たんやHAKATA」** 吃超划算的牛舌明太子當早餐！吃完剛好搭 08:30 的車。（若想多睡一點，就維持原案吃超商麵包）。
        """)
        st.markdown("""
        🚕 **首選交通 (計程車)：** 絕對不要讓長輩走 20 分鐘去博多站！早上走這一段到水族館就累了。請直接在飯店叫車直達博多站博多口 (約 ¥1000 左右，完全不用走路)。
        🚌 **備案交通 (西鐵巴士)：** 走到飯店外大馬路上的「柳橋」公車站牌，搭乘前往博多站的西鐵巴士。
        """)
        st.link_button("🗺️ 路線：住宿地 ➡ 海洋世界海之中道", "https://maps.app.goo.gl/VLqBvFM5QqudXBye7")
        
        st.markdown("##### <span class='time-badge'>08:25</span> 【前往海之中道】JR 轉乘", unsafe_allow_html=True)
        st.write("**進站找月台：** 從博多口走進車站，刷交通卡進 JR 閘門。尋找往「小倉、門司港、福間」方向的 **JR 鹿兒島本線 (Kagoshima Main Line)** (通常在 1 號或 2 號月台)。")
        st.markdown("""
        <div class="route-box">
        <b>第一段：博多 ➡ 香椎 (JR 鹿兒島本線)</b><br>
        搭乘 08:30 左右發車的「快速」或「普通」列車 → <b>【香椎站 (Kashii)】</b> (車程 10-15 分鐘)。<br><br>
        <b>⚠️ 關鍵轉乘：香椎站 換月台</b><br>
        在香椎站下車後，<b>必須走樓梯/電梯上天橋</b>，跟著藍色指標或地上畫的藍線，換到 <b>4 號或 5 號月台</b>。<br><br>
        <b>第二段：香椎 ➡ 海之中道 (JR 香椎線 / 海之中道線)</b><br>
        搭乘 08:50~09:00 左右往「西戶崎」的列車 → <b>【海之中道站】</b> (車程約 20 分鐘)。出站後跟著人群走，水族館就在旁邊。
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🎥 海之中道搭車實景走法參考影片 (點擊展開)"):
            st.markdown("* [帶您從博多車站搭電車前往 海洋世界海之中道](https://www.youtube.com/watch?v=G5a76LMrDPI)")
        
        st.markdown("##### <span class='time-badge'>09:30</span> 【水族館】福岡海洋世界 Marine World", unsafe_allow_html=True)
        st.success("🎫 門票預約：09:30 預約場次 (4 位成人)。準備好手機憑證直接掃碼入場。")
        st.markdown("""
        * **09:30 - 10:30 (黃金動線)：** 趁人少先去逛「全景大水槽」（看鯊魚和沙丁魚）、海豹區、企鵝區。
        * **10:45 (提早佔位)：** 提早前往「海豚表演劇場」找個視野好、不用曬太陽的位子坐下休息。
        * **11:00 (海豚表演)：** 觀賞精彩的海豚與海獅秀。
        * **午餐安排：** 表演結束後，可直接在館內的「Reilly 餐廳」用餐，這家餐廳可以在水下玻璃旁一邊看海豚游泳一邊吃飯，長輩一定喜歡！
        """)
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=マリンワールド海の中道")
        
        st.markdown("##### <span class='time-badge'>13:30</span> 【彈性評估】海濱公園 或 提早回市區", unsafe_allow_html=True)
        st.info("💡 **領隊當下判斷：** 海濱公園非常大，光是走到花海區就要走很久。強烈建議果斷放棄公園，保留體力慢慢走回 JR 車站，搭車回市區 (可在【千早站】下車轉搭西鐵回天神)。")
        
        st.markdown("##### <span class='time-badge'>15:30</span> 【下午逛街】天神北商圈大採買", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：海之中道 ➡ Mina 天神", "https://maps.app.goo.gl/7kneK1btSUQ92DvR6")
        st.markdown("""
        * **1. Full Full 天神店：** 必買九州最有名的「明太子法國麵包」！如果昨天 (Day 2) 經過時沒買到，今天趁著去 AEON 超市前，務必拿下它！買回飯店當宵夜/早餐都超讚。
        * **2. AEON Shoppers 福岡店：** 這是一整棟的大型超市與商場。B1 的超市非常好買，可以讓長輩採購零食、茶包、調味料等體積小、重量輕的伴手禮。
        """)
        st.link_button("📍 導航：Full Full 天神", "https://www.google.com/maps/search/?api=1&query=フルフル天神パン工房")
        st.link_button("📍 導航：AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=イオンショッパーズ福岡店")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 【重頭戲晚餐】天麩羅處 Hirao (大名店)", unsafe_allow_html=True)
        st.write("**策略：** 這家是福岡當地人的靈魂美食，**不能訂位！** 如果 18:30 下班時間才去，絕對會排隊排到懷疑人生。17:20 抵達可以大幅縮短排隊時間。")
        st.write("**必吃特色：** 買好食券入座後，師傅現炸放到您盤子裡。桌上免費無限續加的**「柚子花枝醃鹽辛 (いかの塩辛)」**才是本體，超級下飯！")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=天麩羅処ひらお+大名店")

        st.markdown("##### <span class='time-badge'>19:00</span> 【返回飯店】", unsafe_allow_html=True)
        st.write("**交通：** 吃飽喝足後，長輩今天也走了不少路。強烈建議直接在大馬路 (國體道路) 上攔計程車回 Cross Life 飯店。")
        st.link_button("🗺️ 路線：天神南 ➡ 住宿飯店", "https://maps.app.goo.gl/vV41q2DNK4nfKgJd7")

    # --- Day 4 ---
    elif "Day 4" in day:
        st.header("Day 4: 門司港跨海 & 博多爆買")
        st.caption("今日核心目標：小倉無痛轉乘、唐戶市場吃海鮮/歷史巡禮、博多精準採買！")
        if os.path.exists("出國前最終確認：Day 4 (週三) .jpg"):
            st.image("出國前最終確認：Day 4 (週三) .jpg", use_column_width=True)
            
        st.info("""
        💡 **領隊晨間廣播 (出發前必確認)：**
        1. **實體信用卡必帶：** 早上到博多站的第一件事，就是去機台領取「音速號」車票，必須帶當初刷的那張實體信用卡！
        2. **交通卡必帶：** 今天的轉乘策略已改為「全自動化」，不用跟站務員講話，交通卡請確保有 1,000 日圓的餘額。
        """)
        
        st.markdown("##### <span class='time-badge'>08:15</span> 【神級早餐備案】たんやHAKATA (牛舌屋)", unsafe_allow_html=True)
        st.write("**地點：** 博多站 B1「博多1番街」內。")
        st.write("**亮點：** 福岡超人氣的排隊早餐！招牌「牛舌定食」香氣逼人，強烈建議加點**「明太子與生雞蛋套餐」**，一次把福岡必吃的牛舌與明太子收集齊全！")
        st.write("**時間精算：** 吃完剛好上樓去綠色機台領取 09:21 發車的音速號車票，吃飽喝足再出發！")
        st.link_button("📍 導航：たんやHAKATA (博多1番街)", "https://maps.app.goo.gl/zJJmvTz58y1DgheV8")

        st.markdown("##### <span class='time-badge'>09:00</span> 【抵達車站】博多站 JR 線領票與進站", unsafe_allow_html=True)
        st.write("**搭乘路線：** JR 鹿兒島本線 (Kagoshima Main Line)。")
        st.write("**動作：** 到博多站一樓大廳，尋找綠色招牌的「JR 九州 (JR KYUSHU)」售票處（綠色機台 みどりの券売機）領取實體車票。")
        st.write("**進站入口：** 請尋找 **「中央改札口」或「北改札口」** 進入一般 JR 線（⚠️ 千萬不要走到「新幹線」的閘門喔！）。")
        st.write("**找月台：** 進站後抬頭看電子看板，尋找往「小倉、大分」方向的特急列車（特急ソニック），通常會在 2 號或 3 號月台。")
        st.link_button("🗺️ 路線：博多車站 ➡ 小倉車站", "https://maps.app.goo.gl/98UeENt9L5fdeYYd9")
        
        st.markdown("##### <span class='time-badge'>09:21</span> 【去程】音速號 Sonic 11 (博多 ➡ 小倉)", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 09:21 → 小倉 10:10</b><br>
        座位：<span class="highlight">3 號車 3AB, 4AB</span><br>
        ⚠️ <b>重要動作：</b> 找到座位後，記得踩著椅子下方的踏板，<b>把其中一排椅子轉向</b>，讓全家人可以面對面坐著聊天看風景！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:10</span> 【去程關鍵轉乘】小倉站 (無痛轉乘：先出再進)", unsafe_allow_html=True)
        if os.path.exists("kokura_transfer.jpg"):
            st.image("kokura_transfer.jpg", caption="下車後搭手扶梯上樓，走到出站閘門切換票券", use_column_width=True)
        st.link_button("🗺️ 路線：小倉車站 ➡ 門司港", "https://maps.app.goo.gl/Di2YNWiHU2FrLmgp9")
        st.write("為避免語言不通的補票困擾，請執行以下無痛轉乘動作：")
        st.write("**1. 出站：** 下車後搭手扶梯上樓，走到出站閘門。把您手上的**「音速號車票」放入機器**，機器收走車票出站。")
        st.write("**2. 進站：** 在閘門外轉個身，立刻拿出**「實體交通卡 (Suica/ICOCA)」**，嗶卡重新進站！")
        st.write("**3. 換月台：** 進站後尋找**「鹿兒島本線 (往門司港)」**指標（通常 8 號月台），搭乘普通/快速列車 (約 10-15 分鐘一班)。")

        with st.expander("📚 門司港交通與行程攻略包 (點擊展開)"):
            st.markdown("""
            * 🌟 **圖文轉乘詳解：** [Dcard 北九州交通分享](https://www.dcard.tw/f/japan_travel/p/259610237)
            * 🎥 **行程與交通參考 1：** [福岡前往北九州交通＋動線安排完整攻略](https://www.youtube.com/watch?v=OGWe5jL9Lq4)
            * 🎥 **行程與交通參考 2：** [小倉門司港美食景點交通一次看](https://www.youtube.com/watch?v=2GU-jQCnJ-4&t=227s)
            * 🎥 **行程與交通參考 3：** [北九州門司港一日遊！景點/美食/交通攻略](https://www.youtube.com/watch?v=2AypnBipqeI)
            * 🎥 **門司港交通實戰參考：** [九州自由行#3 門司港下關一日遊📍門司港交通](https://www.youtube.com/watch?v=TDS4yq6kjVk&t=225s)
            """)
        
        st.markdown("##### <span class='time-badge'>10:45</span> 【抵達門司港】大正浪漫之旅起點", unsafe_allow_html=True)
        st.write("**出站：** 直接用交通卡「嗶」出站（自動扣款約 280 日圓），完全免講話。")
        st.write("**第一站 (JR 門司港車站)：** 一出站就是日本重要文化財的百年木造車站，記得拍攝大正時期的復古月台與新文藝復興風格外觀。裡面有超美的復古星巴克可上廁所。")
        st.link_button("📍 導航：門司港車站", "https://www.google.com/maps/search/?api=1&query=門司港駅")
        
        st.markdown("##### <span class='time-badge'>11:00</span> 【午餐與跨海路線選擇】(雙備案)", unsafe_allow_html=True)
        st.write("請視當下長輩體力與天氣，彈性選擇 A 或 B 路線：")
        st.markdown("""
        <div class="route-box">
        <b>🌟 選項 A (推薦主線：跨海吃海鮮與歷史巡禮 - 下關側)：</b><br>
        1. <b>前往碼頭搭船：</b> 走 2 分鐘到「門司港棧橋」。買票搭前往「下關（唐戶）」的聯絡船 (單程 ¥400，航程僅 5 分鐘)。<br>
        2. <b>唐戶市場 (11:15)：</b> 下船右轉走 3 分鐘。今天是週三無屋台，請帶長輩直接上 <b>二樓的「海轉唐戶市場壽司」或定食餐廳</b> 舒服坐著吃。<br>
        3. <b>歷史巡禮 (12:45)：</b> 散步 5-7 分鐘至<b>「日清講和紀念館 (春帆樓)」</b> (李鴻章與伊藤博文簽署馬關條約的歷史現場，免費參觀) 以及旁邊有龍宮造型大門的<b>「赤間神宮」</b>。<br>
        4. <b>🚢 關鍵回程船班：</b> 為了不耽誤下午行程，請最晚搭上 <b>14:10</b> 的船回門司港。<br>
        <hr style="margin:5px 0;">
        <b>🌟 選項 B (備用輕鬆版：留在門司港吃名物)：</b><br>
        如果風浪大或不想搭船，直接留在門司港吃名物<b>「燒咖哩 (烤咖哩)」</b>。車站附近的「Bear Fruits」或「Princess Phi Phi」都是好選擇，香濃咖哩配焗烤起司非常美味。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=唐戸市場")
        st.link_button("📍 導航：日清講和紀念館", "https://www.google.com/maps/search/?api=1&query=日清講和記念館")
        st.link_button("📍 導航：赤間神宮", "https://www.google.com/maps/search/?api=1&query=赤間神宮")
        
        st.markdown("##### <span class='time-badge'>14:20</span> 【午後散策】門司港懷舊區經典巡禮", unsafe_allow_html=True)
        st.write("沿著海港邊的平路慢慢散步拍照：")
        st.write("1. **舊大阪商船大樓 & 舊門司稅關：** 西洋風味百年建築，稅關內部有免費的休息空間可坐。")
        st.write("2. **藍翼橋 (Blue Wing Moji)：** 日本最大行人專用吊橋。橋面會在 14:00 和 15:00 打開，記得卡位看開橋！")
        st.write("3. **海峽廣場 (KAIKYO PLAZA)：** 伴手禮聚集地，**必拍著名的「香蕉人」雕像**。")
        st.write("4. **下午茶時光 (15:30)：** 逛累了去網美愛店 **「Mooon de Retro」** 吃華麗水果聖代，順便上廁所準備搭車。")
        
        st.markdown("##### <span class='time-badge'>16:30</span> 【回程轉乘】門司港 ➡ 小倉 (JR 鹿兒島本線)", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：門司港 ➡ 小倉車站", "https://maps.app.goo.gl/EZrm7WS4Lcsrj3BN8")
        st.write("**搭車位置：** JR 門司港車站是終點站，任何一個月台發車的普通或快速列車，全都會沿著「JR 鹿兒島本線」開往小倉，看到車就可以上。")
        st.write("**16:30：** **嗶交通卡進站**，搭乘普通車回小倉 (約 16:45 抵達)。")
        st.write("**無痛轉乘動作 (與早上相反)：**")
        st.write("1. 抵達小倉後，上樓到出站閘門，**嗶交通卡出站** (扣款結清門司港到小倉的車資)。")
        st.write("2. 拿出您的**「小倉 ➡ 博多」音速號車票**，放入機器重新進 JR 閘門。尋找往博多方向的特急月台（通常在 4 號或 7 號月台）。")
        
        st.markdown("##### <span class='time-badge'>17:06</span> 【回程】音速號 Sonic 42 (小倉 ➡ 博多)", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：小倉車站 ➡ 博多車站", "https://maps.app.goo.gl/TrgCs6hfxqbpb2Tm8")
        st.markdown("""
        <div class="ticket-box">
        <b>小倉 17:06 → 博多 17:49</b><br>
        座位：<span class="highlight">2 號車 3AB, 4AB</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:00</span> 【博多站黃金採買動線】(不繞路精華版)", unsafe_allow_html=True)
        st.write("回到博多站後先不回飯店，直接在車站內「精準打擊」把戰利品買齊：")
        st.markdown("""
        <div class="shopping-box">
        <b>1. 第一站：博多銘品藏 (博多口側)：</b> 目標是買 <b>「努努雞」</b> (冰涼酥脆的冷吃炸雞，九州必吃名物)。<br>
        <b>2. 第二站：AMANBERRY (AMU PLAZA 1F)：</b> 博多口旁邊的百貨 1F。目標：超人氣的<b>草莓夾心餅乾</b>。<br>
        <b>3. 第三站：LOPIA 超市 (筑紫口 Yodobashi 4F)：</b> 穿過大廳到後站筑紫口，進 Yodobashi 上 4F。直接買好今晚的熟食、披薩、生魚片、草莓、飲料回飯店開派對！
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=ロピア+博多ヨドバシ店")
        
        st.markdown("##### <span class='time-badge'>18:45</span> 【晚餐備案】博多めん街道 (清爽系拉麵候選)", unsafe_allow_html=True)
        st.write("如果大家想吃碗熱呼呼的拉麵再回飯店，請直攻博多車站 DEITOS 2 樓的「博多めん街道」。為照顧長輩胃口，特別精選 3 間最不油膩的清爽系名單：")
        st.markdown("""
        * 🍜 **博多醤油ラーメン 月や：** 罕見的「非豚骨」！透明清湯，激推「德島酸橘拉麵」，酸甜柑橘解膩程度 100 分。
        * 🍜 **博多らーめん Shin-Shin：** 怕油膩也能大口喝湯的「純情豚骨」，完全無豬骨臭味，排隊人潮滿滿女性與長輩。
        * 🍜 **博多川端どさんこ：** 主打味噌/鹽味拉麵，上面鋪滿炒過的蔬菜，多了一份清甜，他們家的「炒飯」更是神級必點！
        """)

        st.markdown("##### <span class='time-badge'>19:30</span> 【返回飯店】計程車直達", unsafe_allow_html=True)
        st.write("**動作：** 買完大包小包，直接在筑紫口的計程車排班處上車，跟司機說回 Cross Life 博多柳橋。")
        st.write("**宵夜：** 在飯店房間內輕鬆享用 LOPIA 超市大餐與努努雞！")

    # --- Day 5 ---
    elif "Day 5" in day:
        st.header("Day 5: 熊本一日遊 & 頂級鰻魚")
        st.caption("今日核心目標：輕裝上陣、搭新幹線吃便當、看熊本熊、回博多吃百年鰻魚！")
        if os.path.exists("出國前最終確認：Day 5 (週四) .jpg"):
            st.image("出國前最終確認：Day 5 (週四) .jpg", use_column_width=True)
            
        st.info("""
        💡 **領隊晨間廣播 (出發前必確認)：**
        1. **行李放飯店：** 今天晚上還會回同一間飯店，大件行李留在飯店房間，大家只要背輕便小包包出門！
        2. **車票確認：** 確認 4 個人的新幹線來回車票都在身上。
        3. **交通卡備妥：** 在熊本市區搭乘「路面電車」，上下車直接刷交通卡最方便 (後門上車嗶，前門下車再嗶一次)，不用買一日券。
        """)
        
        st.markdown("##### <span class='time-badge'>08:00</span> 【飯店出發】前往博多車站 (筑紫口)", unsafe_allow_html=True)
        st.write("**交通：** 直接請飯店叫計程車，跟司機說到 **「博多駅 筑紫口 (Chikushi-guchi)」**。因為新幹線的搭車點和便當店都在這側。")
        
        st.markdown("##### <span class='time-badge'>08:10</span> 【早餐任務】駅弁当 (Ekiben Station) 買鐵路便當", unsafe_allow_html=True)
        st.markdown("""
        <div class="bento-box">
        <b>地點：</b> 博多站 1F 筑紫口側，就在新幹線改札口附近。<br>
        <b>動作：</b> 帶長輩來這裡挑選自己喜歡的鐵路便當 (明太子便當、佐賀牛便當等)。結帳後，準備進新幹線閘門。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：駅弁当 筑紫口店", "https://www.google.com/maps/search/?api=1&query=駅弁当+博多駅")
        
        st.markdown("##### <span class='time-badge'>08:30</span> 【去程】JR 九州新幹線 Mizuho 601 (博多 ➡ 熊本)", unsafe_allow_html=True)
        st.write("**搭乘路線：** 九州新幹線 (Kyushu Shinkansen)。")
        st.write("**進站入口：** 請注意！搭乘新幹線必須從筑紫口側的 **「新幹線改札口 (Shinkansen Gate)」** 放入實體車票進站，不要走到一般 JR 線的閘門。")
        st.write("**找月台：** 進站後，尋找往「熊本、鹿兒島中央」方向的月台（通常在 11 到 16 號月台區間，請對照電子看板確認）。")
        st.link_button("🗺️ 路線：博多車站 ➡ 熊本車站", "https://maps.app.goo.gl/bXPduPfdVgihUVFh8")
        st.markdown("""
        <div class="ticket-box">
        <b>博多 08:30 → 熊本 09:02</b><br>
        座位：<span class="highlight">5 號車 5AB, 6AB</span><br>
        備註：乘車體驗！上車就可以打開便當一邊看風景一邊吃。瑞穗號速度極快，<b>只要 32 分鐘</b>就會抵達熊本！
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🎥 熊本市區行程交通 VLOG 參考 (點擊展開)"):
            st.markdown("* [熊本市區一日遊｜福岡機場到博多、熊本交通方式](https://www.youtube.com/watch?v=IucP8Lrs43E&t=273s)")
        
        st.markdown("##### <span class='time-badge'>09:15</span> 【市區移動】搭乘熊本市電", unsafe_allow_html=True)
        st.write("**動線：** 出熊本車站後，走到站前的「市電乘車處」。")
        st.write("**搭車：** 搭乘 **A 系統（紅線，往健軍町方向）**。在 **【熊本城・市役所前】** 站下車。")
        st.link_button("🗺️ 路線：市電 A 系統 ➡ 通町筋(熊本城)", "https://maps.app.goo.gl/WhczLrp8QfC5yJLk7")
        with st.expander("🚃 熊本市電交通攻略與知識庫 (點擊展開)"):
            st.markdown("""
            * 🎥 **市電搭乘教學影片：** [最新！熊本市區千萬要知道的所有交通細節](https://www.youtube.com/watch?v=Lkgorc2QWOs)
            * 📝 **備用知識庫：** [熊本市電一日券與24小時券介紹](https://nicklee.tw/3297/kumamoto-tram-1day/)
            """)
        
        st.markdown("##### <span class='time-badge'>09:40</span> 【上午景點】櫻之馬場 城彩苑 & 熊本城", unsafe_allow_html=True)
        st.write("**第一站 (城彩苑)：** 步行 3 分鐘先到仿江戶時代的城下町「城彩苑」，有很多好拍的街景和特色小吃 (海膽可樂餅、芥末蓮藕)。")
        st.write("💡 **護膝神仙路線 (前往天守閣)：** **絕對不要帶長輩爬好漢坡！** 請在城彩苑尋找 **「免費接駁巴士」**，它會直接把您們載到熊本城上方的廣場，走平緩的空中步道進天守閣，對長輩膝蓋最友善！")
        st.link_button("📍 導航：櫻之馬場 城彩苑", "https://www.google.com/maps/search/?api=1&query=桜の馬場+城彩苑")
        st.link_button("📍 導航：熊本城", "https://www.google.com/maps/search/?api=1&query=熊本城")
        
        st.markdown("##### <span class='time-badge'>11:30</span> 【午餐】勝烈亭豬排 (新市街本店)", unsafe_allow_html=True)
        st.write("**移動：** 從熊本城搭市電，搭到 **【辛島町站】** 下車，走 2 分鐘。")
        st.write("**策略：** 11:30 抵達可以完美避開中午 12:00 的上班族排隊人潮。")
        st.write("**必點：** 「六白黑豚」炸豬排定食。肉質軟嫩多汁，長輩絕對咬得動！")
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=勝烈亭+新市街本店")
        
        st.markdown("##### <span class='time-badge'>13:30</span> 【午後散策】下通商店街 & 尋找熊本熊", unsafe_allow_html=True)
        st.write("**動線：** 餐廳外面就是熱鬧的 **「下通商店街」**，有拱廊不怕風吹日曬。一路往北走約 15 分鐘會連通到「鶴屋百貨」。")
        st.write("🌟 **熊本熊部長辦公室 (Kumamon Square)：** 熊本熊大本營！若想看本尊的下午 15:00 見面會表演，記得 **14:30** 就要去卡位，人會非常多！")
        st.link_button("📍 導航：熊本熊部長辦公室", "https://www.google.com/maps/search/?api=1&query=Kumamon+Square")
        
        with st.expander("🛍️ 熊本市區購物攻略參考 (點擊展開)"):
            st.markdown("* [2026熊本購物必逛攻略｜上通、下通商店街+車站周邊必買](https://www.bring-you.info/zh-tw/kumamoto-shopping-guide)")
        
        st.markdown("##### <span class='time-badge'>17:00</span> 【熊本車站採買】肥後よかモン市場", unsafe_allow_html=True)
        st.link_button("🗺️ 路線：通町筋 ➡ 熊本車站", "https://maps.app.goo.gl/mFG4fTckyxgFPxXH9")
        st.write("**搭車：** 從水道町或通町筋搭市電 A 系統回到熊本車站。")
        st.write("**目標：** 新幹線改札口正對面的市場。必買 **「熊本熊圓形便當」** (可重複微波使用的便當盒當紀念)，或買個阿蘇赤牛便當當宵夜。")
        st.link_button("📍 導航：肥後よかモン市場", "https://www.google.com/maps/search/?api=1&query=肥後よかモン市場")
        
        with st.expander("🎥 熊本車站周邊攻略影片 (點擊展開)"):
            st.markdown("* [最完整熊本車站周邊全攻略｜美食購物住宿](https://www.youtube.com/watch?v=4IxvIkJMn9Q)")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 【回程】JR 九州新幹線 Tsubame 328 (燕子號)", unsafe_allow_html=True)
        st.write("**進站入口：** 在市場採買完畢後，直接走到旁邊的 **「新幹線改札口」** 放入實體車票進站。")
        st.write("**找月台：** 尋找往「博多、新大阪」方向的新幹線月台（通常在 11 或 12 號月台）。")
        st.link_button("🗺️ 路線：熊本車站 ➡ 博多車站", "https://maps.app.goo.gl/3H5Nmctx35eenUu5A")
        st.markdown("""
        <div class="ticket-box">
        <b>熊本 17:20 → 博多 18:09</b><br>
        座位：<span class="highlight">5 號車 6AB, 7AB</span><br>
        備註：燕子號的木質內裝非常有設計感，剛好讓長輩在車上休息補眠。提早回博多，從容吃晚餐！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:50</span> 【百年美味】吉塚鰻魚屋 (本店)", unsafe_allow_html=True)
        st.write("**交通：** 抵達博多站後，往 **「博多口」** 方向出站，直接搭計程車 (車程 10 分鐘內)。")
        st.write("**點餐建議：** 被譽為福岡第一的百年鰻魚飯老店。推薦點 **「鰻重 (Unaju)」** (飯與鰻魚分開裝)，表皮烤得極度酥脆，肉質軟嫩，絕對是整趟旅程的美食最高潮！吃飽後若天氣好可沿那珂川散步回飯店，或直接攔車。")
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=吉塚うなぎ屋")

    # --- Day 6 ---
    elif "Day 6" in day:
        st.header("Day 6: 甜點衝刺 & 滿載而歸")
        st.caption("今日核心目標：絕對不扛大行李轉車，新台幣/日幣戰術順利去機場！")
        if os.path.exists("出國前最終確認：Day 6 (週五) .jpg"):
            st.image("出國前最終確認：Day 6 (週五) .jpg", use_column_width=True)
            
        st.warning("⚠️ **行李整理大魔王提醒：** 昨晚買的草莓請當早餐吃完，不能帶回台灣！「明太子（軟管或盒裝）」和「布丁/果凍」在飛安規定上屬於**液體/膏狀物**，請務必塞進「托運行李」中，絕對不能放在隨身手提包包，否則安檢會被丟掉！")
        
        st.markdown("##### <span class='time-badge'>07:30</span> 【早鳥專屬】柳橋連合市場 (最後巡禮)", unsafe_allow_html=True)
        st.write("從飯店走出去 1 分鐘就到。長輩如果起得早，可以去市場買個現炸的手工魚板（甜不辣）當早餐，或是感受一下在地傳統市場的早晨活力。")
        
        st.markdown("##### <span class='time-badge'>08:50</span> 【辦理退房】行李寄放櫃台", unsafe_allow_html=True)
        st.write("**動作：** 將所有大件行李整理好，到一樓櫃台辦理 Check-out。")
        st.write("**寄放：** 把大行李寄放在櫃台（跟櫃台說 \"Luggage keep, please\"），全家人只要帶著隨身小包包出門做最後衝刺！")
        
        st.markdown("##### <span class='time-badge'>09:10</span> 【甜點任務】I'm donut ? (天神店)", unsafe_allow_html=True)
        st.write("**移動：** 從飯店慢慢散步前往天神南區域（約 10 分鐘）。")
        st.write("**戰術分工：** 福岡目前最紅的生甜甜圈名店，排隊人潮非常可怕。年輕人負責排隊，**請長輩到對面的「大丸百貨」外面的椅子坐著休息，千萬別讓長輩跟著罰站！**")
        st.link_button("📍 導航：I'm donut ? 天神店", "https://www.google.com/maps/search/?api=1&query=I'm+donut+天神店")
        
        st.markdown("##### <span class='time-badge'>10:00</span> 【備用行程】大丸百貨 (福岡天神店)", unsafe_allow_html=True)
        st.write("**動作：** 10:00 百貨公司準時開門，長輩可以進去上個乾淨的廁所。")
        st.write("**備案買法：** 如果甜甜圈排太長決定放棄，直接帶長輩殺進大丸百貨地下街 (B2)，挑選幾家精緻的和菓子或洋菓子，完美取代甜甜圈。")
        st.link_button("📍 導航：大丸福岡天神店", "https://www.google.com/maps/search/?api=1&query=大丸福岡天神店")
        
        st.markdown("##### <span class='time-badge'>10:20</span> 【返回飯店】領行李與叫車", unsafe_allow_html=True)
        st.error("🛑 **關鍵交通：絕對不要去搭地鐵轉接駁巴士！** (對長輩提大行李非常折磨)")
        st.write("**動作：** 回飯店拿大行李，直接請飯店櫃檯幫忙叫計程車，或是走到大馬路上攔車。")
        st.write("**跟司機說：** **「Fukuoka Kūkō, Kokusai-sen (福岡空港 國際線)」**。走高速公路直達約 15-20 分鐘，這是全趟旅程 CP 值最高的一趟計程車。")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 【抵達機場】福岡機場國際線 3F 出境大廳", unsafe_allow_html=True)
        st.write("**流程：** 找到**長榮航空 (EVA Air)**報到櫃台 ➡ 托運行李 (再次確認明太子已托運) ➡ 領取登機證 ➡ 過安檢 ➡ 過海關。")
        
        st.markdown("##### <span class='time-badge'>11:15</span> 【最後衝刺】機場免稅店大採購", unsafe_allow_html=True)
        st.write("**免稅必買：**")
        st.write("1. **福砂屋 長崎蛋糕 (Castella)：** 底下有雙目糖顆粒的極品，買回家配茶最棒。")
        st.write("2. **明太子系列：** 如果市區沒買夠，這裡有保冷袋包裝的明太子可以安心帶上飛機。")
        st.write("*溫馨提醒：結帳排隊人潮可能很多，請留一位家人注意登機時間。*")
        
        st.markdown("##### <span class='time-badge'>12:15</span> 【起飛】長榮航空 BR105", unsafe_allow_html=True)
        st.write("帶著滿滿的戰利品與美好回憶，在飛機上吃頓飛機餐睡個午覺。**13:50 平安降落台灣桃園國際機場 (T2)**。慢慢拿行李出關，搭機捷至高鐵桃園站 (車程約 16 分鐘)。")
        
        st.markdown("##### <span class='time-badge'>16:34</span> 【平安返家】高鐵 841 車次", unsafe_allow_html=True)
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
        st.checkbox("明太子 (注意液體托運規定)")
        st.checkbox("熊本熊便當 (空盒)")

# === Tab 3: 車票與預約 ===
with tab3:
    st.header("🎫 票券管理中心 (已全數確認)")

    st.markdown("### ✅ 台灣高鐵來回車票 (已購買)")
    st.success("台中 ↔ 桃園")
    st.markdown("""
    <div class="ticket-box">
    <b>去程 (Day 1 - 630車次):</b> 12:00 台中 → 12:36 桃園<br>
    備註：抵達後搭機捷前往桃園機場 T2。<br>
    <hr style="margin:5px 0; border-top: 1px dashed #1ABC9C;">
    <b>回程 (Day 6 - 841車次):</b> 16:34 桃園 → 17:15 台中<br>
    備註：從桃園機場 T2 搭機捷前往高鐵站。
    </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("### 💳 IC 卡 (Suica/ICOCA) 儲值建議")
    st.info("""
    💡 **最保險但不浪費的儲值策略：每張卡儲值 ¥4,000**
    
    (預估總花費約 ¥3,550，保留 ¥450 緩衝，萬一臨時多搭一段也夠用，且不會剩太多錢退卡麻煩。)
    """)
    
    st.markdown("""
    <div class="route-box">
    <b>🧾 各日 IC 卡預估車資清單：</b><br>
    <ul>
        <li><b>Day 1 (福岡市地下鐵):</b> 約 ¥470 (機場→博多→渡邊通)</li>
        <li><b>Day 2 (西鐵電車):</b> 約 ¥840 (天神 ↔ 太宰府來回)</li>
        <li><b>Day 3 (JR):</b> 約 ¥960 (博多 ↔ 海之中道來回)</li>
        <li><b>Day 4 (JR 普通車):</b> 約 ¥560 (小倉 ↔ 門司港來回)</li>
        <li><b>Day 5 (熊本市電):</b> 約 ¥720 (保守估計搭乘 4 段，單趟 ¥180)</li>
    </ul>
    <b>📊 全部加總：約 ¥3,550</b>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### 🍽️ 餐廳預約")
    st.success("藥院燒肉 肉一：3/2 19:00 (4人)")
    st.caption("預約大名：鄭又豪 先生")

# === Tab 4: 旅費與記帳 ===
with tab4:
    st.header("💰 旅費與結算系統 (Google Sheets 雲端連動版)")
    
    # --- 上半部：固定開銷 ---
    st.subheader("🏦 行前總預算與固定開銷 (已確定金額)")
    
    fixed_total_twd = 107234
    fixed_per_person = fixed_total_twd / 4
    
    st.markdown(f"""
    <div class="account-box">
    <b>🧾 固定花費明細 (單位：台幣)：</b><br>
    <ul>
        <li>台灣高鐵來回：3,780 元</li>
        <li>長榮來回機票 (4人)：65,828 元</li>
        <li>Cross Life 飯店 (5晚)：27,080 元</li>
        <li>海洋世界門票：2,060 元</li>
        <li>音速號車票：4,298 元</li>
        <li>新幹線車票：9,188 元</li>
    </ul>
    <b>💰 行前總花費：{fixed_total_twd:,} 元</b><br>
    <span style="color:#C0392B;"><b>👨‍👩‍👧‍👦 平均每人已分擔：{fixed_per_person:,.0f} 元</b></span>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # --- 下半部：當地記帳本 ---
    st.subheader("💴 旅途當地記帳本")
    rate = st.number_input("🔄 今日日幣換台幣匯率 (可隨時調整)", value=0.215, format="%.4f")
    
    # Google Sheets 雙刀流連線機制
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        try:
            # 模式 A：嘗試讀取 Streamlit Secrets 保險箱 (雲端上線時會走到這裡)
            creds_dict = dict(st.secrets["gcp_service_account"])
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        except Exception:
            # 模式 B：讀取本地檔案 (在您自己電腦測試時會走到這裡)
            creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
        
        client = gspread.authorize(creds)
        sheet = client.open('2026北九州行_旅費記帳').sheet1
        
        # 讀取現有的記帳資料
        records = sheet.get_all_records()
        df = pd.DataFrame(records)
        
        with st.form("expense_form"):
            col_day, col_payer = st.columns(2)
            exp_day = col_day.selectbox("🗓️ 日期", ["行前開銷", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"])
            exp_payer = col_payer.selectbox("👤 誰的開銷 / 歸屬", ["All (全家平分)", "爸爸", "媽媽", "姊姊", "弟弟"])
            
            exp_name = st.text_input("📝 項目名稱 (例如：便利商店買水、松本清藥妝)")
            exp_amount = st.number_input("💴 金額 (日圓 ¥ / 台幣請先將匯率改1)", min_value=0, step=100)
            
            submitted = st.form_submit_button("新增這筆花費 ➕")
            if submitted and exp_name and exp_amount > 0:
                ntd_amount = int(exp_amount * rate)
                # 直接寫入 Google Sheets
                sheet.append_row([exp_day, exp_payer, exp_name, exp_amount, ntd_amount])
                st.success(f"✅ 已成功記錄並同步至雲端：{exp_name} (¥{exp_amount} / NT${ntd_amount})")
                st.rerun()

        # --- 顯示記帳明細與結算 ---
        if not df.empty:
            st.markdown("### 📜 旅途花費明細表 (同步自 Google Sheets)")
            st.dataframe(df, use_container_width=True)
            
            # 結算邏輯
            st.markdown("### 📊 最終個人結算報表 (台幣)")
            
            # 確保台幣欄位格式正確
            if '歸屬' in df.columns and '台幣 (NT$)' in df.columns:
                df['台幣 (NT$)'] = pd.to_numeric(df['台幣 (NT$)'], errors='coerce').fillna(0)
                
                # 1. 算出當地「All」的總公費，並除以 4
                shared_twd = df[df['歸屬'] == 'All (全家平分)']['台幣 (NT$)'].sum()
                shared_per_person = shared_twd / 4
                
                # 2. 分別計算 4 個人的最終總額
                persons = ["爸爸", "媽媽", "姊姊", "弟弟"]
                settlement_data = []
                
                for p in persons:
                    personal_twd = df[df['歸屬'] == p]['台幣 (NT$)'].sum()
                    total_for_p = fixed_per_person + shared_per_person + personal_twd
                    settlement_data.append({
                        "家人": p,
                        "行前公費底銷": f"{fixed_per_person:,.0f}",
                        "當地平分公費": f"{shared_per_person:,.0f}",
                        "個人專屬花費": f"{personal_twd:,.0f}",
                        "🔥 應付總額": f"{total_for_p:,.0f}"
                    })
                    
                df_settlement = pd.DataFrame(settlement_data)
                st.table(df_settlement)

    except Exception as e:
        st.error("⚠️ 無法連線至 Google Sheets。請確認金鑰設定是否正確，或是試算表是否已開啟共用。")
        st.caption("開發人員錯誤訊息檢視：")
        st.code(str(e))

