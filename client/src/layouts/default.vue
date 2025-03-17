<template>
  <div class="absolute">
    <div class="container">
      <CustomHeader/>
      <v-main class="customPadding">
        <router-view />
      </v-main>
    </div>
  </div>



</template>

<script setup>
import CustomHeader from "@/components/CustomHeader.vue"

</script>

<style lang="scss" scoped>

.absolute{
  display: flex;
  justify-content: center;
}
.container{
  max-width: 2200px;
  width: 100%;
  border-left: 1px solid #E9E9E9;
  border-right: 1px solid #E9E9E9;
}

.customPadding{
  margin-top: 45px;
  margin-bottom: 25px;
}
</style>
