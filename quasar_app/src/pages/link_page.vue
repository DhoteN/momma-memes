<template>
  <q-page>

      <div class="row q-pa-sm">
        <div class="col-12">
          <q-img style="border-radius: 5px" :src="selected_type_data.icon" width="10%" class="float-left q-mr-lg"/>
          <div class="text-weight-bold q-mt-lg">{{ selected_type_data.label }}</div>
          <div class="q-pb-lg">{{ selected_type_data.description }}</div>
          <div class="q-mt-sm">
            <q-tabs
            v-model="tab"
            dense
            :class="$q.dark.isActive ? 'text-white' : 'text-black'"
            :active-color="$q.dark.isActive ? 'secondary':'primary'"
            indicator-color="$q.dark.isActive ? 'secondary':'primary'"
            align="left"
            narrow-indicator
          >
            <q-tab name="hot" label="Hot" />
            <q-tab name="fresh" label="Fresh" />
          </q-tabs>

          <q-separator />
          <q-tab-panels v-model="tab" animated>
            <q-tab-panel class="q-px-none" name="hot">
              <div class="q-pt-sm">
                <q-chip v-for="tag in selected_type_data.tags" :label="tag"/>
              </div>
              <div class="row">
                <div class="col-6">
                  <q-list>
                    <q-item :class="index==0 ? '' : 'q-mt-md'" v-for="item,index in hot_options">
                      <q-item-section>
                        <q-item-label caption>
                            <q-icon name="font_download" size="sm"/>  {{item.caption}}  - 2h</q-item-label>
                        <q-item-label header class="text-weight-bold q-pl-none q-pt-none" :class="$q.dark.isActive ? 'text-white' : 'text-black'" > {{item.header}}</q-item-label>
                        <img class="q-ml-xl" :src="item.icon">
                        <q-media-player
                          class="q-ml-xl"
                          type="video"
                          :sources="item.sources"
                          :poster="item.poster"
                        v-if="item.sources"
                        />
                      </q-item-section>
                    </q-item>
                  </q-list>
                </div>
                <div class="col-3"></div>
                </div>
<!--              <div class="text-h6">Mails</div>-->
<!--              Lorem ipsum dolor sit amet consectetur adipisicing elit.-->
            </q-tab-panel>

          </q-tab-panels>
          </div>

          </div>
      </div>
      <div class="row">
        <div class="col-6">
          <q-list>
            <q-item v-for="item in hot_options">
              <q-item-section>
                <q-item-label caption>
                    <q-icon name="font_download" size="sm"/>  {{item.caption}}  - 2h</q-item-label>
                <q-item-label header class="text-weight-bold q-pl-none q-pt-none" :class="$q.dark.isActive ? 'text-white' : 'text-black'"> {{item.header}}</q-item-label>
                <img :src="item.icon">
                <q-media-player
                  type="video"
                  :sources="item.sources"
                  :poster="item.poster"
                v-if="item.sources"
                />
              </q-item-section>
            </q-item>
          </q-list>
        </div>
                <div class="col-3"></div>

        </div>

  </q-page>
</template>

<script>
export default {
    name: 'PageIndex',
    data() {
        return {
            tab: 'hot',
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
                ],
                sections:[],
            selected_type_data:{},
            hot_options: [
                    {
                        'caption': 'Funny',
                        'header': 'Who remembers being a Pirate like this?',
                        'icon': 'statics/images/how_old_areyou.webp',
                    },
                    {
                        'caption': 'Funny',
                        'header': 'Maybe India',
                        'icon': 'statics/images/maybe_india.webp',
                    },
                    {
                        'caption': 'Awesome',
                        'header': 'Working at a paint store would be so much fun',
                        'poster': 'statics/images/paint_store.mp4',
                        'sources':[
                          {
                            src: 'statics/images/paint_store.mp4',
                            type: 'video/mp4'
                          }
                        ]
                    },
                    {
                        'caption': 'Awesome',
                        'header': 'Thats a clean one',
                        'sources':[
                          {
                            src: 'statics/images/clean_pc.mp4',
                            type: 'video/mp4'
                          }
                        ]
                    },

                ]
        }
    },
    watch:{
        '$route':function () {
            let self=this;

                self.selected_type_data = self.popular.filter(function (item) {
                                      return item.value.toLowerCase() == self.$route.params.page_type.toLowerCase();
                                  })[0]

        }
    },
    // created(){
    //     let self = this;
    //     self.selected_type_data = self.popular.filter(function (item) {
    //                                   return item.label.toLowerCase() == self.$route.params.page_type.toLowerCase();
    //                               })[0]
    // },
    methods:{
        // get_filtered_data:function (type) {
        //     let self=this;
        //     return this.popular.filter(function (item) {
        //         return item.label == type
        //     })[0]
        // }
    }
}
</script>
