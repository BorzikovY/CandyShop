<template>
    <div class="container">
      <v-main>
        <router-view />
      </v-main>
    </div>

</template>

<script setup>

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


</style>
