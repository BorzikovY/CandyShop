<template>

  <v-container class="rounded-circle position-fixed bg-white cartCircle cursor-pointer">
    <v-img sizes="48px" :src="cart" style="z-index: 11"  />
  </v-container>

</template>

<script setup>
import cart from "../../public/cart.svg"
</script>

<style lang="scss" scoped>

.cartCircle{
  box-shadow: 0 1px 2px 0 rgba(50,50,50,0.15);
  width: 50px;
  height: 50px;
  z-index: 10;
  bottom: 15px;
  right: 15px;

}

</style>
