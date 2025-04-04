<template>
  <!-- При клике на CustomCart открываем модалку -->
  <CustomCart @click="dialog = true" />

  <v-dialog v-model="dialog" width="auto">
    <v-card
      prepend-icon="mdi-update"
      text="Your application will relaunch automatically after the update is complete."
      title="Update in progress"
    >

    </v-card>
  </v-dialog>
</template>

<script setup>
import CustomCart from "@/components/CustomCart.vue";
import { ref } from "vue";
import { products } from "@/components/testsArray/CartArray.vue";

const dialog = ref(false);
</script>

<style scoped lang="scss">
/* Добавьте стили по необходимости */
</style>
