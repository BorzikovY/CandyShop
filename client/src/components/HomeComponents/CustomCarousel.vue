

<template>
  <v-carousel
    hide-delimiters
    height="700px"
  >
    <v-carousel-item
      v-for="item in arrayOfImages"
      :src="item.imgURL"
      cover
    />

  </v-carousel>
</template>

<script setup>

defineProps({
  arrayOfImages: Array,
})



</script>

<style lang="scss" scoped>

</style>
