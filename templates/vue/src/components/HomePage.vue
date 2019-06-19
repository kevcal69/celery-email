<template>
	 <a-card title="Send Email" class="email">
		<EmailForm />
	</a-card>
</template>

<script>
export default {
	name: 'HomePage',
	components: {
		EmailForm: require('components/EmailForm.vue').default,
		EmailList: require('components/EmailList.vue').default
	}
};
</script>

<style scoped>
.email {
	width: 100%;
	max-width: 80rem;
	height: 500px;
}
</style>