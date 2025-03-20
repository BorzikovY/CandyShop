<template>
  <CustomEnterPanel :isNameAndLogo=false />

  <v-container>

    <v-card-text class="text-h4 text-blue-accent-4">
      Наша команда
    </v-card-text>
    <v-card-text class="text-h6">
      Самые лучшие два программиста. Команда маленькая, да удаленькая!
    </v-card-text>
    <v-container class="d-flex ga-6">
      <CustomCreator v-for="creator in creators" :creatorData="creator"/>
    </v-container>
  </v-container>

<!--  TODO Добавить предкпреждение-->

</template>

<script setup>
import CustomCreator from "@/components/AboutUsComponents/CustomCreator.vue";
import CustomEnterPanel from "@/components/CustomEnterPanel.vue";
import { useCreators }  from "@/components/testsArray/CreatorsArray.vue";

const creators = useCreators

</script>

<style lang="scss" scoped>

</style>
