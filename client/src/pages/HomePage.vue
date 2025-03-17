<template>
  <v-card
    color="basil"
    style="margin: 20px auto 0; border: none;"
    width="70vw"
    flat>

    <v-card-title class="text-center justify-center py-6">
      <h1 class="font-weight-bold text-h2 text-basil">
        CandyShop
      </h1>
    </v-card-title>

    <v-tabs
      v-model="tab"
      bg-color="transparent"
      color="basil"
      style="margin-top: 40px"
      grow
    >
      <v-tab
        v-for="item in ['Конфетки', 'Гарантии', 'О создателях']"
        :key="item"
        :text="item"
        :value="item"
      ></v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item
        v-for="item in items"
        :key="item"
        :value="item"
      >
        <v-card
          color="basil"
          flat
        >
          <v-card-text>{{ text }}</v-card-text>
        </v-card>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>

  <v-carousel hide-delimiters height="700px">
    <v-carousel-item
      src="https://www.americangrocer.co.uk/cdn/shop/collections/AG___Collections___-49.jpg?v=1595459036"
      cover
    ></v-carousel-item>

    <v-carousel-item
      src="https://gettyimagesgallery.com/wp-content/uploads/2020/03/GettyImages-536975153.jpg"
      cover
    ></v-carousel-item>

    <v-carousel-item
      src="https://www.zastavki.com/pictures/originals/2014/Creative_Wallpaper_Colorful_candys_075920_.jpg"
      cover
    ></v-carousel-item>
  </v-carousel>

</template>

<script>

</script>

<style lang="scss" scoped>

</style>
