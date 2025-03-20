<template>
  <v-card
    color="basil"
    flat
    width="90vw"
    max-width="1000px"
    class="mx-auto mt-1"
  >
  <v-container
  class="d-flex justify-space-between w-100"
  >
    <router-link
      class="text-h6 text-decoration-none text-black "
      v-for="item in pagesArray"
      :key="item.id"
      :to="item.to"
    ><p class="customAnimation">
      {{ item.name }}

    </p>
    </router-link>

  </v-container>

    <v-card-title
      v-if="isNameAndLogo"
      class="justify-center py-16 pb-16"
      style="display: flex; justify-content: center;"
    >
      <div class="w-100 align-center justify-center d-flex">
        <v-img :src="logo" width="140" max-width="140px" height="140"/>
        <h1
          class="font-weight-bold text-h2 text-basil" style="color: black">
          CandyShop
        </h1>
      </div>

    </v-card-title>
  </v-card>

</template>

<script setup>

defineProps({
  isNameAndLogo: Boolean
})

import logo from "../../public/logo.svg";



const pagesArray = [
  {
    id: 1,
    to: "/",
    name: "Главная"
  },
  {
    id: 2,
    to: "/store",
    name: "Магазин"
  },
  {
    id: 3,
    to: "/about",
    name: "О создателях"
  },
  {
    id: 4,
    to: "/guarantees",
    name: "Гарантии"
  }
]

</script>

<style lang="scss" scoped>

.customAnimation{

}:hover{
  color: #836398;
 }

</style>
