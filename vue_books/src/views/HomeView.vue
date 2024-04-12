<template>
    <div class="card">
        <div class="card-body">
            <table class="table table-striped">
                <thead>
                <tr>
                    <th v-for="header in posts[0]"><div v-if="header != 'id'">{{ header }}</div></th>
                    <button style="margin: 5px;" data-bs-toggle="modal" data-bs-target="#exampleModal2" class="btn btn-success">Add new book</button>
                </tr>
                
                </thead>
                <tbody >
                <tr v-for="post in posts[1]" :key="post.id">
                    <td v-for="item in post">{{ item }}</td>
                    <td><button class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#exampleModal" @click="get_more_data(post.id_b)">Show</button></td>
                    <td><button class="btn btn-danger" @click="delete_book(post.id_b)">Delete</button></td>
                    <td><button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#exampleModal3" @click="update_book(post.id_b)">Update</button></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>

    
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">{{ data.name }}</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Title - {{ data.title }}</h1>
                <h3 class="modal-title fs-5" id="exampleModalLabel">Author - {{ data.author }}</h3>
                <p>Description - {{ data.description }}</p>
                <h4 class="modal-title fs-5" id="exampleModalLabel">Price - {{ data.price }}</h4>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="exampleModal2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <form id="myForm">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Add new book</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">id_b</label>
                            <input type="text" class="form-control" id="input_id_b" name="id_b">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">name</label>
                            <input type="text" class="form-control" id="input_name" name="name">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">title</label>
                            <input type="text" class="form-control" id="input_title" name="title">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">author</label>
                            <input type="text" class="form-control" id="input_author" name="author">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">description</label>
                            <input type="text" class="form-control" id="input_description" name="description">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">price</label>
                            <input type="text" class="form-control" id="input_price" name="price">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Add</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <div class="modal fade" id="exampleModal3" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <form id="myForm2">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Update the Book</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">id_b: {{post_update.id_b}}</label>
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">name</label>
                            <input type="text" class="form-control" id="input_name" name="name" v-model="post_update.name">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">title</label>
                            <input type="text" class="form-control" id="input_title" name="title" v-model="post_update.title">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">author</label>
                            <input type="text" class="form-control" id="input_author" name="author" v-model="post_update.author">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">description</label>
                            <input type="text" class="form-control" id="input_description" name="description" v-model="post_update.description">
                        </div>
                        <div class="mb-3">
                            <label for="inputField1" class="form-label">price</label>
                            <input type="text" class="form-control" id="input_price" name="price" v-model="post_update.price">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Add</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<style>

</style>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: [],
            data: [],
            id_b_update: 0,
            base_url: "http://127.0.0.1:8001",
            post_update: []
        }
    },
    mounted() {
        this.get_data()

        const form = document.getElementById('myForm')

        form.addEventListener('submit', async function(event) {
            event.preventDefault()
            const formData = new FormData(form)
            try {
                await axios.post(`${this.base_url}/api/book/`, formData).then((response) => {
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                })
            } catch (error) {
                console.log(error)
            }
        })
    },
    methods: {
        async get_data() {
            let posts = await axios(`${this.base_url}/api/get_books/`)
            this.posts = posts.data
            console.log(this.posts)
        },
        async get_more_data(id) {
            await axios.get(`${this.base_url}/api/book/${id}/`).then((response) => {
                this.data = response.data
            }).catch ((err) => {
                console.log(err)
            })
            console.log(this.data)
        },
        async delete_book(id) {
            await axios.delete(`${this.base_url}/api/book/${id}/`).then((response) => {
                console.log(response)
            }).catch((error) => {
                console.log(error)
            })
        },
        async update_book(id_b) {
            await axios(`${this.base_url}/api/book/${id_b}/`).then((response) => {
                this.post_update = response.data
            }).catch((err) => {
                console.log(error)
            })
            
            console.log(this.post_update)
            const form = document.getElementById('myForm2')

            form.addEventListener('submit', async function(event) {
                event.preventDefault()
                const formData = new FormData(form)
                try {
                    await axios.put(`${this.base_url}/api/book/${id_b}/`, formData).then((response) => {
                        console.log(response)
                    }).catch((error) => {
                        console.log(error)
                    })
                } catch (error) {
                    console.log(error)
                }
            })
        }
    }
}

</script>