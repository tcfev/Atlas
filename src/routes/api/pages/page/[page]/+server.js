import { postsPerPage } from '../../../../../content/configs'
import fetchPages from '$lib/assets/js/fetchPages'
import { json } from '@sveltejs/kit'

export const prerender = true

export const GET = async ({ params }) => {
  const { page } = params || 1

  const options = {
    offset: (page - 1) * postsPerPage,
    limit: postsPerPage
  }

  const { posts } = await fetchPages(options)
  
  return json(posts)
}