<template>
  <v-app>
      <HelloWorld/>
    </v-app>
  
</template>

<script>
import HelloWorld from './components/HelloWorld';
import vuetify from '@/plugins/vuetify'
import 'vuetify/dist/vuetify.min.css'
export default {
  name: 'App',
  vuetify,
  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped> 
  @import 'https://cdn.jsdelivr.net/npm/vuetify/dist/vuetify.min.css';
</style>
