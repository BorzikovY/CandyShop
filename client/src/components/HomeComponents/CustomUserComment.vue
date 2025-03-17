<template>
  <v-container fluid>
    <v-row class="d-flex justify-center ga-9"  dense>
      <v-col

        v-for="comment in comments"
        :key="comment.id"
        cols="12"
        md="5"
      >
        <v-card class="w-100" height="400">
          <v-card-text>
            <p class="w-100 text-end">{{ comment.date || "04/06/2004" }}</p>
            <p class="text-h4 mb-2 font-weight-black">
              {{ comment.author || "Анонимус Темный" }}
            </p>

            <v-rating
              readonly
              :length="5"
              :size="32"
              :model-value="comment.rating || 3.5"
              active-color="primary"
              class="mb-2"
            />

            <div class="text-medium-emphasis text-h6">
              {{ catComment(comment.comment) }}
            </div>
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="teal-accent-4"
              variant="text"
              @click="toggleReveal(comment.id, true)"
            >
              Прочитать полностью
            </v-btn>
          </v-card-actions>

          <v-expand-transition>
            <v-card
              v-if="reveals[comment.id]"
              class="position-absolute w-100"
              height="100%"
              style="bottom: 0;"
            >
              <v-card-text class="pb-0">
                <p class="text-medium-emphasis">
                  {{ comment.comment }}
                </p>
              </v-card-text>

              <v-card-actions class="pt-0">
                <v-btn
                  color="teal-accent-4"
                  variant="text"
                  @click="toggleReveal(comment.id, false)"
                >
                  Close
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  comments: {
    type: Array,
    default: () => [],
  }
});

const reveals = ref({});

function toggleReveal(id, value) {
  reveals.value[id] = value;
}

function catComment(comment) {
  if (comment.length > 150) {
    return comment.slice(0, 150) + '....';
  }
  return comment;
}
</script>

<style scoped>

</style>
