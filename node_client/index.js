const OpenAPIClientAxios = require('openapi-client-axios').default;
const request = require("superagent");

(async () => {
	try
	{
		const api = new OpenAPIClientAxios({ 
			definition: 'http://localhost:8000/openapi.json',
			withServer: {
				url: "http://localhost:8000"
			}
		});
		const client = await api.init();
		console.log(api.getBaseURL())
		console.log(api.getBaseURL("getMessage"))

		const idJohnDoe = v4();
		const idTopic1 = v4();

		const addTopicResponse = await client.addTopic({
			userId: idJohnDoe,
			topicId: idTopic1,
			topicName: "Topic1",
			status: "ACTIVE"
		});
		const getAvailableTopicsResponse = await client.getAvailableTopics({
			userId: idJohnDoe
		});
		console.log(res.data);
	}
	catch(ex)
	{
		console.log(ex);
	}
})();

/**
 * Superuser gets credentials
 * John creates admin account
 * Jane creates student account
 * John signs into his account
 * John creates 'class A'
 * John assigns Jane to 'class A'
 * John creates topic 'Topic A' for 'class A'
 * John creates topic 'Topic B' for 'class A'
 * Jane signs into her account
 * Jane gets inventory
 */
async function main()
{
	// 
	// Superuser gets credentials
	//

	//
	// John creates admin account
	//

	//
	// Jane creates student account
	//

	//
	// John signs into his account
	//

	//
	// John creates 'class A'
	//
}

main();

