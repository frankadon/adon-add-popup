<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
            <label for="">Username: </label>
            <input type="email" name="username" v-model="username"><br><br>
            <label for="">Password: </label>
            <input type="password" name="password" v-model="password"><br><br>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "Login",
    data(){
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        submitForm(){
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('access')

            const formData = {
                username: this.username,
                password: this.password
            }
            axios.post('/api/v1/jwt/create/', formData)
            .then(response => {
                console.log(response)
                const access = response.data.access
                const refresh = response.data.refresh
                this.$store.commit('setAccess', access)
                this.$store.commit('setRefreshToken', refresh)
                axios.defaults.headers.common['Authorization'] = "JWT " + access
                localStorage.setItem('access', access)
                localStorage.setItem('refresh', refresh)
                this.$router.push('/')
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style>

</style>