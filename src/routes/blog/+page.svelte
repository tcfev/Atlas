<script>
    import { onMount } from "svelte";
    import Header from "@/components/layout/Header.svelte";
    export let data;
	const posts = data.posts;
</script>

<svelte:head>
    <title>اطلس جامعه مدنی ایران - وبلاگ</title>
</svelte:head>

<Header />

<div class="mb-16">
    {#each posts as post}
        <div>
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            <a href="blog/{post.slug}">ادامه مطلب</a>
        </div>
    {/each}
</div>