<template>
    <div>
        <h1>Sign up</h1>
        <form @submit.prevent="submitForm">
            <label for="">Username: </label>
            <input type="email" name="username" v-model="username"><br><br>
            <label for="">Password: </label>
            <input type="password" name="password" v-model="password"><br><br>
            <button type="submit">Sign up</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
// import axios from 'axios'
export default {
    name: "SignUp",
    data(){
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        submitForm(){
            const formData = {
                username: this.username,
                password: this.password
            }
            axios
                .post('/api/v1/users/', formData)
                .then(response => {
                    console.log(response)
                    this.$router.push('/login')
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