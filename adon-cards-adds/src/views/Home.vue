<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <h1>Home</h1>
    <span :src="user_data">{{ user_data }}</span>
    <Cards />
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Cards from '../components/Cards.vue'
export default {
  name: 'Home',
  data() {
    return {
      user_data: ''
    }
  },
  components: {
    Cards,
  },
  mounted() {
    this.getProfile()
  },
  methods: {
    getProfile(){
      axios.get('/api/v1/users/me')
      .then(response => {
        console.log(response)
        this.user_data = response.data.username
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
