import { error } from '@sveltejs/kit'
export const load = async ({ params }) => {
	let post;
	let isSvx = true;


	try {
		post = await import(`../../../content/pages/${params.page}.md`);
		isSvx = false;
	} catch (err) {
		console.log(err);
		try {
			post = await import(`../../../content/pages/${params.page}.svx`);
		} catch (err) {
			console.log(err);
			return error(404, err);
		}
	}

	if(!post) {
		return error(404, new Error('Post not found'));
	}
	

	return {
		PostContent: post.default,
		meta: { 
			isSvx,
			...post.metadata, 
			slug: params.post, 
			
		}
	}
}
