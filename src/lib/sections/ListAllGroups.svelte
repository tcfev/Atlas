<script>
    import GroupCardItem from "./GroupCardItem.svelte";
    import { createEventDispatcher } from "svelte";
    import Button from "@/components/ui/button/button.svelte";
    import GroupTable from "./GroupTable.svelte";


    const dispatch = createEventDispatcher();

    export let data = [];

    function truncateString(str, length) {
        if (!str) return "";
        return str.length > length ? `${str.substring(0, length)}...` : str;
    }

    function edit(e){
        dispatch('edit', e.detail);
    }
</script>

<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each data as item, idx (idx)}
        <GroupCardItem {...item} on:edit={edit} />
    {/each}
</div>

<!-- <GroupTable {data}/> -->

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
</style>
