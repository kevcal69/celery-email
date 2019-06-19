<template>
    <div class="wrapper">
        <div class="content">
            <div class="title" @click="goTo($event, '/')">Email App</div>

            <div class="button">
                <a-icon type="mail" /> Try it!
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'the-header',
    methods: {
        goTo(e, loc) {
            this.$router.push(loc);
        }
    }
};
</script>

<style scoped="true">
.wrapper {
    padding: 15px 0px;
    border: 1px solid #dedede;
}
.wrapper .content {
    width: 90vw;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    font-family: 'Open Sans Condensed', sans-serif;
}
.wrapper .title {
    font-size: 25px;
    cursor: pointer;
}
.wrapper .content .button {
    font-family: 'Roboto Mono', monospace;
}
.wrapper .content .button a {
    text-decoration: none;
    color: #fff;
}
</style>