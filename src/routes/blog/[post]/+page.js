import { error } from '@sveltejs/kit'

export const load = async ({ params }) => {
	try {	
		const post = await import(`../../../content/posts/${params.post}.md`)
		
		return {
			PostContent: post.default,
			meta: { ...post.metadata, slug: params.post } 
		}
	} catch(err) {
		console.log(err)
		error(404, err);
	}
}
