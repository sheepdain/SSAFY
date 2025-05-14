<template>
  <h1>여기는 {{ num }}번 글의 상세 페이지입니다.</h1>

  <RouterLink :to="{name: 'over-thirty'}">30세 이상</RouterLink>
  <hr>
  <RouterLink :to="{name: 'under-thirty'}">30세 미만</RouterLink>
  <hr>
  <RouterView/>
</template>

<script setup>
import {ref, watch} from "vue"
import {useRoute} from "vue-router"

const route=useRoute()
const num=ref(route.params.id)

watch(()=>route.params.id, (newId)=>{
  num.value=newId
})
</script>