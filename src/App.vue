<template>
  <div id="app">

    <form @submit.prevent="new_tweet">
      <div class="form-group-row">
            <table class="table">
        <thead>
            <th>  <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="tweet.name"></th>
            <th>  <input type="text" class="form-control col-3 mx-2" placeholder="Content" v-model="tweet.content"></th>
            <th>  <button class="btn btn-sucess">Tweet!</button></th>
        </thead>
        </table>
      </div>
    </form>

    <table class="table">
        <thead>
            <th>  </th>
            <th>  </th>
            <th>  </th>
        </thead>
        <tbody>
            <tr v-for="tweet in tweets" v-bind:key="tweet.id">
                <td> {{ tweet.creation_time }} </td>
                <td> {{ tweet.name }} </td>
                <td> {{ tweet.content }} </td>
            </tr>
        </tbody>
    </table>
  </div>

</template>

<script>
import axios from "axios"

export default {
  name: 'App',
    data(){
    return {
        tweet: {
            'name': '',
            'content': ''
        },
        tweets: []
    }
    },
    async created(){
        await this.fetch_tweets();
    },

    methods: {
        async fetch_tweets(){
            var response = await axios.get("http://127.0.0.1:8000/");
            this.tweets = await response.data;
        },
        async new_tweet(){
            let info = {
                name: this.tweet.name,
                content: this.tweet.content
            };
            await axios.post("http://127.0.0.1:8000/", info);

            await this.fetch_tweets();
        }
    }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
