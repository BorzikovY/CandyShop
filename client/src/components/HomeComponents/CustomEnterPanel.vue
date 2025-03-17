<template>
  <v-card
    color="basil"
    flat
    width="70vw"
    class="mx-auto mt-6"
  >
    <v-card-title
      class="justify-center py-16 pb-16"
      style="display: flex; justify-content: center;"
    >
      <div class="w-100 align-center justify-center d-flex">
        <v-img :src="logo" width="140" max-width="140px" height="140"/>
        <h1
          class="font-weight-bold text-h2 text-basil ">
          CandyShop
        </h1>
      </div>

    </v-card-title>

    <v-tabs
      height="85px"
я      bg-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        height="88px"
        v-for="item in pagesArray"
        :key="item.id"
        :value="item.name"
        :to="item.to"
      >
        {{ item.name }}
      </v-tab>
    </v-tabs>
  </v-card>
</template>

<script setup>
import logo from "../../../public/logo.svg";


const pagesArray = [
  {
    id: 1,
    to: "/",
    name: "Конфетки"
  },
  {
    id: 2,
    to: "/guarantees",
    name: "Гарантии"
  },
  {
    id: 3,
    to: "/about",
    name: "О создателях"
  },
]

</script>

<style lang="scss" scoped>

</style>
