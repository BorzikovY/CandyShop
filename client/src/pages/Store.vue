<template>
  <CustomEnterPanel :isNameAndLogo=false />
  <StoreModal/>
  <v-container class="d-flex flex-wrap ga-4" max-width="1200px">
    <CustomGood v-for="good in goods" :currentGood="good" :key="good.id"/>
  </v-container>
</template>

<script setup>

import CustomEnterPanel from "@/components/CustomEnterPanel.vue";
import { goods } from "@/components/testsArray/GoodsTestArray.vue";
import CustomGood from "@/components/StoreComponents/CustomGood.vue";
import { ref } from 'vue'
import StoreModal from "@/components/StoreModal/StoreModal.vue";

</script>

<style lang="scss" scoped>

</style>
