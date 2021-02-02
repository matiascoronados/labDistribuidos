<template>
    <b-table :data="data" :columns="columns" bordered striped hoverable focusable></b-table>
</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
                apiData:[],
                titles: [],
                topic_titles:[],
                authors:[],
                numcomments:[],
                scores:[],
                stats:[],
                comments:[],
                data: [],
                columns: [
                    {
                        field: 'topic_title',
                        label: 'Topico',
                    
                    },
                    {
                        field: 'post_title',
                        label: 'Post',
                    },
                    {
                        field: 'post_author',
                        label: 'Autor',
                    },
                   
                    {
                        field: 'comment',
                        label: 'Comentario',
                        centered:true
                    }
                ]
            }
        },
        methods:{
            getData(){
                const url = 'http://localhost:3000/getCommentStats'
                axios.get(url).then(response=>{
                    this.apiData = response.data["rows"]

                    console.log( this.apiData)
                    

                    this.apiData.forEach(element=>{
                        this.topic_titles.push(element["topic_title"])
                        this.titles.push(element["post_title"])
                        this.authors.push(element["post_author"])
                        this.numcomments.push(element["post_numcomments"])
                        this.scores.push(element["post_score"])
                        this.comments.push(element["comment_body"])
                        this.stats.push([
                                element["uppercase"],
                                element["lowercase"],
                                element["vocals"],
                                element["consonants"],
                                element["words"],
                                element["stopwords"]
                            ])
                            
                            
                    })
                    console.log(this.comments) 
                    this.setTableData()

                })
            },
            setTableData(){
                for(var i =0; i<this.apiData.length;i++){
                    this.data.push({
                        'topic_title':this.titles[i],
                        'post_title':this.topic_titles[i],
                        'post_author':this.authors[i],
                        'score':this.scores[i],
                        'comment':this.comments[i]
                    })
                }
            }
        },
        mounted(){
            this.getData()
        }

    }
</script>