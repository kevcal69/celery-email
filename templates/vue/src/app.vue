<template>
    <div id="app" style="height: 100%">
        <TheHeader/>
        <div class="content">
            <div class="menu">
                <a-menu
                    style="width: 256px; height: 100%; position: relative;"
                >
                    <a-menu-item key="1">
                        <router-link :to="{ name: 'home'}">
                            <a-icon type="mail" />
                            <span>Send Mail</span>
                        </router-link>
                    </a-menu-item>
                    <a-menu-item key="2">
                        <router-link :to="{ name: 'queue'}">
                            <a-icon type="bars" />
                            <span>Email Queues</span>
                        </router-link>
                    </a-menu-item>
                </a-menu>
            </div>
            <div class='routes'>
                <router-view />
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'App',
    components: {
        TheHeader: require('components/TheHeader.vue').default
    }
};
</script>

<style scoped>
#app {
    display: flex;
    flex-direction: column;
}
.content {
    border-box: 100;
    height: 100%;
    width: 100%;
    display: flex;
}
.routes {
    min-height: 500px;
    width: 100%;
    display: flex;
    padding: 20px;
    justify-content: center;
}
</style>