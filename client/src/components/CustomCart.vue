<template>
  <v-menu offset-y bottom right>
    <template v-slot:activator="{ on, attrs }">
      <v-container
        v-bind="attrs"
        v-on="on"
        class="rounded-circle position-fixed bg-white cartCircle cursor-pointer"
      >
        <v-img
          sizes="48px"
          :src="cart"
          @click="dialog = true"
          style="z-index: 11"
        />
      </v-container>
    </template>
  </v-menu>

    <v-dialog v-model="dialog" class="d-flex justify-center align-center justify-center" persistent>
    <v-card class="d-flex justify-center align-center" max-width="800px">
      <v-card-title>Корзина</v-card-title>
      <v-card-text style="width: 100%;">
        <v-list>
          <v-container
            v-for="product in products"
            :key="product.id"
          class="d-flex flex-nowrap align-center" style="width: 100%;">
            <v-container class="d-flex flex-wrap flex-column">
              <p style="font-size: 17px">{{ product.name }}</p>
              <p style="font-size: 14px">{{ product.price }}/1гр</p>
            </v-container>
            <v-container class="align-center">
              <v-text-field placeholder="Сколько грамм?"/>
            </v-container>
          </v-container>
        </v-list>
      </v-card-text>
      <template v-slot:actions>
        <v-btn text @click="dialog = false">Закрыть</v-btn>
      </template>
    </v-card>
  </v-dialog>

</template>

<script setup>
import { ref } from 'vue';
import cart from '../../public/cart.svg';
import { products } from "@/components/testsArray/CartArray.vue";

const dialog = ref(false);
</script>

<style lang="scss" scoped>
.cartCircle {
  box-shadow: 0 1px 2px 0 rgba(50,50,50,0.15);
  width: 50px;
  height: 50px;
  z-index: 10;
  bottom: 15px;
  right: 15px;
}
</style>
