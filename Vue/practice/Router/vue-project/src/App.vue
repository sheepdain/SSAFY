<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink> | 
      <RouterLink to="/about">About</RouterLink> | 
      <RouterLink to="/board">Board</RouterLink> | 
      <RouterLink :to="{ name: 'detail', params: {id:'1'}}">1번페이지</RouterLink> | 
      <RouterLink :to="{ name: 'detail', params: {id:'2'}}">2번페이지</RouterLink> | 
      <RouterLink :to="{ name: 'login'}">Login</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
