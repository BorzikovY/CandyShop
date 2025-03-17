<template>
  <div class="wrapper">
    <div class="wrapper__contactInfo">
      <v-icon icon="fa-solid fa-phone" size="13"></v-icon>
      <p>+8 (985) 456-3212</p>
    </div>
    <p class="wrapper__name">Лучший Сайт по продаже конфеток!</p>

    <p class="wrapper__cart">cart</p>
  </div>
</template>

<script>

</script>

<style lang="scss" scoped>
.wrapper {
  height: 45px;
  width: 100%;
  max-width: 2199px;
  background: #E9E9E9;
  font-size: 16px;
  display: flex;
  align-items: center;
  color: black;
  justify-content: space-between;
  position: fixed;
  top: 0;
  z-index: 10;
}

.wrapper__contactInfo {
  display: flex;
  gap: 10px;
  align-items: center;
  padding-left: 4vw;
}

.wrapper__name {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  white-space: nowrap;
  font-size: 20px;
}

.wrapper__cart {
  display: flex;
  padding-right: 5vw;
}

</style>
