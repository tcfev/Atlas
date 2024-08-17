import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';


// cloudflare 
// import adapter from '@sveltejs/adapter-cloudflare';

// static
// import adapter from '@sveltejs/adapter-static';

// auto
import adapter from '@sveltejs/adapter-auto';

import { mdsvex } from 'mdsvex';
import mdsvexConfig from './mdsvex.config.js';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: [
		'.svelte', 
		...mdsvexConfig.extensions
	],

	preprocess: [
		mdsvex(mdsvexConfig),
		vitePreprocess(),
	],


	kit: {
		// --------------------------------------------------- static
		// adapter: adapter({
		// 	fallback: 'index.html'
		// }),

		// --------------------------------------------------- cloudflare 
		// adapter: adapter({
		// 	// See below for an explanation of these options
		// 	routes: {
		// 		include: ['/*'],
		// 		exclude: ['<all>']
		// 	},
		// 	platformProxy: {
		// 		configPath: 'wrangler.toml',
		// 		environment: undefined,
		// 		experimentalJsonConfig: false,
		// 		persist: false
		// 	}
		// }),

		// --------------------------------------------------- auto
		adapter: adapter(),




		alias: {
			"@/*": "./src/lib/*",
		},

		prerender: {
			entries: [
				'*',
				'/api/pages/page/*',
				'/api/posts/page/*',
			]
		},
		csp: { mode: 'auto' }

	},

};

export default config;
