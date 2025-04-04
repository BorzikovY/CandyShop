<template>
  <CustomCart @click="dialog = true"/>

  <v-dialog
      v-model="dialog"
      width="auto"
    >
      <v-card
        max-width="400"
        prepend-icon="mdi-update"
        text="Your application will relaunch automatically after the update is complete."
        title="Update in progress"
      >
        <template v-slot:actions>
          <v-btn
            class="ms-auto"
            text="Ok"
            @click="dialog = false"
          ></v-btn>
        </template>
      </v-card>
    </v-dialog>
</template>

<script setup>
import CustomCart from "@/components/CustomCart.vue";
import { ref } from "vue"
const dialog = ref(false)

</script>

<style lang="scss" scoped>

</style>
