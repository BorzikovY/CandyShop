
import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
  state: () => {
    return {
      cartData: Array,
      goodsData: Array,
      error: null,
      isLoading: false
    }
  },

 actions: {

 }
})
