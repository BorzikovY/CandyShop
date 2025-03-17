<template>
  <v-card
    color="basil"
    flat
    width="70vw"
    class="mx-auto mt-6"
  >
    <v-card-title
      class="text-center justify-center py-16 pb-16"
    >
      <h1
        class="font-weight-bold text-h2 text-basil"
      >
        CandyShop
      </h1>
    </v-card-title>

    <v-tabs
      height="85px"
      v-model="tab"
      bg-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        height="88px"
        v-for="item in ['Конфетки', 'Гарантии', 'О создателях']"
        :key="item"
        :value="item"
      >
        {{ item }}
      </v-tab>
    </v-tabs>
  </v-card>

  <v-carousel
    hide-delimiters
    height="700px"
  >
    <v-carousel-item
      src="https://www.americangrocer.co.uk/cdn/shop/collections/AG___Collections___-49.jpg?v=1595459036"
      cover
    />

    <v-carousel-item
      src="https://gettyimagesgallery.com/wp-content/uploads/2020/03/GettyImages-536975153.jpg"
      cover
    />

    <v-carousel-item
      src="https://www.zastavki.com/pictures/originals/2014/Creative_Wallpaper_Colorful_candys_075920_.jpg"
      cover
    />
  </v-carousel>

  <v-row
    justify="center"
    class="mt-10"
  >
    <v-col
      cols="12"
      class="text-center"
    >
      <h1
        class="text-h3 pb-9 pt-3"
      >
        Наши продукты
      </h1>
    </v-col>
  </v-row>

  <v-container
    fluid
  >
    <v-row
      class="d-flex flex-nowrap overflow-x-auto px-6 pb-6 row-nowrap hide-scrollbar"
      align="start"
    >
      <v-col
        cols="auto"
        v-for="good in goods"
        :key="good.id"
        class="px-2"
      >
        <v-card
          max-width="300"
          min-width="300"
          height="400"
          max-height="400"
        >
          <v-img
            color="surface-variant"
            height="200"
            :src="good.imgURL"
            cover
          >
            <v-toolbar
              color="transparent"
            >
              <v-toolbar-title
                class="text-h5"
              >
                {{ good.name }}
              </v-toolbar-title>
            </v-toolbar>
          </v-img>

          <v-card-text>
            <div
              class="font-weight-bold mb-2"
            >
              Описание
            </div>
            <p style="height: 100px; display: flex; text-wrap: wrap">
              {{ good.description }}
            </p>
            <v-btn
              color="primary"
              class="mt-2"
            >
              КУПИТЬ
            </v-btn>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from "vue"

const tab = ref("Конфетки")

const goods = ref([
  {
    id: 1,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
  {
    id: 2,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
  {
    id: 3,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
  {
    id: 4,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
  {
    id: 5,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
  {
    id: 6,
    name: "Шоколадка",
    imgURL:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F24tv.ua%2Fresources%2Fphotos%2Fnews%2F202411%2F2691670.jpg%3Fv%3D1732273528000&f=1&nofb=1",
    description:
      "Самая вкусная, неописуемо приятная, а так же содержит столько какао бобов, что накрывает не по-детски... Просто посмотрите вкус",
  },
])
</script>

<style scoped>
.row-nowrap {
  white-space: nowrap;
}

.hide-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.hide-scrollbar::-webkit-scrollbar {
  display: none;
}
</style>

