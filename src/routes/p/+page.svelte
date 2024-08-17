<script>
    import { onMount } from "svelte";
    import Header from "@/components/layout/Header.svelte";
    import Footer from "@/components/layout/Footer.svelte";

    export let data;
	const posts = data.posts;
</script>

<svelte:head>
    <title>اطلس جامعه مدنی ایران - وبلاگ</title>
</svelte:head>

<Header />

<div class="mt-16">
    {#each posts as post}
        <div>
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            <a href="p/{post.slug}">ادامه مطلب</a>
        </div>
    {/each}
</div>

<Footer />