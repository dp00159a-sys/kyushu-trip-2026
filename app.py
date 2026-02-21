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
            
        st.info("💡 **出發前溫馨提醒 (領隊廣播)：** 請務必提醒家人要帶上「日本的交通卡」(Suica、ICOCA 等)。雖然現場買實體票也可以，但帶著長輩拉行李，能直接「嗶」卡進出站，絕對會讓旅程一開始就順暢無比！")
        
        st.markdown("##### <span class='time-badge'>12:00</span> 台灣出發", unsafe_allow_html=True)
        st.write("**動作：** 從高鐵台中站出發。搭乘 **630 車次 (12:00 發車)** 前往高鐵桃園站，轉乘機捷抵達航廈。")
        st.write("**航班：** 長榮航空 BR102 (桃園機場 T2 / 16:25 準時起飛)。")
        
        st.markdown("##### <span class='time-badge'>19:55</span> 抵達日本 (福岡機場出關)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>🚌 機場移動動線 (重要更新)：</b><br>
        1. 拿好行李出關後，請尋找並從 <b>「A3 出口」</b> 離開航廈。<br>
        2. 出 A3 出口後 <b>「往右邊走」</b>，就會看到前往國內線航廈的「免費接駁巴士」站牌。<br>
        3. <b>搭乘接駁巴士 (車程約 10 分鐘)</b>，巴士會直接載您抵達國內線航廈的「福岡機場地鐵站」入口。
        </div>
        """, unsafe_allow_html=True)
        
        st.caption("🎥 實景走法請參考以下影片（從下飛機到搭巴士）：")
        st.video("https://www.youtube.com/watch?v=pRwDSFJskzQ")
        
        st.markdown("##### <span class='time-badge'>21:20</span> 市區移動 (地鐵轉乘)", unsafe_allow_html=True)
        st.write("**進站：** 拿出準備好的交通卡感應進站。")
        st.markdown("""
        <div class="route-box">
        <b>第一段 (空港線)：</b> 從【福岡機場站】搭乘地下鐵空港線，搭 2 站在 <b>【博多站】</b> 下車。<br>
        <b>🚶 站內轉乘動線：</b> 下車後跟著綠色指標「七隈線」走。這段連通道設有<b>「電動步道」</b>，慢慢走約 6 分鐘。<br>
        <b>第二段 (七隈線)：</b> 搭乘往「橋本」方向的列車，<b>僅搭 1 站</b>，在 <b>【渡邊通站】</b> 下車。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>22:00</span> 飯店入住", unsafe_allow_html=True)
        st.write("**出口指引：** 在【渡邊通站】下車後，**請務必尋找「2號出口」(有手扶梯)**，絕對不要讓家人第一天就扛行李爬樓梯。")
        st.write("**步行至飯店：** 從 2 號出口一到地面直接左轉，過一座小橋後，飯店即在右手邊。辦理 Check-in。")
        st.link_button("📍 導航：Cross Life 博多柳橋", "https://www.google.com/maps/search/?api=1&query=Cross+Life+博多柳橋")
        
        st.markdown("##### <span class='time-badge'>22:30</span> 夜間補給", unsafe_allow_html=True)
        st.write("**地點：** 飯店附近的 Sunny 超市 (24小時營業)。")
        st.write("**採買任務：** 大瓶裝礦泉水 (2L)、博多甘王草莓 (九州必吃宵夜)、優格/牛奶，以及若隔日不想排隊名店可先買好的早餐備品。")
        st.link_button("📍 導航：Sunny 超市 渡邊通店", "https://www.google.com/maps/search/?api=1&query=Sunny+渡邊通店")

    # --- Day 2 ---
    elif "Day 2" in day:
        st.header("Day 2: 太宰府賞梅 & 天神購物")
        st.caption("今日核心目標： 早上看限定版神殿與梅花，下午逛街，晚上吃和牛燒肉！")
        if os.path.exists("出國前最終確認：Day 2 (週一).jpg"):
            st.image("出國前最終確認：Day 2 (週一).jpg", use_column_width=True)
            
        st.markdown("##### <span class='time-badge'>08:00</span> 晨間散步：柳橋連合市場", unsafe_allow_html=True)
        st.write("**出發：** 從飯店走出來約 2 分鐘即達「博多的廚房」。")
        st.write("**看點：** 早上市場最有活力，可以看在地海鮮、買個現做的魚漿天婦羅（甜不辣）或玉子燒當早點。")
        st.info("💡 **備註：** 如果長輩想睡晚一點，這個點可以隨時取消，或是移到 Day 6 早上。")
        st.link_button("📍 導航：柳橋連合市場", "https://www.google.com/maps/search/?api=1&query=柳橋連合市場")
            
        st.markdown("##### <span class='time-badge'>08:30</span> 早餐：挑戰名店或輕鬆吃", unsafe_allow_html=True)
        st.markdown("""
        * **選項 A (網美挑戰)：** DACOMECCA 麵包店 (博多站旁，需搭地鐵過去排隊)。
        * **選項 B (輕鬆路線)：** 直接在飯店附近吃麥當勞、超商，或市場買的小吃墊胃。
        """)
        st.link_button("📍 導航：飯店周邊超市備案", "https://maps.app.goo.gl/DuySWvfGregfzPVN9")
            
        st.markdown("##### <span class='time-badge'>09:30</span> 市區移動：前往西鐵天神站", unsafe_allow_html=True)
        st.write("**動線：** 從【渡邊通站】搭地下鐵七隈線 ➡ 【天神南站】下車。")
        st.write("**轉乘：** 沿著地下街的指標，往上走到 2F/3F 的 【西鐵福岡(天神)站】。")
            
        st.markdown("##### <span class='time-badge'>10:00</span> 前往太宰府 (西鐵電車)", unsafe_allow_html=True)
        st.write("**交通方式：** 直接刷實體交通卡進站 (Suica/ICOCA)。不用買套票！")
        st.markdown("""
        <div class="route-box">
        <b>✨ 列車選擇攻略：</b><br>
        1. <b>直達車 (首選)：</b> 平日早上 (約 09:46 左右，依現場班表為準) 會有一班直達太宰府的<b>「旅人號 (Tabito)」或直達急行</b>，如果遇到，請直接跳上去，不用換車！<br>
        2. <b>一般急行 (備案)：</b> 如果沒遇到直達車，就搭往「大牟田」方向的特急或急行，在 <b>【西鐵二日市站】</b> 下車，同月台或換月台轉搭「太宰府線」。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:45</span> 太宰府散策：賞梅與吃餅", unsafe_allow_html=True)
        st.markdown("""
        * **必看亮點 1：** 期間限定「臨時本殿」 (漂浮森林屋頂，非常特別！)。
        * **必看亮點 2：** 3 月初正值太宰府的梅花季，整個天滿宮會有粉白相間的梅花，非常適合幫長輩拍照。
        * **吃喝採買：** 參道上的「梅枝餅」(現烤的最好吃) 以及隈研吾設計的「星巴克」。
        """)
        st.info("💡 **備用景點 (強烈建議 PASS)：** 九州國立博物館或光明禪寺/竈門神社距離較遠需爬坡。為了下午逛街保留體力，建議不要去！")
        st.link_button("📍 導航：太宰府天滿宮", "https://www.google.com/maps/search/?api=1&query=太宰府天滿宮")

        st.markdown("##### <span class='time-badge'>13:00</span> 午餐：彈性安排", unsafe_allow_html=True)
        st.write("可以在太宰府參道吃一蘭拉麵（合格五角形碗）、暖暮拉麵或定食。如果太擠，就搭車回天神再吃。")
        
        st.markdown("##### <span class='time-badge'>14:30</span> 下午逛街：天神地下街 ➡ Mina 天神", unsafe_allow_html=True)
        st.write("**動線 (不曬太陽/不淋雨)：** 搭西鐵回天神後，直接鑽進【天神地下街】(有椅子可休息，還能買 BAKE 起司塔、RINGO)。一路往北走到底，直接連通【Mina 天神】。")
        st.write("**主力戰場 (Mina 天神)：** UNIQLO (九州最大旗艦店)、GU、LOFT、Seria (百元店)。長輩可以坐在服飾店的沙發區等您結帳。")
        st.link_button("📍 導航：Mina 天神", "https://www.google.com/maps/search/?api=1&query=Mina+天神")
        
        st.markdown("##### <span class='time-badge'>18:20</span> 前往晚餐：兩種移動方案", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>方案 A (搭西鐵)：</b> 沿著地下街慢慢走回【西鐵天神站】，搭一站到【西鐵藥院站】，再走 3-5 分鐘到餐廳。(缺點：對走了一下午的長輩來說有點折磨)。<br>
        <b>方案 B (🚕 強烈建議 - 搭計程車)：</b> 逛完 Mina 天神，直接請百貨櫃檯幫忙叫車，或是走到大馬路上攔車。4 個人平分車資約 ¥1,000 日圓出頭，直達燒肉店門口，長輩會覺得您是世界上最棒的導遊。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>19:00</span> 重頭戲晚餐：藥院燒肉 肉一", unsafe_allow_html=True)
        st.success("✅ 確認事項：已預約 19:00 / 4 位 / 鄭又豪先生。")
        st.write("**必點：** 豪華黑毛和牛拼盤、盛岡冷麵 (解膩神物)。這家肉質很軟嫩，長輩牙口不好絕對沒問題。")
        st.link_button("📍 導航：藥院燒肉 肉一", "https://www.google.com/maps/search/?api=1&query=薬院焼肉+肉一")

        st.markdown("##### <span class='time-badge'>21:00</span> 返回飯店", unsafe_allow_html=True)
        st.write("**交通：** 餐廳門口直接搭計程車回 Cross Life 博多柳橋（超近，起步價左右就到了），結束完美的一天。")

    # --- Day 3 ---
    elif "Day 3" in day:
        st.header("Day 3: 海豚相伴 & 天神北美食")
        st.caption("今日核心目標：09:30 準時入園、看海豚秀、順利買到明太子法棍、提早排隊吃天麩羅！")
        if os.path.exists("出國前最終確認：Day 3 (週二) .jpg"):
            st.image("出國前最終確認：Day 3 (週二) .jpg", use_column_width=True)
        
        st.markdown("##### <span class='time-badge'>08:00</span> 飯店出發 (交通升級)", unsafe_allow_html=True)
        st.write("**早餐建議：** 前一晚在超商買好早餐，房間吃完再下樓。")
        st.warning("🚕 **首選交通 (計程車)：** 絕對不要走路 20 分鐘去博多站！請直接在飯店叫車直達博多站博多口 (約 ¥1000)。<br>🚌 **備案交通 (西鐵巴士)：** 走到飯店外大馬路的「柳橋」站牌搭乘往博多站的巴士。")
        
        st.markdown("##### <span class='time-badge'>08:25</span> 前往海之中道 (JR轉乘)", unsafe_allow_html=True)
        st.write("**進站找月台：** 博多口進站，尋找往「小倉、門司港」方向的鹿兒島本線 (約 1、2 號月台)。")
        st.markdown("""
        <div class="route-box">
        <b>Step 1:</b> 08:30 左右搭車 (快速/普通) → <b>【香椎站】</b> (車程10-15分)。<br>
        <b>Step 2 (⚠️ 關鍵轉乘):</b> 香椎站下車，<b>必須走樓梯/電梯上天橋</b>，換到 <b>4 號或 5 號月台 (香椎線)</b>。<br>
        <b>Step 3:</b> 搭乘 08:50~09:00 左右往「西戶崎」的列車 → <b>【海之中道站】</b> (車程約20分)。
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>09:30</span> 福岡海洋世界 Marine World", unsafe_allow_html=True)
        st.success("🎫 門票預約：09:30 (4 位成人)。準備手機憑證掃碼入場。")
        st.markdown("""
        * **黃金動線：** 趁人少先去「全景大水槽」看沙丁魚風暴與海豹/企鵝。
        * **海豚表演：** 10:45 提早前往劇場找陰涼座位。**11:00 準時觀賞精彩海豚海獅秀**。
        * **午餐安排：** 表演結束後，可直接在館內的「Reilly 餐廳」用餐，在水下玻璃旁看海豚游泳吃飯，長輩最愛！
        """)
        st.link_button("📍 導航：Marine World", "https://www.google.com/maps/search/?api=1&query=マリンワールド海の中道")
        
        st.markdown("##### <span class='time-badge'>13:30</span> 提早離開 & 返回市區", unsafe_allow_html=True)
        st.info("💡 **彈性評估：** 旁邊的海濱公園佔地極大，若長輩需要休息，強烈建議果斷放棄公園，原路搭 JR 返回市區 (可在【千早站】下車轉搭西鐵回天神)。")
        
        st.markdown("##### <span class='time-badge'>15:30</span> 下午逛街：天神北商圈", unsafe_allow_html=True)
        st.markdown("""
        * **1. Full Full 天神店：** 必買九州最有名的「明太子法國麵包」，買回飯店當宵夜/早餐超讚。
        * **2. AEON Shoppers 福岡店：** B1 超市非常好買，採購零食、茶包等輕量伴手禮。
        """)
        st.link_button("📍 導航：Full Full 天神", "https://www.google.com/maps/search/?api=1&query=フルフル天神パン工房")
        st.link_button("📍 導航：AEON Shoppers", "https://www.google.com/maps/search/?api=1&query=イオンショッパーズ福岡店")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 重頭戲晚餐：天麩羅處 Hirao", unsafe_allow_html=True)
        st.write("**策略：** 這家當地靈魂美食**不能訂位！** 提早去大名店排隊大幅縮短時間。買食券入座，師傅現炸。桌上免費的**「柚子花枝醃鹽辛」**超級下飯必吃！")
        st.link_button("📍 導航：天麩羅處 Hirao 大名", "https://www.google.com/maps/search/?api=1&query=天麩羅処ひらお+大名店")

        st.markdown("##### <span class='time-badge'>19:00</span> 返回飯店", unsafe_allow_html=True)
        st.write("吃飽後長輩也累了，強烈建議直接在大馬路 (國體道路) 上攔計程車回飯店。")

    # --- Day 4 ---
    elif "Day 4" in day:
        st.header("Day 4: 門司港跨海 & 博多爆買")
        st.caption("今日核心目標：小倉無痛轉乘、唐戶市場吃海鮮/歷史巡禮、博多精準採買！")
        if os.path.exists("出國前最終確認：Day 4 (週三) .jpg"):
            st.image("出國前最終確認：Day 4 (週三) .jpg", use_column_width=True)
            
        st.info("💡 **領隊廣播 (出發前必確認)：**<br>1. **實體信用卡必帶：** 早上到博多站要用機台領音速號車票。<br>2. **交通卡必帶：** 今天的無痛轉乘全靠交通卡，請確保有千元餘額。")
        
        st.markdown("##### <span class='time-badge'>09:00</span> 抵達車站：博多站領票進站", unsafe_allow_html=True)
        st.write("**動作：** 找到「綠色售票機」插入信用卡領取來回實體車票。拿「博多 ➡ 小倉」車票進閘門，尋找往小倉/大分方向特急月台。")
        
        st.markdown("##### <span class='time-badge'>09:21</span> 去程：音速號 Sonic 11", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 09:21 → 小倉 10:10</b><br>
        座位：<span class="highlight">3 號車 3AB, 4AB</span><br>
        ⚠️ <b>重要動作：</b> 找到座位後，記得踩著踏板把椅子轉向，面對面坐著聊天！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>10:10</span> 小倉站去程轉乘 (無痛轉乘神技)", unsafe_allow_html=True)
        if os.path.exists("kokura_transfer.jpg"):
            st.image("kokura_transfer.jpg", caption="下車後搭手扶梯上樓，走到出站閘門切換票券", use_column_width=True)
        st.write("**1. 出站：** 放入「音速號車票」出閘門。")
        st.write("**2. 進站：** 轉身拿出「交通卡」嗶卡重新進站！")
        st.write("**3. 換月台：** 去尋找往門司港的指標 (約 8 號月台) 搭普通車。")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 抵達門司港：大正浪漫之旅起點", unsafe_allow_html=True)
        st.write("直接嗶交通卡出站 (扣款結清)。出站就是充滿大正風華的木造車站，可拍攝月台與車站外觀。")
        
        st.markdown("##### <span class='time-badge'>11:00</span> 午餐與跨海路線選擇 (雙備案)", unsafe_allow_html=True)
        st.markdown("""
        <div class="route-box">
        <b>🌟 選項 A (推薦：跨海吃海鮮與歷史巡禮)：</b><br>
        1. <b>搭船：</b> 走到門司港棧橋，搭 11:00 聯絡船前往下關 (單程¥400，約5分)。<br>
        2. <b>唐戶市場午餐：</b> 週三無一樓市集，請帶長輩直上二樓吃海轉壽司或海鮮定食。<br>
        3. <b>歷史巡禮：</b> 散步 5-7 分鐘至「日清講和紀念館」(馬關條約現場) & 「赤間神宮」(龍宮造型紅白大門)。<br>
        4. <b>🚢 關鍵回程：最晚必須搭上 14:10 的船回門司港。</b><br>
        <hr style="margin:5px 0;">
        <b>🌟 選項 B (備案：留在門司港吃名物)：</b><br>
        風浪大不想搭船，直接留在門司港吃「燒咖哩」。車站附近的 Bear Fruits 香濃焗烤咖哩非常美味。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：唐戶市場", "https://www.google.com/maps/search/?api=1&query=唐戸市場")
        st.link_button("📍 導航：日清講和紀念館", "https://www.google.com/maps/search/?api=1&query=日清講和記念館")
        st.link_button("📍 導航：赤間神宮", "https://www.google.com/maps/search/?api=1&query=赤間神宮")
        
        st.markdown("##### <span class='time-badge'>14:20</span> 午後散策：門司港懷舊區", unsafe_allow_html=True)
        st.write("沿海港散步：拍著名的「香蕉人」雕像、去舊門司稅關沙發區休息、看「藍翼橋」開橋 (14:00 或 15:00)。")
        st.write("**下午茶：** 15:30 帶家人去「Mooon de Retro」吃水果聖代順便上廁所。")
        st.link_button("📍 導航：門司港車站", "https://www.google.com/maps/search/?api=1&query=門司港駅")
        
        st.markdown("##### <span class='time-badge'>16:30</span> 回程轉乘 (門司港 ➡ 小倉)", unsafe_allow_html=True)
        st.write("**16:30** 嗶交通卡進門司港站搭車。抵達小倉後執行相反神技：**1. 嗶交通卡出站** ➡ **2. 放入回程「音速號車票」進站**。")
        
        st.markdown("##### <span class='time-badge'>17:06</span> 回程：音速號 Sonic 42", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>小倉 17:06 → 博多 17:49</b><br>
        座位：<span class="highlight">2 號車 3AB, 4AB</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:00</span> 博多站黃金採買動線 (不繞路精華)", unsafe_allow_html=True)
        st.markdown("""
        <div class="shopping-box">
        <b>1. 博多銘品藏 (博多口)：</b> 買 <b>努努雞</b> (冰涼酥脆冷吃炸雞)。<br>
        <b>2. AMANBERRY (AMU PLAZA 1F)：</b> 博多口旁邊，買人氣草莓夾心餅乾。<br>
        <b>3. LOPIA 超市 (筑紫口 Yodobashi 4F)：</b> 穿過車站到後站上4F，買熟食、披薩、生魚片回飯店開派對！
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：LOPIA 博多", "https://www.google.com/maps/search/?api=1&query=ロピア+博多ヨドバシ店")
        
        st.markdown("##### <span class='time-badge'>19:30</span> 返回飯店", unsafe_allow_html=True)
        st.write("買完大包小包，直接在筑紫口搭計程車回飯店享用超市大餐！")

    # --- Day 5 ---
    elif "Day 5" in day:
        st.header("Day 5: 熊本一日遊 & 頂級鰻魚")
        st.caption("今日核心目標：輕裝上陣、搭新幹線吃便當、看熊本熊、回博多吃百年鰻魚！")
        if os.path.exists("出國前最終確認：Day 5 (週四) .jpg"):
            st.image("出國前最終確認：Day 5 (週四) .jpg", use_column_width=True)
            
        st.info("💡 **領隊廣播 (出發前必確認)：**<br>1. **行李放飯店：** 今晚回同一間飯店，大件行李留房間，帶輕便小包出門！<br>2. **車票與交通卡：** 帶好新幹線來回車票。市內路面電車刷交通卡即可 (後門上車嗶，前門下車嗶)。")
        
        st.markdown("##### <span class='time-badge'>08:00</span> 飯店出發 & 買鐵路便當", unsafe_allow_html=True)
        st.write("**交通：** 飯店叫計程車直達「博多站 筑紫口」。")
        st.markdown("""
        <div class="bento-box">
        <b>🍱 早餐任務：駅弁当 (Ekiben Station)</b><br>
        地點在筑紫口側新幹線改札口附近，帶長輩挑選便當，結帳後進站。
        </div>
        """, unsafe_allow_html=True)
        st.link_button("📍 導航：駅弁当 筑紫口店", "https://www.google.com/maps/search/?api=1&query=駅弁当+博多駅")
        
        st.markdown("##### <span class='time-badge'>08:30</span> 去程：新幹線 Mizuho 601", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>博多 08:30 → 熊本 09:02</b><br>
        座位：<span class="highlight">5 號車 5AB, 6AB</span><br>
        備註：車程僅 32 分鐘，上車請盡情享用便當！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>09:40</span> 上午景點：城彩苑 & 熊本城", unsafe_allow_html=True)
        st.write("**市區移動：** 出站搭市電 A 系統 (往健軍町) 至【熊本城・市役所前】。")
        st.write("**護膝神仙路線：** 先逛江戶風情的「城彩苑」，然後**絕對不要爬好漢坡**！請尋找「免費接駁巴士」直接搭到天守閣上方廣場，平緩入城最友善。")
        st.link_button("📍 導航：櫻之馬場 城彩苑", "https://www.google.com/maps/search/?api=1&query=桜の馬場+城彩苑")
        st.link_button("📍 導航：熊本城", "https://www.google.com/maps/search/?api=1&query=熊本城")
        
        st.markdown("##### <span class='time-badge'>11:30</span> 午餐：勝烈亭豬排 (新市街本店)", unsafe_allow_html=True)
        st.write("搭市電到【辛島町站】走 2 分鐘。提早抵達完美避開上班族人潮，必點「六白黑豚」定食，肉質軟嫩長輩咬得動。")
        st.link_button("📍 導航：勝烈亭 新市街", "https://www.google.com/maps/search/?api=1&query=勝烈亭+新市街本店")
        
        st.markdown("##### <span class='time-badge'>13:30</span> 午後散策：下通商店街 & 尋找熊本熊", unsafe_allow_html=True)
        st.write("吃飽沿有屋頂的下通商店街往北逛到「鶴屋百貨」。若想看熊本熊部長本尊，請提早於 **14:30** 去部長辦公室卡位。")
        st.link_button("📍 導航：熊本熊部長辦公室", "https://www.google.com/maps/search/?api=1&query=Kumamon+Square")
        
        st.markdown("##### <span class='time-badge'>17:00</span> 熊本車站採買：肥後よかモン市場", unsafe_allow_html=True)
        st.write("從水道町/通町筋搭市電回熊本站。進站前在改札口正對面的市場買 **熊本熊圓形便當 (空盒可微波，必買)** 或阿蘇赤牛便當當宵夜。")
        st.link_button("📍 導航：肥後よかモン市場", "https://www.google.com/maps/search/?api=1&query=肥後よかモン市場")
        
        st.markdown("##### <span class='time-badge'>17:20</span> 回程：新幹線 Tsubame 328 (燕子號)", unsafe_allow_html=True)
        st.markdown("""
        <div class="ticket-box">
        <b>熊本 17:20 → 博多 18:09</b><br>
        座位：<span class="highlight">5 號車 6AB, 7AB</span><br>
        備註：燕子號木質內裝極美，提早回博多，從容吃晚餐！
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### <span class='time-badge'>18:50</span> 終極晚餐：吉塚鰻魚屋", unsafe_allow_html=True)
        st.write("**交通：** 抵達博多站後出博多口搭計程車。")
        st.write("**美味推薦：** 福岡第一的百年老店。點「鰻重」(飯與鰻魚分開裝)，享受表皮極致酥脆、肉質軟嫩的最高潮晚餐！吃飽可散步回飯店。")
        st.link_button("📍 導航：吉塚鰻魚屋 本店", "https://www.google.com/maps/search/?api=1&query=吉塚うなぎ屋")

    # --- Day 6 ---
    elif "Day 6" in day:
        st.header("Day 6: 甜點衝刺 & 滿載而歸")
        st.caption("今日核心目標：絕對不扛大行李轉車，新台幣/日幣戰術順利去機場！")
        if os.path.exists("出國前最終確認：Day 6 (週五) .jpg"):
            st.image("出國前最終確認：Day 6 (週五) .jpg", use_column_width=True)
            
        st.warning("⚠️ **行李整理大魔王提醒：** 草莓當早餐吃完！明太子(軟管/盒裝)與布丁/果凍屬於**液體膏狀**，絕對不能放隨身包，必須放進托運行李！")
        
        st.markdown("##### <span class='time-badge'>07:30</span> 早鳥專屬：柳橋連合市場", unsafe_allow_html=True)
        st.write("長輩若早起，可去旁邊市場買手工甜不辣或感受在地早晨活力。")
        
        st.markdown("##### <span class='time-badge'>08:50</span> 辦理退房", unsafe_allow_html=True)
        st.write("整理好大件行李，於一樓櫃台辦理退房並寄放行李 (Luggage keep)，帶隨身小包出門衝刺。")
        
        st.markdown("##### <span class='time-badge'>09:10</span> 甜點任務：I'm donut ? (天神店)", unsafe_allow_html=True)
        st.write("**戰術分工：** 福岡最紅生甜甜圈排隊可怕。年輕人去排隊，請長輩去對面「大丸百貨」外面椅子休息。")
        st.link_button("📍 導航：I'm donut ? 天神店", "https://www.google.com/maps/search/?api=1&query=I'm+donut+天神店")
        
        st.markdown("##### <span class='time-badge'>10:00</span> 備用行程：大丸百貨地下街", unsafe_allow_html=True)
        st.write("若甜甜圈排太長，直接殺進大丸 B2 挑選高級精緻和菓子/洋菓子完美取代。")
        st.link_button("📍 導航：大丸福岡天神店", "https://www.google.com/maps/search/?api=1&query=大丸福岡天神店")
        
        st.markdown("##### <span class='time-badge'>10:20</span> 返回飯店領行李 & 叫車赴機場", unsafe_allow_html=True)
        st.error("🛑 **關鍵交通：絕對不要去搭地鐵轉接駁巴士！** 請直接請飯店叫計程車，或路邊攔車，跟司機說「福岡空港 國際線」。高速直達只需 15-20 分鐘，CP值最高！")
        
        st.markdown("##### <span class='time-badge'>10:45</span> 抵達機場 & 免稅店大採購", unsafe_allow_html=True)
        st.write("長榮航空報到與托運行李 (再次確認明太子托運)。")
        st.write("**免稅必買：** 過海關後鎖定 **「福砂屋長崎蛋糕」** (雙目糖底極品) 與保冷袋裝明太子。留一人注意登機時間。")
        
        st.markdown("##### <span class='time-badge'>12:15</span> 班機起飛 (BR105)", unsafe_allow_html=True)
        st.write("滿載而歸，機上吃午餐補眠。**13:50 降落桃園機場 T2**。悠哉過海關拿行李，推推車搭機捷往桃園高鐵站 (車程16分)。")
        
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
    
    st.divider()
    st.markdown("### 🍽️ 餐廳預約")
    st.success("藥院燒肉 肉一：3/2 19:00 (4人)")
    st.caption("預約大名：鄭又豪 先生")
