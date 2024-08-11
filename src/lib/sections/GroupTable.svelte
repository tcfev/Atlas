<script lang="ts">
    import {
        createTable,
        Render,
        Subscribe,
        createRender,
    } from "svelte-headless-table";
    import {
        addPagination,
        addSortBy,
        addTableFilter,
    } from "svelte-headless-table/plugins";
    import { readable } from "svelte/store";
    import ArrowUpDown from "lucide-svelte/icons/arrow-up-down";
    import * as Table from "@/components/ui/table";
    // import DataTableActions from "./data-table-actions.svelte";
    import Button from "@/components/ui/button/button.svelte";
    import Input from "@/components/ui/input/input.svelte";
    import { onMount } from "svelte";

    export let data: any[] = [];

    let table;

    let columns;

    let headerRows, pageRows, tableAttrs, tableBodyAttrs, pluginStates;

    let hasNextPage, hasPreviousPage, pageIndex;
    let filterValue;

    function renderTable(data) {
        table = createTable(readable(data), {
            page: addPagination(),
            sort: addSortBy(),
            filter: addTableFilter({
                fn: ({ filterValue, value }) =>
                    value.toLowerCase().includes(filterValue.toLowerCase()),
            }),
        });
        columns = table.createColumns([
            table.column({
                accessor: "@dropdown",
                header: "@dropdown",
            }),
            table.column({
                accessor: "Persian name",
                header: "Persian name",
            }),
            table.column({
                accessor: "englishName",
                header: "English Name",
            }),
            table.column({
                accessor: "Full name",
                header: "Full Name",
            }),
            table.column({
                accessor: "location",
                header: "Location",
            }),
            table.column({
                accessor: "internetAddress",
                header: "Internet Address",
            }),
            table.column({
                accessor: "Contact",
                header: "Contact",
            }),
            table.column({
                accessor: "assets & specialties",
                header: "Assets & Specialties",
            }),
            table.column({
                accessor: "estimation of Nb of members",
                header: "Estimation of Nb of Members",
            }),
            table.column({
                accessor: "Needs/Wants",
                header: "Needs/Wants",
            }),
            table.column({
                accessor: "constitution",
                header: "Constitution",
            }),
            table.column({
                accessor: "مرامنامه و باورها و منشور",
                header: "مرامنامه و باورها و منشور",
            }),
            table.column({
                accessor: "Plan",
                header: "Plan",
            }),
            table.column({
                accessor: "گرایش سیاسی",
                header: "گرایش سیاسی",
            }),
            table.column({
                accessor: "about",
                header: "About",
            }),
            table.column({
                accessor: "activities",
                header: "Activities",
            }),
            table.column({
                accessor: "History",
                header: "History",
            }),
            // table.column({
            //     accessor: ({ id }) => id,
            //     header: "",
            //     cell: ({ value }) => {
            //         return createRender(DataTableActions, { id: value });
            //     },
            // }),
        ]);

        const tableRes = table.createViewModel(columns);

        headerRows = tableRes.headerRows;
        pageRows = tableRes.pageRows;
        tableAttrs = tableRes.tableAttrs;
        tableBodyAttrs = tableRes.tableBodyAttrs;
        pluginStates = tableRes.pluginStates;

        hasNextPage = pluginStates.page.hasNextPage;
        hasPreviousPage = pluginStates.page.hasPreviousPage;
        pageIndex = pluginStates.page.pageIndex;

        filterValue = pluginStates?.filter.filterValue;
    }

    $: renderTable(data);
    onMount(() => {});
</script>

{#if table}
    <div>
        <div class="flex items-center py-4">
            <Input
                class="max-w-sm"
                placeholder="جستجوی گروه‌ها ..."
                type="text"
                bind:value={$filterValue}
            />
        </div>
        <div class="rounded-md border">
            <Table.Root {...$tableAttrs}>
                <Table.Header>
                    {#each $headerRows as headerRow}
                        <Subscribe rowAttrs={headerRow.attrs()}>
                            <Table.Row>
                                {#each headerRow.cells as cell (cell.id)}
                                    <Subscribe
                                        attrs={cell.attrs()}
                                        let:attrs
                                        props={cell.props()}
                                        let:props
                                    >
                                        <Table.Head {...attrs}>
                                            {#if cell.id === "amount"}
                                                <div class="text-right">
                                                    <Render
                                                        of={cell.render()}
                                                    />
                                                </div>
                                            {:else if cell.id === "email"}
                                                <Button
                                                    variant="ghost"
                                                    on:click={props.sort.toggle}
                                                >
                                                    <Render
                                                        of={cell.render()}
                                                    />
                                                    <ArrowUpDown
                                                        class="ml-2 h-4 w-4"
                                                    />
                                                </Button>
                                            {:else}
                                                <Render of={cell.render()} />
                                            {/if}
                                        </Table.Head>
                                    </Subscribe>
                                {/each}
                            </Table.Row>
                        </Subscribe>
                    {/each}
                </Table.Header>
                <Table.Body {...$tableBodyAttrs}>
                    {#each $pageRows as row (row.id)}
                        <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
                            <Table.Row {...rowAttrs}>
                                {#each row.cells as cell (cell.id)}
                                    <Subscribe attrs={cell.attrs()} let:attrs>
                                        <Table.Cell {...attrs}>
                                            {#if cell.id === "amount"}
                                                <div
                                                    class="text-right font-medium"
                                                >
                                                    <Render
                                                        of={cell.render()}
                                                    />
                                                </div>
                                            {:else if cell.id === "status"}
                                                <div class="capitalize">
                                                    <Render
                                                        of={cell.render()}
                                                    />
                                                </div>
                                            {:else}
                                                <Render of={cell.render()} />
                                            {/if}
                                        </Table.Cell>
                                    </Subscribe>
                                {/each}
                            </Table.Row>
                        </Subscribe>
                    {/each}
                </Table.Body>
            </Table.Root>
        </div>
        <div class="flex items-center justify-end space-x-4 py-4">
            <Button
                variant="outline"
                size="sm"
                on:click={() => ($pageIndex = $pageIndex - 1)}
                disabled={!$hasPreviousPage}>Previous</Button
            >
            <Button
                variant="outline"
                size="sm"
                disabled={!$hasNextPage}
                on:click={() => ($pageIndex = $pageIndex + 1)}>Next</Button
            >
        </div>
    </div>
{/if}
