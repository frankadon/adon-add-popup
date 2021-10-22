<template>
    <div>
        <h3>Data</h3>
        <div v-for="card in cards" :key="card.id">
            {{card.title}}
            <img :src="path+card.image" alt="" style="width: 100px;">
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "Cards",
    data(){
        return {
            cards: [],
            path: 'http://localhost:8000'
        }
    },
    async created() {
        this.getCards()
    },
    methods: {
        async getCards(){
            axios.get('/api/v1/cards', {
                headers: {
                    'content-Type': 'application/json',
                    'Authorization': this.$store.state.access
                }
            })
            .then(response => {
                console.log(response)
                this.cards = response.data
            })
        }
    }
}
</script>

<style>

</style>