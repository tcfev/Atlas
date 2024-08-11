import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import adapter from '@sveltejs/adapter-static';
// import adapter from '@sveltejs/adapter-cloudflare';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		adapter: adapter({
			fallback: 'index.html' // may differ from host to host
		}),

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
		alias: {
			"@/*": "./src/lib/*",
		},
	},
	preprocess: vitePreprocess()

};

export default config;
