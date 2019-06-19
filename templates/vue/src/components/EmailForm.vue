<template>
	<a-form
		class="form"
		:form="form"
		layout="horizontal"
		@submit="handleSubmit"
	>
	    <a-form-item
	      	label="From :"
	      	:label-col="{ span: 3 }"
	      	:wrapper-col="{ span: 16 }"
	    >
			<a-input
				v-decorator="[
				  'from_address',
				  {
				    rules: [{
				      type: 'email', message: 'The input is not valid E-mail!',
				    }, {
				      required: true, message: 'Please input your E-mail!',
				    }]
				  }
				]"
			/>
		</a-form-item>

	    <a-form-item
	      label="To :"
	      :label-col="{ span: 3 }"
	      :wrapper-col="{ span: 16 }"
	    >
			<a-select
				mode="tags"
				style="width: 100%"
				:tokenSeparators="[',']"
				v-decorator="[
				  'to_address',
				  {
				    rules: [{
				      type: 'array', required: true, message: 'The this field is required',
				    }, {
				      validator: validateToEmails,
				    }]
				  }
				]"
			/>
		</a-form-item>

	    <a-form-item
	      label="Subject :"
	      :label-col="{ span: 3 }"
	      :wrapper-col="{ span: 16 }"
	    >
			<a-input
				v-decorator="[
					'subject',
					{ rules: [{ required: true, message: 'This field is required!' }] }
					]"/>
		</a-form-item>

	    <a-form-item
	      label="Body :"
	      :label-col="{ span: 3 }"
	      :wrapper-col="{ span: 16 }"
	    >
			<a-textarea :rows="4"
				v-decorator="[
					'body',
					{ rules: [{ required: true, message: 'This field is required!' }] }
					]"/>
		</a-form-item>

		<a-form-item
	      :wrapper-col="{ span: 16, offset: 3 }"
	    >
			<a-button html-type="submit" type="primary">Submit</a-button>
		</a-form-item>
 	</a-form>
</template>

<script>
function validateEmail(email) {
	/*  from SO. `https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript`
		Used simple validation
	*/
 	var re = /\S+@\S+\.\S+/;
 	return re.test(email);
}
export default {
	name: 'EmailForm',

	data() {
		return {
			form: this.$form.createForm(this)
		}
	},

	methods: {
		handleSubmit(e) {
			e.preventDefault();
			this.form.validateFields((err, values) => {
				if (!err) {
					values.to_address = values.to_address.join(',')
					this.$store.dispatch('sendEmail', values)
						.then(() => {
							this.form.resetFields();
							this.$message.success('Email Sent', 2);
						});
				}
			});
		},
		validateToEmails(rule, value, callback) {
			for (let i = 0; i < value.length; i++) {
				let email = value[i];
				if (!validateEmail(email)) {
					callback(`This  ${email} has invalid email format`)
					return;
				}
			}
			if (value.length > 0) {
				callback();
				return
			}
			callback();
		}
	}
};
</script>

<style scoped>
.form {
	width: 100%;
}
</style>