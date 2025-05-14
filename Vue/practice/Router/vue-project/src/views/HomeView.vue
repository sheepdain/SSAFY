<template>
  <h1>Home</h1>
  <button @click="goToBoardRoute">게시판으로 가자</button>
</template>

<script setup>
import {useRouter} from 'vue-router'

const router=useRouter()

function goToBoardRoute() {
  router.push({name: "board"})
}
</script>