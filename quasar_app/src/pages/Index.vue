<template>
  <q-page>
<!--    <div class="row">-->
<!--      <div class="col-12">-->
<!--      <q-carousel-->
<!--        v-model="slide"-->
<!--        transition-prev="scale"-->
<!--        transition-next="scale"-->
<!--        swipeable-->
<!--        animated-->
<!--        control-color="white"-->
<!--        navigation-->
<!--        padding-->
<!--        arrows-->
<!--        height="300px"-->
<!--        class="bg-primary text-white shadow-1 rounded-borders"-->
<!--      >-->
<!--        <q-carousel-slide name="style" class="column no-wrap flex-center">-->
<!--          <q-icon name="style" size="56px" />-->
<!--          <div class="q-mt-md text-center">-->
<!--            {{ lorem }}-->
<!--          </div>-->
<!--        </q-carousel-slide>-->
<!--        <q-carousel-slide name="tv" class="column no-wrap flex-center">-->
<!--          <q-icon name="live_tv" size="56px" />-->
<!--          <div class="q-mt-md text-center">-->
<!--            {{ lorem }}-->
<!--          </div>-->
<!--        </q-carousel-slide>-->
<!--        <q-carousel-slide name="layers" class="column no-wrap flex-center">-->
<!--          <q-icon name="layers" size="56px" />-->
<!--          <div class="q-mt-md text-center">-->
<!--            {{ lorem }}-->
<!--          </div>-->
<!--        </q-carousel-slide>-->
<!--        <q-carousel-slide name="map" class="column no-wrap flex-center">-->
<!--          <q-icon name="terrain" size="56px" />-->
<!--          <div class="q-mt-md text-center">-->
<!--            {{ lorem }}-->
<!--          </div>-->
<!--        </q-carousel-slide>-->
<!--      </q-carousel>-->
<!--        </div>-->
<!--    </div>-->
      <div class="row q-pa-sm">
        <div class="col-12">
          <q-chip label="Last of Us"/>
          <q-chip label="Corona virus"/>
          <q-chip label="Wuhan"/>
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
          slide: 'style',
          lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.',
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
          // new_options:[
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          // ],
          // trending_options:[
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          // ],
          // popular_options:[
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          //     {'caption':,'header', 'icon' },
          // ]
         // video: {
         //     label: 'Tears of Steel',
         //     poster: 'statics/media/TearsOfSteel/TearsOfSteel.jpeg',
         //     sources: [
         //         {
         //             src: 'statics/images/miss_jokes.mp4',
         //             type: 'video/mp4'
         //         }
         //     ],
         // }
      }
  }
}
</script>
