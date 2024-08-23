<script>
    import { page } from "$app/stores";
    import Globe from "lucide-svelte/icons/globe";
    import {
        siteTitle,
        defaultHeaderLinks,
        socialLinks,
    } from "../../../content/configs";
    import AuthButton from "$lib/components/AuthButton.svelte";
    import Github from "lucide-svelte/icons/github";

    export let haederLinks = defaultHeaderLinks;
    export let _socialLinks = socialLinks;
</script>

<footer
    class=" border-t mx-auto flex flex-col
    justify-center items-center py-8 mt-32"
>
    <div class="flex flex-col justify-between w-full max-w-screen-lg mx-auto">
        <div class="inline-flex items-center flex-col gap-4">
            <Globe class="w-16 h-16 text-indigo-300 " />
            <h1 class="font-extralight text-3xl">
                <a href="/">
                    {siteTitle}
                </a>
            </h1>
        </div>

        <div class="inline-flex flex-row flex-wrap justify-center my-8 gap-5">
            {#each haederLinks as { name, link }, idx (idx)}
                <a
                    href={link}
                    class:active-link={$page.url.pathname === link}
                    class:not-active-link={$page.url.pathname !== link}
                    class="text-sm"
                >
                    {name}
                </a>
            {/each}
        </div>
    </div>

    <div class="flex flex-row flex-wrap">
        {#each _socialLinks as { name, link, type }, idx (idx)}
            {#if type === "github"}
                <a
                    href={link}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-gray-300 hover:text-gray-500"
                >
                    <Github />
                </a>
            {/if}
        {/each}
    </div>

    <div class="mt-4 text-sm text-gray-300">
        &copy; {new Date().getFullYear()}
        {siteTitle}.Some Rights Reserved!
    </div>
    <div class="">
        <AuthButton />
    </div>
</footer>

<style>
    footer .active-link {
        @apply text-indigo-500;
    }

    footer .not-active-link {
        @apply text-gray-500;
    }
</style>
