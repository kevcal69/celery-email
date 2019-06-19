<template>
	<a-table :columns="columns"
		:rowKey="record => record.id"
		:dataSource="dataSource"
		:loading="loading"
		:pagination="false"
	>
    	<span slot="status" slot-scope="status">
     		<a-tag :color="emailStatus[status]">{{status}}</a-tag>
    	</span>
	    <span slot="from_address" slot-scope="from_address">
	     	<a-tag color="blue">{{from_address}}</a-tag>
	    </span>
	    <span slot="to_address" slot-scope="to_address">
	      <a-tag v-for="email in splitEmails(to_address)" color="blue" :key="email">{{email}}</a-tag>
	    </span>
	</a-table>
</template>

<script>
import {mapActions} from 'vuex';

const columns = [{
	title: 'Status',
	dataIndex: 'status',
	width: '10%',
	scopedSlots: { customRender: 'status' }
}, {
	title: 'From Address',
	dataIndex: 'from_address',
	width: '15%',
	scopedSlots: { customRender: 'from_address' }
}, {
	title: 'To Address',
	dataIndex: 'to_address',
	width: '25%',
	scopedSlots: { customRender: 'to_address' }
}, {
	title: 'Subject',
	dataIndex: 'subject',
	width: '10%',
}, {
	title: 'Body',
	dataIndex: 'body',
	width: '30%',
}, {
	title: 'Sent At',
	dataIndex: 'when_sent',
	width: '10%',
}];

const emailStatus = {
	Pending: '#87d068',
	Sent: '#108ee9',
	Failed: '#f50'
}
export default {
	name: 'EmailList',

	data() {
		return {
			emailStatus,
			columns,
			dataSource: [],
			loading: false,
			top: 0
		}
	},

	mounted() {
		this.loading = true;
		this.fetchEmailQueue()
			.then((response) => {
				this.loading = false;
				let results = response.data;
				this.dataSource = [...this.dataSource, ...results];
				console.log(this.dataSource)
			});
	},

	methods: {
		...mapActions(['fetchEmailQueue']),

		splitEmails(emails) {
			return emails.split(',');
		}
	}
};
</script>