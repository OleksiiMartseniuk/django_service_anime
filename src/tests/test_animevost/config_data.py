from src.utils.animevost.schemas import (
    AnimeMin,
    AnimeComposed,
    Anime,
    Series,
    AnimeFull,
    AnimeData
)

schedule_html = """
<div class="interDubBgTwo">
    <b style="padding:11px 0px; display: block; text-align: center; color:#c97e09; font-size: 18px; border-bottom: 1px solid #fbc167;">Расписание</b>
    <p style="padding: 8px 0px; display: block; text-align: center; color:#825001; font-weight: bold; font-size: 12px;">Представлены только те аниме, которые озвучивает сайт animevost.</p>

    <a style="display: block; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisMon')">Понедельник</a>
    <div id="raspisMon" style="display: none;" class="raspis">
        <a href="/tip/tv/2696-kyoukai-senki.html">Воины Пограничья  ~ (21:30)</a>
        <a href="/tip/tv/2804-honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen-3rd-season.html">Власть книжного червя: Чтобы стать библиотекарем, все средства хороши (третий сезон)  ~ (23:00)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisTue')">Вторник</a>
    <div id="raspisTue" style="display: none;" class="raspis">
        <a href="/tip/tv/2774-yuusha-yamemasu.html">Перестану быть героем  ~ (19:30)</a>
        <a href="/tip/tv/2755-zi-chuan.html">Цзычуань  ~ (В течение дня)</a><a href="/tip/tv/2789-tomodachi-game.html">Игра друзей  ~ (22:30)</a>
        
        <a href="/tip/tv/2810-the-last-summoner.html">Последний призыватель  ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisWed')">Среда</a>
    <div id="raspisWed" style="display: none;" class="raspis"> 
    <a href="/tip/tv/2786-shijou-saikyou-no-daimaou-murabito-a-ni-tensei-suru.html">Величайший Повелитель Демонов перерождается как типичное ничтожество ~ (18:00)</a>
    <a href="/tip/tv/2788-rpg-fudousan.html">РПГ недвижимость ~ (18:30)</a>
    <a href="/tip/tv/2791-tate-no-yuusha-no-nariagari-2nd-season.html">Восхождение героя щита (второй сезон) ~ (19:00)</a>
    <a href="/tip/tv/2775-deaimon.html">Дэаймон  ~ (19:50)</a>
    <a href="/tip/tv/2776-komi-san-wa-comyushou-desu-2nd-season.html">У Коми проблемы с общением (второй сезон)  ~ (21:00)</a>
    <a href="/tip/tv/2761-tunshi-xingkong.html">Пожиратель звёзд ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisThu')">Четверг</a>
    <div id="raspisThu" style="display: none;" class="raspis">
        <a href="/tip/tv/2794-shachiku-san-wa-youjo-yuurei-ni-iyasaretai.html">Корпоративная рабыня хочет быть исцелена лоли-призраком ~ (18:30)</a>
        <a href="/tip/tv/2793-heroine-tarumono-kiraware-heroine-to-naisho-no-oshigoto.html">Стать настоящей героиней! Непопулярная героиня и секретное задание ~ (20:00)</a>
        <a href="/tip/tv/2792-gaikotsu-kishi-sama-tadaima-isekai-e-odekakechuu.html">Рыцарь-скелет вступает в параллельный мир ~ (20:00)</a>
        <a href="/tip/tv/2787-paripi-koumei.html">Тусовщик Кунмин ~ (21:30)</a>
        <a href="/tip/tv/2807-summer-time-render.html">Летнее время ~ (22:30)</a>
        <a href="/tip/tv/2777-machikado-mazoku-2-choume.html">Городская дьяволица (второй сезон) ~ (23:30)</a>
        <a href="/tip/tv/2779-mahoutsukai-reimeiki.html">Восхождение чародея ~ (23:30)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisFri')">Пятница</a>
    <div id="raspisFri" style="display: none;" class="raspis">
        <a href="/tip/tv/2800-date-a-live-iv.html">Рандеву с жизнью (четвёртый сезон) ~ (18:00)</a>
        <a href="/tip/tv/2778-koi-wa-sekai-seifuku-no-ato-de.html">Любовь после мирового господства ~ (18:30)</a>
        <a href="/tip/tv/2790-kaguya-sama-wa-kokurasetai-ultra-romantic.html">Госпожа Кагуя: в любви как на войне (третий сезон) ~ (21:00)</a>
        <a href="/tip/tv/2783-rikei-ga-koi-ni-ochita-no-de-shoumei-shitemita-heart.html">Наука влюблена, и мы докажем это (второй сезон) ~ (21:45)</a>
        <a href="/tip/tv/2781-shokei-shoujo-no-virgin-road.html">Жизнь девушки-карателя ~ (22:30)</a>
        <a href="/tip/tv/2771-aharen-san-wa-hakarenai.html">Непостижимая Ахарэн ~ (22:30)</a>
        <a href="/tip/tv/2796-dance-dance-danseur.html">Танцуй, танцуй, танцор ~ (22:30)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisSat')">Суббота</a>
    <div id="raspisSat" style="display: none;" class="raspis">
    
    <a href="/tip/tv/2772-love-all-play.html">Игра с нулевым счётом ~ (15:00)</a>
    <a href="/tip/tv/2780-ao-ashi.html">Аой Асито ~ (16:00)</a>
    <a href="/tip/tv/2782-gunjou-no-fanfare.html">Ультрамариновые фанфары ~ (20:30)</a>
    <a href="/tip/tv/2798-spy-x-family.html">Семья шпиона ~ (20:30)</a>
    <a href="/tip/tv/2802-kunoichi-tsubaki-no-mune-no-uchi.html">В сердце куноити Цубаки ~ (21:00)</a>
    <a href="/tip/tv/2801-kingdom-4.html">Царство (четвёртый сезон) ~ (22:30)</a>
    <a href="/tip/tv/2797-build-divide-code-white.html">Билд Дивайд: Белый код ~ (22:30)</a>
    <a href="/tip/tv/2808-kakkou-no-iinazuke.html">Сведённые кукушкой ~ (22:30)</a>
    <a href="/tip/tv/2799-kawaii-dake-ja-nai-shikimori-san.html">Моя девушка не только милая ~ (22:30)</a>
    <a href="/tip/tv/2539-douluo-dalu.html">Боевой континент ~ (В течение дня)</a>
    <a href="/tip/tv/2756-the-magic-chef-of-fire-and-ice.html">Демон-шеф Льда и Пламени ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisSun')">Воскресенье</a>
    <div id="raspisSun" style="display: none;" class="raspis">
   
    <a href="/tip/tv/179-one-piece.html">Ван Пис ~ (09:00)</a>
    <a href="/tip/tv/1805-boruto-naruto-next-generations111.html">Боруто: Новое поколение Наруто ~ (14:00)</a>
    <a href="/tip/tv/2803-kono-healer-mendokusai.html">Этот противный целитель! ~ (16:30)</a>
    <a href="/tip/tv/2741-baraou-no-souretsu.html">Похороны Короля Роз ~ (18:00)</a>
    <a href="/tip/tv/2785-otome-game-sekai-wa-mob-ni-kibishii-sekai-desu.html">Мир отомэ-игр - это тяжёлый мир для мобов ~ (19:00)</a>
    <a href="/tip/tv/2773-black-rock-shooter-dawn-fall.html">Стрелок с чёрной скалы: Падение ~ (20:00)</a>
        
    </div>
        <p style="padding: 6px 4px 7px 4px; display: block; text-align: center; color:red; font-weight: bold; font-size: 12px;">Указано время выхода релиза в русской озвучке. (Московское)</p>
    </div>
"""

schedule_html_not_id = """
<div class="interDubBgTwo">
    <b style="padding:11px 0px; display: block; text-align: center; color:#c97e09; font-size: 18px; border-bottom: 1px solid #fbc167;">Расписание</b>
    <p style="padding: 8px 0px; display: block; text-align: center; color:#825001; font-weight: bold; font-size: 12px;">Представлены только те аниме, которые озвучивает сайт animevost.</p>

    <a style="display: block; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisMon')">Понедельник</a>
    <div id="raspisMon" style="display: none;" class="raspis">
        <a href="/tip/tv/2696-kyoukai-senki.html">Воины Пограничья  ~ (21:30)</a>
        <a href="/tip/tv/2804-honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen-3rd-season.html">Власть книжного червя: Чтобы стать библиотекарем, все средства хороши (третий сезон)  ~ (23:00)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisTue')">Вторник</a>
    <div id="raspisTue" style="display: none;" class="raspis">
        <a href="/tip/tv/2774-yuusha-yamemasu.html">Перестану быть героем  ~ (19:30)</a>
        <a href="/tip/tv/2755-zi-chuan.html">Цзычуань  ~ (В течение дня)</a><a href="/tip/tv/2789-tomodachi-game.html">Игра друзей  ~ (22:30)</a>
        
        <a href="/tip/tv/2810-the-last-summoner.html">Последний призыватель  ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisWed')">Среда</a>
    <div id="raspisWed" style="display: none;" class="raspis"> 
    <a href="/tip/tv/2786-shijou-saikyou-no-daimaou-murabito-a-ni-tensei-suru.html">Величайший Повелитель Демонов перерождается как типичное ничтожество ~ (18:00)</a>
    <a href="/tip/tv/2788-rpg-fudousan.html">РПГ недвижимость ~ (18:30)</a>
    <a href="/tip/tv/2791-tate-no-yuusha-no-nariagari-2nd-season.html">Восхождение героя щита (второй сезон) ~ (19:00)</a>
    <a href="/tip/tv/deaimon.html">Дэаймон  ~ (19:50)</a>
    <a href="/tip/tv/2776-komi-san-wa-comyushou-desu-2nd-season.html">У Коми проблемы с общением (второй сезон)  ~ (21:00)</a>
    <a href="/tip/tv/2761-tunshi-xingkong.html">Пожиратель звёзд ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisThu')">Четверг</a>
    <div id="raspisThu" style="display: none;" class="raspis">
        <a href="/tip/tv/2794-shachiku-san-wa-youjo-yuurei-ni-iyasaretai.html">Корпоративная рабыня хочет быть исцелена лоли-призраком ~ (18:30)</a>
        <a href="/tip/tv/2793-heroine-tarumono-kiraware-heroine-to-naisho-no-oshigoto.html">Стать настоящей героиней! Непопулярная героиня и секретное задание ~ (20:00)</a>
        <a href="/tip/tv/2792-gaikotsu-kishi-sama-tadaima-isekai-e-odekakechuu.html">Рыцарь-скелет вступает в параллельный мир ~ (20:00)</a>
        <a href="/tip/tv/2787-paripi-koumei.html">Тусовщик Кунмин ~ (21:30)</a>
        <a href="/tip/tv/2807-summer-time-render.html">Летнее время ~ (22:30)</a>
        <a href="/tip/tv/2777-machikado-mazoku-2-choume.html">Городская дьяволица (второй сезон) ~ (23:30)</a>
        <a href="/tip/tv/2779-mahoutsukai-reimeiki.html">Восхождение чародея ~ (23:30)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisFri')">Пятница</a>
    <div id="raspisFri" style="display: none;" class="raspis">
        <a href="/tip/tv/2800-date-a-live-iv.html">Рандеву с жизнью (четвёртый сезон) ~ (18:00)</a>
        <a href="/tip/tv/2778-koi-wa-sekai-seifuku-no-ato-de.html">Любовь после мирового господства ~ (18:30)</a>
        <a href="/tip/tv/2790-kaguya-sama-wa-kokurasetai-ultra-romantic.html">Госпожа Кагуя: в любви как на войне (третий сезон) ~ (21:00)</a>
        <a href="/tip/tv/2783-rikei-ga-koi-ni-ochita-no-de-shoumei-shitemita-heart.html">Наука влюблена, и мы докажем это (второй сезон) ~ (21:45)</a>
        <a href="/tip/tv/2781-shokei-shoujo-no-virgin-road.html">Жизнь девушки-карателя ~ (22:30)</a>
        <a href="/tip/tv/2771-aharen-san-wa-hakarenai.html">Непостижимая Ахарэн ~ (22:30)</a>
        <a href="/tip/tv/2796-dance-dance-danseur.html">Танцуй, танцуй, танцор ~ (22:30)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisSat')">Суббота</a>
    <div id="raspisSat" style="display: none;" class="raspis">
    
    <a href="/tip/tv/2772-love-all-play.html">Игра с нулевым счётом ~ (15:00)</a>
    <a href="/tip/tv/2780-ao-ashi.html">Аой Асито ~ (16:00)</a>
    <a href="/tip/tv/2782-gunjou-no-fanfare.html">Ультрамариновые фанфары ~ (20:30)</a>
    <a href="/tip/tv/2798-spy-x-family.html">Семья шпиона ~ (20:30)</a>
    <a href="/tip/tv/2802-kunoichi-tsubaki-no-mune-no-uchi.html">В сердце куноити Цубаки ~ (21:00)</a>
    <a href="/tip/tv/2801-kingdom-4.html">Царство (четвёртый сезон) ~ (22:30)</a>
    <a href="/tip/tv/2797-build-divide-code-white.html">Билд Дивайд: Белый код ~ (22:30)</a>
    <a href="/tip/tv/2808-kakkou-no-iinazuke.html">Сведённые кукушкой ~ (22:30)</a>
    <a href="/tip/tv/2799-kawaii-dake-ja-nai-shikimori-san.html">Моя девушка не только милая ~ (22:30)</a>
    <a href="/tip/tv/2539-douluo-dalu.html">Боевой континент ~ (В течение дня)</a>
    <a href="/tip/tv/2756-the-magic-chef-of-fire-and-ice.html">Демон-шеф Льда и Пламени ~ (В течение дня)</a>
    </div>
    <a style="display: block; margin-top: 5px; background: #ffb84d; color: #fff; font-weight: bold; text-transform: uppercase; font-size: 18px; padding:6px 0; text-align: center;" href="javascript:ShowOrHide('raspisSun')">Воскресенье</a>
    <div id="raspisSun" style="display: none;" class="raspis">
   
    <a href="/tip/tv/179-one-piece.html">Ван Пис ~ (09:00)</a>
    <a href="/tip/tv/1805-boruto-naruto-next-generations111.html">Боруто: Новое поколение Наруто ~ (14:00)</a>
    <a href="/tip/tv/2803-kono-healer-mendokusai.html">Этот противный целитель! ~ (16:30)</a>
    <a href="/tip/tv/2741-baraou-no-souretsu.html">Похороны Короля Роз ~ (18:00)</a>
    <a href="/tip/tv/2785-otome-game-sekai-wa-mob-ni-kibishii-sekai-desu.html">Мир отомэ-игр - это тяжёлый мир для мобов ~ (19:00)</a>
    <a href="/tip/tv/2773-black-rock-shooter-dawn-fall.html">Стрелок с чёрной скалы: Падение ~ (20:00)</a>
        
    </div>
        <p style="padding: 6px 4px 7px 4px; display: block; text-align: center; color:red; font-weight: bold; font-size: 12px;">Указано время выхода релиза в русской озвучке. (Московское)</p>
    </div>
"""
schedule_data = {
    'monday': [
        AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html', anime_composed=[]),
        AnimeMin(id_anime=2804, link='https://animevost.org/tip/tv/2804-honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen-3rd-season.html', anime_composed=[])
    ],
    'tuesday': [
        AnimeMin(id_anime=2774, link='https://animevost.org/tip/tv/2774-yuusha-yamemasu.html', anime_composed=[]),
        AnimeMin(id_anime=2755, link='https://animevost.org/tip/tv/2755-zi-chuan.html', anime_composed=[]),
        AnimeMin(id_anime=2789, link='https://animevost.org/tip/tv/2789-tomodachi-game.html', anime_composed=[]),
        AnimeMin(id_anime=2810, link='https://animevost.org/tip/tv/2810-the-last-summoner.html', anime_composed=[])
    ],
    'wednesday': [
        AnimeMin(id_anime=2786, link='https://animevost.org/tip/tv/2786-shijou-saikyou-no-daimaou-murabito-a-ni-tensei-suru.html', anime_composed=[]),
        AnimeMin(id_anime=2788, link='https://animevost.org/tip/tv/2788-rpg-fudousan.html', anime_composed=[]),
        AnimeMin(id_anime=2791, link='https://animevost.org/tip/tv/2791-tate-no-yuusha-no-nariagari-2nd-season.html', anime_composed=[]),
        AnimeMin(id_anime=2775, link='https://animevost.org/tip/tv/2775-deaimon.html', anime_composed=[]),
        AnimeMin(id_anime=2776, link='https://animevost.org/tip/tv/2776-komi-san-wa-comyushou-desu-2nd-season.html', anime_composed=[]),
        AnimeMin(id_anime=2761, link='https://animevost.org/tip/tv/2761-tunshi-xingkong.html', anime_composed=[])
    ],
    'thursday': [
        AnimeMin(id_anime=2794, link='https://animevost.org/tip/tv/2794-shachiku-san-wa-youjo-yuurei-ni-iyasaretai.html', anime_composed=[]),
        AnimeMin(id_anime=2793, link='https://animevost.org/tip/tv/2793-heroine-tarumono-kiraware-heroine-to-naisho-no-oshigoto.html', anime_composed=[]),
        AnimeMin(id_anime=2792, link='https://animevost.org/tip/tv/2792-gaikotsu-kishi-sama-tadaima-isekai-e-odekakechuu.html', anime_composed=[]),
        AnimeMin(id_anime=2787, link='https://animevost.org/tip/tv/2787-paripi-koumei.html', anime_composed=[]),
        AnimeMin(id_anime=2807, link='https://animevost.org/tip/tv/2807-summer-time-render.html', anime_composed=[]),
        AnimeMin(id_anime=2777, link='https://animevost.org/tip/tv/2777-machikado-mazoku-2-choume.html', anime_composed=[]),
        AnimeMin(id_anime=2779, link='https://animevost.org/tip/tv/2779-mahoutsukai-reimeiki.html', anime_composed=[])
    ],
    'friday': [
        AnimeMin(id_anime=2800, link='https://animevost.org/tip/tv/2800-date-a-live-iv.html', anime_composed=[]),
        AnimeMin(id_anime=2778, link='https://animevost.org/tip/tv/2778-koi-wa-sekai-seifuku-no-ato-de.html', anime_composed=[]),
        AnimeMin(id_anime=2790, link='https://animevost.org/tip/tv/2790-kaguya-sama-wa-kokurasetai-ultra-romantic.html', anime_composed=[]),
        AnimeMin(id_anime=2783, link='https://animevost.org/tip/tv/2783-rikei-ga-koi-ni-ochita-no-de-shoumei-shitemita-heart.html', anime_composed=[]),
        AnimeMin(id_anime=2781, link='https://animevost.org/tip/tv/2781-shokei-shoujo-no-virgin-road.html', anime_composed=[]),
        AnimeMin(id_anime=2771, link='https://animevost.org/tip/tv/2771-aharen-san-wa-hakarenai.html', anime_composed=[]),
        AnimeMin(id_anime=2796, link='https://animevost.org/tip/tv/2796-dance-dance-danseur.html', anime_composed=[])
    ],
    'saturday': [
        AnimeMin(id_anime=2772, link='https://animevost.org/tip/tv/2772-love-all-play.html', anime_composed=[]),
        AnimeMin(id_anime=2780, link='https://animevost.org/tip/tv/2780-ao-ashi.html', anime_composed=[]),
        AnimeMin(id_anime=2782, link='https://animevost.org/tip/tv/2782-gunjou-no-fanfare.html', anime_composed=[]),
        AnimeMin(id_anime=2798, link='https://animevost.org/tip/tv/2798-spy-x-family.html', anime_composed=[]),
        AnimeMin(id_anime=2802, link='https://animevost.org/tip/tv/2802-kunoichi-tsubaki-no-mune-no-uchi.html', anime_composed=[]),
        AnimeMin(id_anime=2801, link='https://animevost.org/tip/tv/2801-kingdom-4.html', anime_composed=[]),
        AnimeMin(id_anime=2797, link='https://animevost.org/tip/tv/2797-build-divide-code-white.html', anime_composed=[]),
        AnimeMin(id_anime=2808, link='https://animevost.org/tip/tv/2808-kakkou-no-iinazuke.html', anime_composed=[]),
        AnimeMin(id_anime=2799, link='https://animevost.org/tip/tv/2799-kawaii-dake-ja-nai-shikimori-san.html', anime_composed=[]),
        AnimeMin(id_anime=2539, link='https://animevost.org/tip/tv/2539-douluo-dalu.html', anime_composed=[]),
        AnimeMin(id_anime=2756, link='https://animevost.org/tip/tv/2756-the-magic-chef-of-fire-and-ice.html', anime_composed=[])
    ],
    'sunday': [
        AnimeMin(id_anime=179, link='https://animevost.org/tip/tv/179-one-piece.html', anime_composed=[]),
        AnimeMin(id_anime=1805, link='https://animevost.org/tip/tv/1805-boruto-naruto-next-generations111.html', anime_composed=[]),
        AnimeMin(id_anime=2803, link='https://animevost.org/tip/tv/2803-kono-healer-mendokusai.html', anime_composed=[]),
        AnimeMin(id_anime=2741, link='https://animevost.org/tip/tv/2741-baraou-no-souretsu.html', anime_composed=[]),
        AnimeMin(id_anime=2785, link='https://animevost.org/tip/tv/2785-otome-game-sekai-wa-mob-ni-kibishii-sekai-desu.html', anime_composed=[]),
        AnimeMin(id_anime=2773, link='https://animevost.org/tip/tv/2773-black-rock-shooter-dawn-fall.html', anime_composed=[])
    ]
}

schedule_data_false = {
    'monday': [
        AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html', anime_composed=None),
        AnimeMin(id_anime=2804, link='https://animevost.org/tip/tv/2804-honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen-3rd-season.html', anime_composed=None)
    ],
    'tuesday': [
        AnimeMin(id_anime=2774, link='https://animevost.org/tip/tv/2774-yuusha-yamemasu.html', anime_composed=None),
        AnimeMin(id_anime=2755, link='https://animevost.org/tip/tv/2755-zi-chuan.html', anime_composed=None),
        AnimeMin(id_anime=2789, link='https://animevost.org/tip/tv/2789-tomodachi-game.html', anime_composed=None),
        AnimeMin(id_anime=2810, link='https://animevost.org/tip/tv/2810-the-last-summoner.html', anime_composed=None)
    ],
    'wednesday': [
        AnimeMin(id_anime=2786, link='https://animevost.org/tip/tv/2786-shijou-saikyou-no-daimaou-murabito-a-ni-tensei-suru.html', anime_composed=None),
        AnimeMin(id_anime=2788, link='https://animevost.org/tip/tv/2788-rpg-fudousan.html', anime_composed=None),
        AnimeMin(id_anime=2791, link='https://animevost.org/tip/tv/2791-tate-no-yuusha-no-nariagari-2nd-season.html', anime_composed=None),
        AnimeMin(id_anime=2775, link='https://animevost.org/tip/tv/2775-deaimon.html', anime_composed=None),
        AnimeMin(id_anime=2776, link='https://animevost.org/tip/tv/2776-komi-san-wa-comyushou-desu-2nd-season.html', anime_composed=None),
        AnimeMin(id_anime=2761, link='https://animevost.org/tip/tv/2761-tunshi-xingkong.html', anime_composed=None)
    ],
    'thursday': [
        AnimeMin(id_anime=2794, link='https://animevost.org/tip/tv/2794-shachiku-san-wa-youjo-yuurei-ni-iyasaretai.html', anime_composed=None),
        AnimeMin(id_anime=2793, link='https://animevost.org/tip/tv/2793-heroine-tarumono-kiraware-heroine-to-naisho-no-oshigoto.html', anime_composed=None),
        AnimeMin(id_anime=2792, link='https://animevost.org/tip/tv/2792-gaikotsu-kishi-sama-tadaima-isekai-e-odekakechuu.html', anime_composed=None),
        AnimeMin(id_anime=2787, link='https://animevost.org/tip/tv/2787-paripi-koumei.html', anime_composed=None),
        AnimeMin(id_anime=2807, link='https://animevost.org/tip/tv/2807-summer-time-render.html', anime_composed=None),
        AnimeMin(id_anime=2777, link='https://animevost.org/tip/tv/2777-machikado-mazoku-2-choume.html', anime_composed=None),
        AnimeMin(id_anime=2779, link='https://animevost.org/tip/tv/2779-mahoutsukai-reimeiki.html', anime_composed=None)
    ],
    'friday': [
        AnimeMin(id_anime=2800, link='https://animevost.org/tip/tv/2800-date-a-live-iv.html', anime_composed=None),
        AnimeMin(id_anime=2778, link='https://animevost.org/tip/tv/2778-koi-wa-sekai-seifuku-no-ato-de.html', anime_composed=None),
        AnimeMin(id_anime=2790, link='https://animevost.org/tip/tv/2790-kaguya-sama-wa-kokurasetai-ultra-romantic.html', anime_composed=None),
        AnimeMin(id_anime=2783, link='https://animevost.org/tip/tv/2783-rikei-ga-koi-ni-ochita-no-de-shoumei-shitemita-heart.html', anime_composed=None),
        AnimeMin(id_anime=2781, link='https://animevost.org/tip/tv/2781-shokei-shoujo-no-virgin-road.html', anime_composed=None),
        AnimeMin(id_anime=2771, link='https://animevost.org/tip/tv/2771-aharen-san-wa-hakarenai.html', anime_composed=None),
        AnimeMin(id_anime=2796, link='https://animevost.org/tip/tv/2796-dance-dance-danseur.html', anime_composed=None)
    ],
    'saturday': [
        AnimeMin(id_anime=2772, link='https://animevost.org/tip/tv/2772-love-all-play.html', anime_composed=None),
        AnimeMin(id_anime=2780, link='https://animevost.org/tip/tv/2780-ao-ashi.html', anime_composed=None),
        AnimeMin(id_anime=2782, link='https://animevost.org/tip/tv/2782-gunjou-no-fanfare.html', anime_composed=None),
        AnimeMin(id_anime=2798, link='https://animevost.org/tip/tv/2798-spy-x-family.html', anime_composed=None),
        AnimeMin(id_anime=2802, link='https://animevost.org/tip/tv/2802-kunoichi-tsubaki-no-mune-no-uchi.html', anime_composed=None),
        AnimeMin(id_anime=2801, link='https://animevost.org/tip/tv/2801-kingdom-4.html', anime_composed=None),
        AnimeMin(id_anime=2797, link='https://animevost.org/tip/tv/2797-build-divide-code-white.html', anime_composed=None),
        AnimeMin(id_anime=2808, link='https://animevost.org/tip/tv/2808-kakkou-no-iinazuke.html', anime_composed=None),
        AnimeMin(id_anime=2799, link='https://animevost.org/tip/tv/2799-kawaii-dake-ja-nai-shikimori-san.html', anime_composed=None),
        AnimeMin(id_anime=2539, link='https://animevost.org/tip/tv/2539-douluo-dalu.html', anime_composed=None),
        AnimeMin(id_anime=2756, link='https://animevost.org/tip/tv/2756-the-magic-chef-of-fire-and-ice.html', anime_composed=None)
    ],
    'sunday': [
        AnimeMin(id_anime=179, link='https://animevost.org/tip/tv/179-one-piece.html', anime_composed=None),
        AnimeMin(id_anime=1805, link='https://animevost.org/tip/tv/1805-boruto-naruto-next-generations111.html', anime_composed=None),
        AnimeMin(id_anime=2803, link='https://animevost.org/tip/tv/2803-kono-healer-mendokusai.html', anime_composed=None),
        AnimeMin(id_anime=2741, link='https://animevost.org/tip/tv/2741-baraou-no-souretsu.html', anime_composed=None),
        AnimeMin(id_anime=2785, link='https://animevost.org/tip/tv/2785-otome-game-sekai-wa-mob-ni-kibishii-sekai-desu.html', anime_composed=None),
        AnimeMin(id_anime=2773, link='https://animevost.org/tip/tv/2773-black-rock-shooter-dawn-fall.html', anime_composed=None)
    ]
}

schedule_html_error_day = """
<div class="interDubBgTwo"></div>
"""

schedule_html_error_id = """
<div id="raspisMon" style="display: none;" class="raspis">
        <a href="/tip/tv2696kyoukai-senki.html">Воины Пограничья  ~ (21:30)</a>
        <a href="/tip/tv2804honzuki-no-gekokujou-shisho-ni-naru-tame-ni-wa-shudan-wo-erandeiraremasen-3rd-season.html">Власть книжного червя: Чтобы стать библиотекарем, все средства хороши (третий сезон)  ~ (23:00)</a>
</div>
"""

anime_composed_html = """
<div id="sp4e5cebc98832797d3c8385c9b9129663" class="text_spoiler" style="">
    <ol>
        <li><a href="/tip/tv/108-kingdom.html" target="_blank" title="Царство">Царство</a> - ТВ (38 эп.), адаптация манги, 2012</li>
        <li><a href="/109-kingdom-2.html" target="_blank" title="Царство (второй сезон)">Царство (второй сезон)</a> - ТВ (39 эп.), продолжение, 2013</li>
        <li><a href="/tip/tv/2436-kingdom-3.html" target="_blank" title="Царство (третий сезон)">Царство (третий сезон)</a> - ТВ (26 эп.), продолжение, 2013</li>
        <li><a href="/tip/tv/2801-kingdom-4.html" target="_blank" title="Царство (четвёртый сезон)">Царство (четвёртый сезон)</a> - ТВ (&gt;12 эп.), продолжение, 2022</li>
    </ol>
</div>
"""

anime_composed_data = [
    AnimeComposed(id_anime=108, link='https://animevost.org/tip/tv/108-kingdom.html'),
    AnimeComposed(id_anime=109, link='https://animevost.org/109-kingdom-2.html'),
    AnimeComposed(id_anime=2436, link='https://animevost.org/tip/tv/2436-kingdom-3.html'),
    AnimeComposed(id_anime=2801, link='https://animevost.org/tip/tv/2801-kingdom-4.html')
]

anime_composed_data_id = [
    AnimeComposed(id_anime=108, link='https://animevost.org/tip/tv/108-kingdom.html'),
    AnimeComposed(id_anime=2436, link='https://animevost.org/tip/tv/2436-kingdom-3.html'),
    AnimeComposed(id_anime=2801, link='https://animevost.org/tip/tv/2801-kingdom-4.html')
]

count_page_html = """
<td class="block_4"><span>1</span> <a href="https://animevost.org/preview/page/2/">2</a> </td>
"""

count_page_html_not_int = """
<td class="block_4"><span>1</span> <a href="https://animevost.org/preview/page/2/">a</a> </td>
"""

count_page_not_html = """
<html><html/>
"""

anons_html = """ 
<div class="shortstoryHead">           
    <h2>
        <a href="https://animevost.org/tip/tv/2827-overlord-4.html">Повелитель (четвёртый сезон) / Overlord IV [Анонс] [1 серия - 5 июля]</a>
    </h2>
</div>

<div class="shortstoryHead">            
    <h2>
        <a href="https://animevost.org/tip/tv/2825-kami-kuzu-idol.html">Богиня идола-мерзавца / Kami Kuzu Idol [Анонс] [1 серия - 2 июля]</a>
    </h2>
</div>
"""

anons_data = [
    AnimeMin(id_anime=2827, link='https://animevost.org/tip/tv/2827-overlord-4.html', anime_composed=[]),
    AnimeMin(id_anime=2825, link='https://animevost.org/tip/tv/2825-kami-kuzu-idol.html', anime_composed=[])
]

anons_data_false = [
    AnimeMin(id_anime=2827, link='https://animevost.org/tip/tv/2827-overlord-4.html', anime_composed=None),
    AnimeMin(id_anime=2825, link='https://animevost.org/tip/tv/2825-kami-kuzu-idol.html', anime_composed=None)
]

anime_json = {
    'data': [
        {
            'screenImage': [
                "/uploads/posts/2013-06/1371576836_2.jpg",
                "/uploads/posts/2013-06/1371576773_3.jpg",
                "/uploads/posts/2013-06/1371576794_4.jpg"
            ],
            'rating': 4935,
            'description': 'description',
            'director': "Камия Дзюн",
            'urlImagePreview': "/uploads/posts/2013-11/1384972471_carstvo.jpg",
            'year': "2012",
            'genre': "приключения, история",
            'id': 108,
            'votes': 1029,
            'title': "Царство / Kingdom [1-38 из 38]",
            'timer': 0,
            'type': "ТВ",
        }
    ]
}

anime_data = Anime(
    id=108,
    title='Царство / Kingdom [1-38 из 38]',
    screen_image=[
        'https://animevost.org/uploads/posts/2013-06/1371576836_2.jpg',
        'https://animevost.org/uploads/posts/2013-06/1371576773_3.jpg',
        'https://animevost.org/uploads/posts/2013-06/1371576794_4.jpg'
    ],
    rating=4935,
    votes=1029,
    description='description',
    director='Камия Дзюн',
    url_image_preview='https://animevost.org/uploads/posts/2013-11/1384972471_carstvo.jpg',
    year='2012',
    genre='приключения, история',
    timer=0,
    type='ТВ'
)

last_anime_json = {
    'data': [
        {
            'screenImage': [
                "/uploads/posts/2022-01/1641826701_2.jpg",
                "/uploads/posts/2022-01/1641826779_3.jpg",
                "/uploads/posts/2022-01/1641826762_4.jpg"
            ],
            'rating': 5922,
            'votes': 1347,
            'description': "description",
            'title': "Пожиратель звёзд / Tunshi Xingkong [1-41 из 52+]",
            'count': "52+ (25 мин.)",
            'timer': 0,
            'director': "",
            'urlImagePreview': "/uploads/posts/2022-01/1641826763_1.jpg",
            'year': "2020",
            'genre': "приключения, фантастика",
            'type': "ТВ",
            'id': 2761,
        },
        {
            'screenImage': [
                "/uploads/posts/2022-04/1649099091_4.jpg",
                "/uploads/posts/2022-04/1649099002_3.jpg",
                "/uploads/posts/2022-04/1649099074_2.jpg"
            ],
            'rating': 13717,
            'votes': 3157,
            'description': "description",
            'title': "Перестану быть героем / Yuusha, Yamemasu [1-12 из 12] [ОВА 1 из 1]",
            'count': "12 (25 мин.)",
            'timer': 0,
            'director': "Нобута Ю",
            'urlImagePreview': "/uploads/posts/2022-03/1647531170_2.jpg",
            'year': "2022",
            'genre': "приключения, фэнтези, комедия",
            'type': "ТВ",
            'id': 2774,
        },
    ]
}

last_anime_data = [
    Anime(
        id=2761,
        title='Пожиратель звёзд / Tunshi Xingkong [1-41 из 52+]',
        screen_image=[
            'https://animevost.org/uploads/posts/2022-01/1641826701_2.jpg',
            'https://animevost.org/uploads/posts/2022-01/1641826779_3.jpg',
            'https://animevost.org/uploads/posts/2022-01/1641826762_4.jpg'
        ],
        rating=5922,
        votes=1347,
        description='description',
        director='',
        url_image_preview='https://animevost.org/uploads/posts/2022-01/1641826763_1.jpg',
        year='2020',
        genre='приключения, фантастика',
        timer=0,
        type='ТВ')
    ,
    Anime(
        id=2774,
        title='Перестану быть героем / Yuusha, Yamemasu [1-12 из 12] [ОВА 1 из 1]',
        screen_image=[
            'https://animevost.org/uploads/posts/2022-04/1649099091_4.jpg',
            'https://animevost.org/uploads/posts/2022-04/1649099002_3.jpg',
            'https://animevost.org/uploads/posts/2022-04/1649099074_2.jpg'
        ],
        rating=13717,
        votes=3157,
        description='description',
        director='Нобута Ю',
        url_image_preview='https://animevost.org/uploads/posts/2022-03/1647531170_2.jpg',
        year='2022',
        genre='приключения, фэнтези, комедия',
        timer=0,
        type='ТВ')
]

search_json = {
    'data': [
        {'screenImage': ['', '', ''],
         'rating': 421,
         'description': 'description',
         'director': 'Кавай Сигэки',
         'urlImagePreview': 'https://static.openni.ru/uploads/posts/2022-06/1656338413_1.jpg',
         'year': '2022',
         'genre': 'фэнтези, комедия',
         'id': 2829,
         'votes': 95,
         'title': 'Перерождение Дяди / Isekai Ojisan [1 из 12+] [2 серия - 13 июля]',
         'timer': 0,
         'type': 'ТВ'
         }
    ]
}

search_data = [
    Anime(
        id=2829,
        title='Перерождение Дяди / Isekai Ojisan [1 из 12+] [2 серия - 13 июля]',
        screen_image=[],
        rating=421,
        votes=95,
        description='description',
        director='Кавай Сигэки',
        url_image_preview='https://static.openni.ru/uploads/posts/2022-06/1656338413_1.jpg',
        year='2022',
        genre='фэнтези, комедия',
        timer=0,
        type='ТВ'
    )
]

anime_schemas_dict = {
    'screenImage': [
        "/uploads/posts/2022-01/1641826701_2.jpg",
        "/uploads/posts/2022-01/1641826779_3.jpg",
        "/uploads/posts/2022-01/1641826762_4.jpg"
    ],
    'rating': 5922,
    'votes': 1347,
    'description': "description",
    'title': "Пожиратель звёзд / Tunshi Xingkong [1-41 из 52+]",
    'count': "52+ (25 мин.)",
    'timer': 0,
    'director': "",
    'urlImagePreview': "/uploads/posts/2022-01/1641826763_1.jpg",
    'year': "2020",
    'genre': "приключения, фантастика",
    'type': "ТВ",
    'id': 2761,
}

anime_schemas_data = Anime(
    id=2761,
    title='Пожиратель звёзд / Tunshi Xingkong [1-41 из 52+]',
    screen_image=[
        'https://animevost.org/uploads/posts/2022-01/1641826701_2.jpg',
        'https://animevost.org/uploads/posts/2022-01/1641826779_3.jpg',
        'https://animevost.org/uploads/posts/2022-01/1641826762_4.jpg'
    ],
    rating=5922,
    votes=1347,
    description='description',
    director='',
    url_image_preview='https://animevost.org/uploads/posts/2022-01/1641826763_1.jpg',
    year='2020',
    genre='приключения, фантастика',
    timer=0,
    type='ТВ'
)

play_list_json = [
    {
        'std': 'http://video.animetop.info/2147423318.mp4',
        'preview': 'http://media.aniland.org/img/2147423318.jpg',
        'name': 'Фильм',
        'hd': 'http://video.animetop.info/720/2147423318.mp4'
    },
    {
        'std': 'http://video.animetop.info/640454801.mp4',
        'preview': 'http://media.aniland.org/img/2147423318.jpg',
        'name': '27 серия',
        'hd': 'http://video.animetop.info/720/640454801.mp4'
    }
]

play_list_data = [
    Series(
        name='Фильм',
        serial='2147423318',
        preview='http://media.aniland.org/img/2147423318.jpg'
    ),
    Series(
        name='27 серия',
        serial='640454801',
        preview='http://media.aniland.org/img/2147423318.jpg'
    )
]

anons_error_attribute = '<html><div class="shortstoryHead"></div></html>'

get_schedule_data = {
    'monday': [
        AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html', anime_composed=None)
    ]
}

get_schedule_data_full = {
    'monday': [
        AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
                 anime_composed=[AnimeComposed(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html')])
    ]
}

get_anime_data = Anime(
    id=2696,
    title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
    screen_image=[
        'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
        'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
        'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
    ],
    rating=3190,
    votes=888,
    description='description',
    director='Хабара Нобуёси',
    url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
    year='2021',
    genre='приключения, фантастика, меха',
    timer=0,
    type='ТВ'
)

get_data_anime_data = {
    'monday': [
        AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика, меха',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[]
        )]
}

get_data_anime_data_full = {
    'monday': [
        AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика, меха',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[AnimeData(
                id=2696,
                title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
                screen_image=[
                    'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                    'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                    'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
                ],
                rating=3190,
                votes=888,
                description='description',
                director='Хабара Нобуёси',
                url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
                year='2021',
                genre='приключения, фантастика, меха',
                timer=0,
                type='ТВ',
                link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            )]
        )]
}

create_anime_full_list = [
    AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html', anime_composed=None)
]

create_anime_full_list_data = [AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика, меха',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[]
)]

create_anime_full_list_composed = [
    AnimeMin(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html', anime_composed=[AnimeComposed(id_anime=2696, link='https://animevost.org/tip/tv/2696-kyoukai-senki.html')])
]

create_anime_full_list_composed_data = [AnimeFull(
            id=2696,
            title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
            screen_image=[
                'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
            ],
            rating=3190,
            votes=888,
            description='description',
            director='Хабара Нобуёси',
            url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
            year='2021',
            genre='приключения, фантастика, меха',
            timer=0,
            type='ТВ',
            link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            anime_composed=[AnimeData(
                id=2696,
                title='Воины Пограничья / Kyoukai Senki [1-25 из 25]',
                screen_image=[
                    'https://animevost.org/uploads/posts/2021-10/1633975183_4.jpg',
                    'https://animevost.org/uploads/posts/2021-10/1633975182_3.jpg',
                    'https://animevost.org/uploads/posts/2021-10/1633975209_2.jpg'
                ],
                rating=3190,
                votes=888,
                description='description',
                director='Хабара Нобуёси',
                url_image_preview='https://animevost.org/uploads/posts/2021-10/1633371168_1.jpg',
                year='2021',
                genre='приключения, фантастика, меха',
                timer=0,
                type='ТВ',
                link='https://animevost.org/tip/tv/2696-kyoukai-senki.html',
            )]
)]

anime_one_data = AnimeMin(
    id_anime=108,
    link='https://test',
    anime_composed=[
        AnimeComposed(id_anime=109, link='https://animevost.org/109-kingdom-2.html'),
        AnimeComposed(id_anime=2436, link='https://animevost.org/tip/tv/2436-kingdom-3.html'),
        AnimeComposed(id_anime=2801, link='https://animevost.org/tip/tv/2801-kingdom-4.html')
    ]
)
