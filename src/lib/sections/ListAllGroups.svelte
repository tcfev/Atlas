<script>
    import GroupCardItem from "./GroupCardItem.svelte";
    import { createEventDispatcher } from "svelte";
    import Button from "@/components/ui/button/button.svelte";
    import GroupTable from "./GroupTable.svelte";
    import Input from "$lib/components/ui/input/input.svelte";

    const dispatch = createEventDispatcher();

    export let data = [];
    let _data = [];
    let filters = [
        { title: "همه", value: "all" },
        { title: "دارای اینستاگرام", value: "instagram" },
        { title: "دارای تلگرام", value: "telegram" },
        { title: "دارای x", value: "x" },
        { title: "دارای وبسایت", value: "internetAddress" },
        { title: "دارای مرامنامه", value: "manifesto" },
        { title: "دارای چارت سازمانی", value: "constitution" },
    ];
    let selectedFilter = [];

    let searchText = "";

    function truncateString(str, length) {
        if (!str) return "";
        return str.length > length ? `${str.substring(0, length)}...` : str;
    }

    function edit(e) {
        dispatch("edit", e.detail);
    }

    function dataSourceChanged(d) {
        _data = d;
    }

    function addFilter(filter) {
        if (filter === "all") return (selectedFilter = ["all"]);
        if (selectedFilter.includes(filter)) {
            selectedFilter = selectedFilter.filter((v) => v !== filter);
        } else {
            selectedFilter = [...selectedFilter, filter];
        }
    }

    function applyFilters(data, filter, search) {
        if (selectedFilter.includes("all") || selectedFilter.length === 0) {
            _data = data;
        } else {
            _data = data.filter((item) => {
                return selectedFilter.some((filter) => item[filter]);
            });
        }

        if (search) {
            _data = _data.filter((item) => {
                return (
                    item.name?.includes(search) ||
                    item.about?.includes(search) ||
                    item.manifesto?.includes(search)
                );
            });
        }
    }

    $: dataSourceChanged(data);
    $: applyFilters(data, selectedFilter, searchText);
</script>

<div class="w-full flex flex-row flex-wrap justify-between items-center my-4 gap-4">
    <div class="min-w-[300px] max-w-full">
        <Input bind:value={searchText} placeholder="جستجو" />
    </div>

    <div class="flex flex-row gap-2 flex-wrap sm:justify-start justify-between">
        {#each filters as { title, value } (value)}
            <Button
                class="text-sm {selectedFilter.includes(value)
                    ? 'text-blue-800 border-blue-800'
                    : ''}"
                variant="outline"
                size="sm"
                on:click={() => addFilter(value)}
            >
                {title}
            </Button>
        {/each}
    </div>
</div>

{#if _data.length === 0}
    <span class="h-40 w-full flex flex-row justify-center items-center">
        گروهی یافت نشد
    </span>
{:else}
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {#each _data as item, idx (idx)}
            <GroupCardItem {...item} on:edit={edit} />
        {/each}
    </div>
{/if}

<!-- <GroupTable {data}/> -->

<style>
   
</style>
