<template>

  <CustomEnterPanel/>

  <CustomCarousel :arrayOfImages="HomeCarouselArray"/>

  <h1 class="text-h2 pb-9 pt-9 w-100 text-center">Смотри продукты</h1>
  <GoodsSlider :goods="goods"/>


  <h1 class="py-8 text-h4 w-100 text-center"> Отвечают за базар</h1>
  <CustomUserComment :comments="commentArray"/>


</template>

<script setup>
//Components
import CustomCarousel from "@/components/HomeComponents/CustomCarousel.vue"
import GoodsSlider from "@/components/HomeComponents/GoodsSlider.vue"
import CustomEnterPanel from "@/components/HomeComponents/CustomEnterPanel.vue";
import CustomUserComment from "@/components/HomeComponents/CustomUserComment.vue";


// TestArrays
import { HomeCarouselArray } from "@/components/testsArray/HomeCarouselArray.vue";
import { goods } from "@/components/testsArray/GoodsTestArray.vue";
import { commentArray } from "@/components/testsArray/CommentsArray.vue";


</script>


<style scoped>

</style>

