<template>
    <b-navbar class="nav">
         <template #brand>
            <b-navbar-item tag="router-link" :to="{ path: '/' }">
                <img
                    src="https://miro.medium.com/max/720/1*mQz1eSo1ZkL-Rufb5Xfrqw.png"
                >
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item router-link href="/">
                Home
            </b-navbar-item>
            <b-navbar-item router-link href="/topics">
                Topicos
            </b-navbar-item>
            <b-navbar-item router-link href="/posts">
                Posts
            </b-navbar-item>
        </template>

        
    </b-navbar>
</template>
<style scoped>
.nav{
    border-bottom: 1px solid #EAEDED;
    margin-bottom:24px;
}
</style>