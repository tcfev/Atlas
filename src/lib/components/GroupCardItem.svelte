<script>
    import Button from "@/components/ui/button/button.svelte";
    import * as Card from "$lib/components/ui/card/index.js";
    import Link from "lucide-svelte/icons/link";
    import Scale from "lucide-svelte/icons/scale";
    import ScrollText from "lucide-svelte/icons/scroll-text";
    import Fullscreen from "lucide-svelte/icons/fullscreen";
    import MapPin from "lucide-svelte/icons/map-pin";
    import Users from "lucide-svelte/icons/users";
    import * as Tooltip from "$lib/components/ui/tooltip/index.js";
    import ListAllGroups from "@/components/ListAllGroups.svelte";
    import Pencil from "lucide-svelte/icons/pencil";
    import Trash from "lucide-svelte/icons/trash";
    import { createEventDispatcher } from "svelte";
    import XIcon from "@/icons/XIcon.svelte";
    import InstagramIcon from "@/icons/InstagramIcon.svelte";
    import ArrowUpRight from "lucide-svelte/icons/arrow-up-right";
    import Loading from "@/components/ui/loading/Loading.svelte";
    import { goto } from "$app/navigation";
    const dispatch = createEventDispatcher();

    export let id = "";
    export let logo = "";
    export let name_fa = "";
    export let name_en = "";
    export let name_short = "";
    export let estimationOfMembers;
    export let location;
    export let about;
    export let manifesto;
    export let internet_address;
    export let constitution;
    export let social_x;
    export let social_instagram;
    export let editable = true;
    export let pageLink;


    let name;

    export let loading = false;

    function truncateString(str, length) {
        if (!str) return "";
        return str.length > length ? `${str.substring(0, length)}...` : str;
    }

    function handleEditClick(e) {
        dispatch("edit", { id });

    }

    function handleDeleteClick(e) {
        dispatch("delete", { id });
    }

    function handleCardClick(e) {
        if (!pageLink){
            return;
        }
        goto(pageLink);
    }

    function gotoPage(link) {
        return (e) =>{
            if(!link || typeof window === "undefined"){
                return;
            }

            e.preventDefault();
            e.stopPropagation();
            
            window.open(link, "_blank");
        }
    }


    $: name= name_fa || name_en || name_short || id || "بدون نام";
</script>
<Loading {loading} class="mb-4">
    <button on:click={handleCardClick} class="w-full {!pageLink? 'cursor-default':''}">
        <Card.Root
            class="w-full  shadow-sm hover:shadow-md {pageLink
                ? ' transition-all cursor-pointer '
                : ''}"
        >
            <Card.Header>
                <div class="flex flex-row gap-4">
                    <div class="w-[78px] flex flex-row justify-center">
                        {#if logo}
                            <div class="image-wrapper">
                                <img
                                    src={logo}
                                    alt="{name} logo"
                                    class="image"
                                />
                            </div>
                        {:else}
                            <div class="image-wrapper">
                                <Fullscreen class="h-8 w-8" />
                            </div>
                        {/if}
                    </div>
                    <div class="title-container">
                        <Card.Title>
                            <h3 class="text-lg font-semibold">
                                {name}
                            </h3>
                        </Card.Title>
                        <Card.Description>
                            <div class="flex flex-row gap-2">
                                <Tooltip.Root>
                                    <Tooltip.Trigger>
                                        <div
                                            class="inline-flex flex-row justify-center items-center gap-2"
                                        >
                                            <Users class="h-4 w-4" />
                                            <span>
                                                {estimationOfMembers || "?"}
                                            </span>
                                        </div>
                                    </Tooltip.Trigger>
                                    <Tooltip.Content>
                                        <p>تعداد تخمینی اعضا</p>
                                    </Tooltip.Content>
                                </Tooltip.Root>

                                <Tooltip.Root>
                                    <Tooltip.Trigger>
                                        <div
                                            class="inline-flex flex-row justify-center items-center gap-2"
                                        >
                                            <MapPin class="h-4 w-4" />
                                            <span>
                                                {truncateString(
                                                    location || "?",
                                                    20,
                                                )}
                                            </span>
                                        </div>
                                    </Tooltip.Trigger>
                                    <Tooltip.Content>
                                        <p>پایگاه فعالیت</p>
                                    </Tooltip.Content>
                                </Tooltip.Root>
                            </div>
                        </Card.Description>
                    </div>
                </div>
            </Card.Header>
            <Card.Content>
                <div class="flex flex-row content-container">
                    <div
                        class="flex flex-col items-start space-x-4 rounded p-2 w-full"
                    >
                        <div class="flex-1 space-y-1 w-full">
                            <p dir="auto" class="about">
                                {truncateString(about, 100) ||
                                    "توضیحاتی در دسترس نیست"}
                            </p>
                        </div>
                    </div>
                </div>
                <!-- Add more fields as necessary -->
            </Card.Content>
            <Card.Footer>
                <div class="content-container links-container">
                    {#if editable}
                        <Button
                            variant="outline"
                            class="text-blue-700"
                            on:click={handleEditClick}
                        >
                            <Pencil class="h-4 w-4" />
                        </Button>
                        <Button
                            variant="outline"
                            class="text-red-700"
                            on:click={handleDeleteClick}
                        >
                            <Trash class="h-4 w-4" />
                        </Button>
                    {/if}

                    {#if internet_address}
                        <Button
                            variant="outline"
                            on:click={gotoPage(internet_address)}
                        >
                            <Link class="h-4 w-4" />
                        </Button>
                    {/if}

                    {#if social_x}
                        {#each social_x as _x}
                            <Button
                                variant="outline"
                                on:click={gotoPage(`https://x.com/${_x}`)}
                            >
                                <div class="h-4 w-4">
                                    <XIcon />
                                </div>
                            </Button>
                        {/each}
                    {/if}

                    {#if social_instagram}
                        {#each social_instagram as insta}
                            <Button
                                variant="outline"
                                on:click={gotoPage(`https://instagram.com/${insta}/`)}
                            >
                                <div class="h-4 w-4">
                                    <InstagramIcon />
                                </div>
                            </Button>
                        {/each}
                    {/if}

                    {#if manifesto}
                        <Button
                            variant="outline"
                            class="text-green-700"
                            on:click={gotoPage(manifesto)}
                        >
                            <Scale class="ml-2 h-4 w-4" />
                            منشور
                        </Button>
                    {/if}

                    {#if constitution}
                        <Button
                            variant="outline"
                            on:click={gotoPage(constitution)}
                            class="text-blue-700"
                        >
                            <ScrollText class="ml-2 h-4 w-4" />
                            چارت سازمانی
                        </Button>
                    {/if}
                </div>
            </Card.Footer>
        </Card.Root>
    </button>
</Loading>

<style>
    .content-container {
        direction: rtl;
    }

    .image-wrapper {
        @apply border rounded;
        width: 80px;
        height: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: white;
        overflow: hidden;
    }

    .image {
        width: 100%;
        height: 100%;
        object-fit: contain; /* Ensures the whole image fits within the container */
    }
    .about {
        @apply text-muted-foreground text-sm;
    }

    .title-container {
        @apply flex flex-col pt-2;
        max-width: 100%;
        word-break: break-word;
    }
    .links-container {
        @apply w-full flex flex-row gap-2 flex-wrap;
    }
</style>
