<template>
  <v-card elevation="4" class="d-flex flex-wrap flex-column pa-0 rounded"  style="height: 460px; width: 300px;">
    <v-img :src="creatorData.imgURL" class="w-100 pa-0 rounded-t" style="height: 210px; max-height: 210px" cover/>
    <v-container class="d-flex ga-1 flex-wrap pa-4">
      <v-card-text class="pa-1">{{ creatorData.fullName }}</v-card-text>
      <v-card-text class="pa-1">{{ creatorData.job }}</v-card-text>
      <v-card-text class="pa-1">{{ creatorData.bio }}</v-card-text>
    </v-container>
  </v-card>
</template>

<script setup>

defineProps({
  creatorData: Array
})

</script>

<style lang="scss" scoped>

</style>
