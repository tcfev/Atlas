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

    <div class="flex flex-row flex-wrap gap-2">
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
            {:else if type === "x"}
                <a
                    href={link}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-gray-300 hover:text-gray-500"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="text-gray-300"
                        width="25"
                        height="25"
                        viewBox="0 0 150 150"
                    >
                        <path
                            d="M67 .55C40.648 3.3 17.102 20.649 6.398 45.2-.5 61.05-1.648 79.3 3.25 96.101c6.05 20.949 21.7 38.648 41.95 47.5 15.85 6.898 34.1 8.046 50.902 3.148 25.148-7.25 44.949-27.898 51.449-53.55C157.699 53 132.8 11.897 92.5 2.3 83.648.2 75.852-.351 67 .55ZM68 47c6.398 8.5 11.8 15.5 12 15.5.2 0 6.852-7 14.7-15.5l14.35-15.5h8.15l-1.75 1.852c-1 1.046-7.5 8.097-14.45 15.648-6.95 7.55-13.75 14.898-15.102 16.25L83.5 67.8l18.75 24.95c10.3 13.75 18.75 25.148 18.75 25.352 0 .25-6.148.398-13.602.398l-13.648-.05-12.7-17C72.3 89.7 68.2 84.647 67.8 84.95c-.3.25-7.402 7.902-15.8 17L36.75 118.5h-3.852c-2.148 0-3.898-.102-3.898-.25 0-.148 7.95-8.852 17.648-19.3 9.653-10.45 17.653-19.2 17.75-19.348C64.45 79.398 56.5 68.55 46.75 55.5 37 42.5 29 31.75 29 31.648c0-.097 6.148-.148 13.7-.148h13.698Zm0 0"
                            style="stroke:none;fill-rule:auto;fill:#000;fill-opacity:1"
                        />
                        <path
                            d="M41.352 38.2c.199.35 12.796 17.25 27.898 37.448l27.5 36.801 6.148.051c3.801 0 6.102-.2 6-.5-.046-.25-12.597-17.148-27.796-37.5l-27.704-37H47.2c-5.148 0-6.199.102-5.847.7Zm0 0"
                            style="stroke:none;fill-rule:auto;fill:#000;fill-opacity:1"
                        />
                    </svg>
                </a>
            {/if}
        {/each}
    </div>
    <div class="mt-4 text-sm text-gray-300">
        Atlas is licensed under Creative Commons
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
