<template>
  <v-container fluid style="display: grid; justify-content: center">
    <v-row
      class="d-flex flex-nowrap overflow-x-auto px-6 pb-6"
      style="width: 90vw; max-width: 1600px"
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
          height="450"
          max-height="450"
        >
          <v-img
            height="200"
            :src="good.imgURL"

            cover
          >
            <div class="image-overlay"></div>
            <v-toolbar color="transparent" class="overlay-text">
              <v-toolbar-title class="text-h5 text-white">
                {{ good.name }}
              </v-toolbar-title>
            </v-toolbar>
          </v-img>

          <v-card-text>
            <div class="font-weight-bold mb-2">
              Описание
            </div>
            <p style="height: 140px; display: flex; text-wrap: wrap">
              {{ good.description }}
            </p>

          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
defineProps({
  goods: Array
})
</script>

<style lang="scss" scoped>
.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1;
}

.overlay-text {
  position: relative;
  z-index: 2;
}
</style>
