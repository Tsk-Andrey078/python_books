<template>
  <div class="card">
    <table class="table">
      <thead>
        <tr>
          <th>Column</th>
          <th>Is Visible</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <td>{{ item.column_name }}</td>
          <td>
            <input type="checkbox" v-model="item.is_visible" @change="updateStatus(item)">
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],
            base_url: "http://127.0.0.1:8001"
        }
    },
    mounted() {
        this.get_data()

        
    },
    methods: {
        async get_data() {
          await axios.get(`${this.base_url}/api/settings/`).then((response) => {
            this.items = response.data
          })
          console.log(this.items)
        },
        async updateStatus(item) {
          await axios.put(`${this.base_url}/api/settings/`, item).then((response) => {
            console.log(response)
          }).catch ((error) => {
            console.log(error)
          })
        }
    }
}
</script>

<style>
</style>
