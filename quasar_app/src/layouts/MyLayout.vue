<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          <div class="row text-subtitle2 q-pa-sm">
            <div class="col-3 text-weight-bold text-subtitle1">Gag Meme</div>
            <div class="col-1 cursor-pointer q-mt-xs">App</div>
            <div class="col-1 cursor-pointer q-mt-xs">Shop</div>
            <div class="col-1 cursor-pointer q-mt-xs">Meme</div>
            <div class="col-1 cursor-pointer q-mt-xs">Local</div>
            <div class="col-1 cursor-pointer q-mt-xs">Cosplay</div>
            <div class="col-1 cursor-pointer q-mt-xs">Random</div>
            <div class="col-1 cursor-pointer q-mt-xs">3am Chat</div>
            <div class="col-1 cursor-pointer">
               <q-btn flat round @click="$q.dark.toggle()" size="10px" :icon="$q.dark.isActive ? 'nights_stay' : 'wb_sunny'" />
<!--              <q-icon name="brightness_2" size="25px"></q-icon>-->
            </div>
            <div class="col-1 q-mt-xs">
              <q-btn label="Sign up" size="sm" @click="$router.push('/login')"></q-btn>
            </div>
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <div class="row">
        <div class="col-2">
          <q-card class="full-height">
            <q-card-section class="q-py-sm text-h6 text-grey-8" style="border-bottom: 2px solid #1e8081">
              <q-input label="search" v-model="search">
                <template v-slot:append>
                  <q-icon name="search"/>
                </template>
              </q-input>
              <q-list dense class="q-mt-sm">

                <q-item class="q-py-none" clickable v-ripple v-for="item in sidebar_options">
                  <q-item-section class="q-py-none">
                    <q-item-label caption lines="2" >
                      <q-icon class="q-mr-sm" :class="$q.dark.isActive ? 'text-white' : 'text-black'" :name="item.icon" size="18px"/>
                      <span :class="$q.dark.isActive ? 'text-white' : 'text-black'"> {{item.label}}</span>
                    </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>

              <q-list dense class="text-black" style="">
                <q-item-label header>Popular</q-item-label>
                <q-item class="q-py-none" clickable v-ripple v-for="item in popular" @click="$router.push('/category/'+item.value)">
                  <q-item-section class="q-py-none">

                    <q-item-label caption lines="2">
                      <q-avatar rounded size="sm">
                        <img :src="item.icon">
                      </q-avatar>
                      <span class="q-pl-sm"  :class="$q.dark.isActive ? 'text-white' : 'text-black'">{{item.label}}</span>
                    </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>

              <q-list dense class="text-black" style="">
                <q-item-label header>Sections</q-item-label>
                <q-item class="q-py-none" clickable v-ripple v-for="item in sections" @click="$router.push('/category/'+item.value)">
                  <q-item-section class="q-py-none">
                    <q-item-label caption lines="2">
                      <q-avatar rounded size="sm">
                        <img :src="item.icon">
                      </q-avatar>
                      <span class="q-pl-sm" :class="$q.dark.isActive ? 'text-white' : 'text-black'">{{item.label}}</span>
                    </q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>
        </div>

        <div class="col-10">
          <div class="row">
      <div class="col-12">
      <q-carousel
        v-model="slide"
        transition-prev="scale"
        transition-next="scale"
        swipeable
        animated
        control-color="white"
        navigation
        arrows
        height="300px"
        class="bg-grey-5 text-white shadow-1 rounded-borders q-pa-none"
      >
        <q-carousel-slide name="style" class="column no-wrap flex-center q-pa-none">
          <q-img contain src="statics/carousel/carousel_4.jpg"/>
        </q-carousel-slide>
        <q-carousel-slide name="tv" class="column no-wrap flex-center q-pa-none">
          <q-img contain src="statics/carousel/carousel_1.jpg"/>
        </q-carousel-slide>
        <q-carousel-slide name="layers" class="column no-wrap flex-center q-pa-none">
          <q-img contain src="statics/carousel/carousel_2.jpg"/>
        </q-carousel-slide>
        <q-carousel-slide name="cars" class="column no-wrap flex-center q-pa-none">
          <q-img contain src="statics/carousel/carousel_3.jpg"/>
        </q-carousel-slide>

      </q-carousel>
        </div>
    </div>
          <div class="row">
            <div class="col-8">
              <router-view/>
            </div>
            <div class="col-4 q-mt-sm">
              <q-card class="my-card" flat bordered>
                <q-img
                  src="statics/right_sidebar/metallica.jpeg"
                />
                <q-card-section class="q-pa-none">
                  <div class="text-5  q-mb-xs cursor-pointer ">The world right now !!!!!!!!</div>
                </q-card-section>
              </q-card>
              <q-card class="my-card" flat bordered>
                <q-img
                  src="statics/right_sidebar/bane.jpeg"
                />
                <q-card-section class="q-pa-none">
                  <div class="text-5 q-mb-xs cursor-pointer">He saw the Danger before we did.</div>
                </q-card-section>
              </q-card>
            </div>
          </div>

        </div>
      </div>

    </q-page-container>
  </q-layout>
</template>

<script>
    export default {
        name: 'MyLayout',

        data() {
            return {
                leftDrawerOpen: false,
                left_mini_drawer_open: false,
                left_drawer_open: false,
                slide:'style',
                search: '',
                sidebar_options: [{'label': 'Hot', 'value': 'hot', 'icon': 'fireplace'}, {
                    'label': 'New',
                    'value': 'new',
                    'icon': 'add'
                }, {'label': 'Trending', 'value': 'trending', 'icon': 'trending_up'}, {
                    'label': 'Fresh',
                    'value': 'fresh',
                    'icon': 'refresh'
                }],
                popular:[
                    {'label':'India', 'value':'india', 'icon':'statics/layout_images/india.webp', 'description':'Everything about India', 'tags':[]},
                    {'label':'Funny', 'value':'funny', 'icon':'statics/layout_images/funny.webp', 'description':'Why so serious', 'tags':['Funny', 'Meme', 'Savage', 'Surreal Meme', 'Dank']},
                    {'label':'Animals', 'value':'animals', 'icon':'statics/layout_images/animals.webp', 'description':'It is so fluffy I am gonna die!', 'tags':['Baby Animal', 'Transformation', 'Cat', 'Dog', 'Puppy']},
                    {'label':'Anime & Manga', 'value':'anime_manga', 'icon':'statics/layout_images/anime_manga.webp', 'description':'Anime memes, news, GIFs and discussions.', 'tags':['Demon Slayer', 'Nezuko', 'Komi San', 'Jojo', 'My Hero Academia', 'Goblin','SAO' ]},
                    {'label':'Anime Waifu', 'value':'anime_waifu', 'icon':'statics/layout_images/anime_waifu.webp', 'description':'Anime girl illustrations, fan art… No sexually explicit content.', 'tags':['Komi San', 'Saber', 'Nezuko','Asuna', 'Raphtalia']},
                    {'label':'Awesome', 'value':'awesome', 'icon':'statics/layout_images/awesome.webp', 'description':'Things that make you WOW', 'tags':['Satisfying', 'Landscape', 'Perfect']},
                    {'label':'Car', 'value':'car', 'icon':'statics/layout_images/car.webp', 'description':'Vroom vroom!', 'tags':['Tesla', 'Top Gear', 'Supercar', 'Ferrari']},
                    {'label':'Comic & Webtoon', 'value':'comic', 'icon':'statics/layout_images/comic.webp', 'description':'Digital comic, webtoon, rage comic, countryball', 'tags':['Loading Artist', 'Rage Comic', 'Webtoon']},
                    {'label':'Cosplay', 'value':'cosplay', 'icon':'statics/layout_images/cosplay.webp', 'description':'Be the character you love', 'tags':['Comic Con', 'Jessica']},
                    {'label':'Gaming', 'value':'gaming', 'icon':'statics/layout_images/gaming.webp', 'description':'We do not die, we respawn!', 'tags':['GTA', 'Fortnite', 'Mincraft', 'Red Dead Redemption 2', 'God of War', 'PUBG']},
                    {'label':'GIF', 'value':'gif', 'icon':'statics/layout_images/gif.webp', 'description':'Let us loop the fun', 'tags':[]},
                    {'label':'League of Legends', 'value':'league_of_legends', 'icon':'statics/layout_images/league_of_legends.webp', 'description':'Welcome to the summoner s rift', 'tags':[]},
                    {'label':'Meme', 'value':'meme', 'icon':'statics/layout_images/meme.webp', 'description':'Dank meme, Classical meme, surreal meme, art meme', 'tags':['Dank Meme', 'Surreal meme']},
                    {'label':'Politics', 'value':'politics', 'icon':'statics/layout_images/politics.webp', 'description':'Political jokes. Deep or derp.', 'tags':['Putin', 'Obama', 'Trump']},
                ],
                sections:[
                    {'label':'Anime Wallpaper', 'value':'anime_wallpaper', 'icon':'statics/layout_images/anime_wallpaper.webp', 'description':'Anime-style wallpaper for desktop & mobile. No sexually explicit content.'},
                    {'label':'Apex Legends', 'value':'apex_legends', 'icon':'statics/layout_images/apex_legends.webp', 'description':'A new battle royale experience'},
                    {'label':'Drawing and DIY', 'value':'drawing', 'icon':'statics/layout_images/drawing.webp', 'description':'Illustration, wood work, drawing & painting, Metalsmithing'},
                    {'label':'Food & Drinks', 'value':'food_drinks', 'icon':'statics/layout_images/food_drinks.webp', 'description':'Crazy foodies'},
                    {'label':'Football', 'value':'football', 'icon':'statics/layout_images/football.webp', 'description':'Premier League, La Liga, Bundesliga, Serie A'},
                    {'label':'Fortnite', 'value':'fortnite', 'icon':'statics/layout_images/fortnite.webp', 'description':'Fortnite Battle Royale'},
                    {'label':'Game of Thrones', 'value':'got', 'icon':'statics/layout_images/got.webp', 'description':'GoT memes, discussions, season recap'},
                    {'label':'History', 'value':'history', 'icon':'statics/layout_images/history.webp', 'description':'Rediscover the past'},
                    {'label':'Horror', 'value':'horror', 'icon':'statics/layout_images/horror.webp', 'description':'Fear to the limit of fun'},
                    {'label':'LEGO', 'value':'lego', 'icon':'statics/layout_images/lego.webp', 'description':'Build what you want'},
                    {'label':'Marvel & DC', 'value':'marvel_dc', 'icon':'statics/layout_images/marvel_dc.webp', 'description':'MCU, DCEU movie reviews, superhero comics'},
                    {'label':'Movie & TV', 'value':'movie_tv', 'icon':'statics/layout_images/movie_tv.webp', 'description':'A way to escape from real world'},
                    {'label':'Music', 'value':'music', 'icon':'statics/layout_images/music.webp', 'description':'Drop the beat now'},
                    {'label':'Overwatch', 'value':'overwatch', 'icon':'statics/layout_images/overwatch.webp', 'description':'Heroes never die'}
                ]


            }
        },
        methods: {
            openMiniDrawer() {
                this.left_mini_drawer_open = true;
                this.left_drawer_open = false;
            },
        }
    }
</script>
