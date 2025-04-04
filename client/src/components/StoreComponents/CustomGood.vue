<template>
  <v-card
    class="mx-auto d-flex flex-column"
    max-width="340"
  >
    <v-img
      class="align-end text-white"
      height="200"
      :src="currentGood.imgURL"
      cover
    >
      <v-card-title>{{ currentGood.name }}</v-card-title>
    </v-img>
     <v-card-text>{{ currentGood.description }}</v-card-text>

    <v-card-actions class="d-flex justify-space-between w-100 pa-3 align-self-end">
      <v-btn style="color:#836398" text="Купить"></v-btn>

      <p style="color:#836398; width: fit-content" text="Explore">{{ currentGood.price }} &#8381;</p>
    </v-card-actions>
  </v-card>
</template>

<script setup>

import axios from "axios";


import CustomCart from "@/components/CustomCart.vue";

defineProps({
  currentGood: Array
})


</script>

<style lang="scss" scoped>

</style>
