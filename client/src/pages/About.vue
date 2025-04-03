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
    <v-divider></v-divider>
    <v-container class="d-flex flex-wrap ga-5 mt-13">
      <v-card-title class="text-h3 text-center w-100 text-red">
        Предупреждение

      </v-card-title>
      <v-card-text class="text-h5">

        Данный сайт создан исключительно в развлекательных и юмористических целях.
        Все материалы, представленные здесь, являются вымышленными и не имеют отношения к
        реальной продаже конфет или любым незаконным веществам. Сайт не пропагандирует употребление
        наркотиков и не несёт за собой какой-либо негативный подтекст. Если вы воспринимаете представленный
        контент буквально, просим относиться к нему с долей юмора.

      </v-card-text>
    </v-container>
  </v-container>

<!--  TODO Добавить предуреждение, что это шуточный проект -->

</template>

<script setup>
import CustomCreator from "@/components/AboutUsComponents/CustomCreator.vue";
import CustomEnterPanel from "@/components/CustomEnterPanel.vue";
import { useCreators }  from "@/components/testsArray/CreatorsArray.vue";

const creators = useCreators

</script>

<style lang="scss" scoped>

</style>
