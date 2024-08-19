<script lang="ts">
    import * as Tabs from "$lib/components/ui/tabs";
    import * as Dialog from "$lib/components/ui/dialog";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import { createEventDispatcher } from "svelte";
    import Textarea from "./ui/textarea/textarea.svelte";
    import CountrySelect from "$lib/components/ui/CountrySelect.svelte";

    const dispatch = createEventDispatcher();

    export let open = false;
    export let data = {};
    export let suggestable = false;

    let forms = [
        {
            name: "اطلاعات کلی",
            value: "info",
            selected: true,
            fields: [
                {
                    id: "id",
                    displayName: "شناسه",
                    value: "",
                    type: "text",
                    disabled: true,
                },
                {
                    id: "logo",
                    displayName: "لوگو",
                    value: "",
                    type: "text",
                },
                {
                    id: "name",
                    displayName: "نام سازمان",
                    value: "",
                    type: "text",
                },
                {
                    id: "persianName",
                    displayName: "نام فارسی",
                    value: "",
                    type: "text",
                },
                {
                    id: "fullName",
                    displayName: "نام کامل",
                    value: "",
                    type: "text",
                },
                {
                    id: "location",
                    displayName: "پایگاه فعالیت",
                    value: "",
                    type: "countrySelect",
                },
            ],
        },
        {
            name: "اطلاعات ارتباطی",
            value: "contact",
            fields: [
                {
                    id: "internetAddress",
                    displayName: "پایگاه اینترنتی",
                    value: "",
                    type: "url",
                },
                { id: "contact", displayName: "تماس", value: "", type: "text" },
                { id: "x", displayName: "شبکه‌ی x", value: "", type: "text" },
                {
                    id: "instagram",
                    displayName: "اینستاگرام",
                    value: "",
                    type: "text",
                },
                {
                    id: "telegram",
                    displayName: "تلگرام",
                    value: "",
                    type: "text",
                },
            ],
        },
        {
            name: "اطلاعات سازمانی",
            value: "organization",
            fields: [
                {
                    id: "specialties",
                    displayName: "تخصص‌ها",
                    value: "",
                    type: "text",
                },
                {
                    id: "estimationOfMembers",
                    displayName: "تخمین تعداد اعضا",
                    value: "",
                    type: "number",
                },
                { id: "needs", displayName: "نیازها", value: "", type: "text" },
                {
                    id: "constitution",
                    displayName: "چارت سازمانی",
                    value: "",
                    type: "text",
                },
                {
                    id: "manifesto",
                    displayName: "بیانیه",
                    value: "",
                    type: "text",
                },
                { id: "plan", displayName: "برنامه", value: "", type: "text" },
                {
                    id: "politicalOrientation",
                    displayName: "گرایش سیاسی",
                    value: "",
                    type: "text",
                },
            ],
        },
        {
            name: "اطلاعات تکمیلی",
            value: "additional",
            fields: [
                {
                    id: "history",
                    displayName: "تاریخچه",
                    value: "",
                    type: "text",
                },
                {
                    id: "activities",
                    displayName: "فعالیت‌ها",
                    value: "",
                    type: "text",
                },
                {
                    id: "about",
                    displayName: "توضیحات",
                    value: "",
                    type: "textarea",
                },
            ],
        },
    ];

    function fillData(data) {
        forms.forEach((form) => {
            form.fields.forEach((field) => {
                field.value = data[field.id];
            });
        });
    }

    function onOpenChange() {
        // change the data fields to the value of the form fields
        forms.forEach((form) => {
            form.fields.forEach((field) => {
                data[field.id] = field.value;
            });
        });
        dispatch("close");
    }

    $: {
        if (open) {
            fillData(data);
        }
    }
</script>

<div class="dialog-container max-h-full">
    <Dialog.Root {open} {onOpenChange}>
        <Dialog.Content>
            <Dialog.Header>
                <Dialog.Title>ویرایش گروه</Dialog.Title>
                <Dialog.Description>
                    تغییرات خود را اعمال کنید و در نهایت برای ذخیره کردن دکمه‌ی
                    ذخیره را بزنید.
                </Dialog.Description>
            </Dialog.Header>

            <Tabs.Root value="overall">
                <Tabs.List
                    class="flex flex-row justify-center items-center w-full"
                >
                    {#each forms as form}
                        <Tabs.Trigger value={form.value}>
                            {form.name}
                        </Tabs.Trigger>
                    {/each}
                </Tabs.List>
                <div class="dialog-root">
                    {#each forms as form}
                        <Tabs.Content value={form.value}>
                            <div class="grid gap-4 py-4">
                                {#each form.fields as field}
                                    <div
                                        class="grid grid-cols-4 items-center gap-4"
                                    >
                                        {#if field.type === "textarea"}
                                            <Label
                                                for={field.id}
                                                class="text-right"
                                            >
                                                {field.displayName}
                                            </Label>
                                            <Textarea
                                                class="col-span-3"
                                                bind:value={field.value}
                                                placeholder=""
                                            />
                                        {:else if field.type === "countrySelect"}
                                            <Label
                                                for={field.id}
                                                class="text-right"
                                            >
                                                {field.displayName}
                                            </Label>
                                            <div class="col-span-3">
                                                <CountrySelect
                                                    bind:value={field.value}
                                                />
                                            </div>
                                        {:else}
                                            <Label
                                                for={field.id}
                                                class="text-right"
                                            >
                                                {field.displayName}
                                            </Label>
                                            <Input
                                                id={field.id}
                                                bind:value={field.value}
                                                type={field.type}
                                                class="col-span-3"
                                                disabled={field.disabled}
                                            />
                                        {/if}
                                    </div>
                                {/each}
                            </div>
                        </Tabs.Content>
                    {/each}
                </div>
            </Tabs.Root>

            <Dialog.Footer>
                {#if suggestable}
                    <Button type="submit">
                        مرحله بعد
                    </Button>
                {/if}
            </Dialog.Footer>
        </Dialog.Content>
    </Dialog.Root>
</div>

<style>
    .dialog-container {
        direction: rtl;
    }
    .dialog-root {
        @apply w-full;
        max-height: calc(100vh - 200px);
        overflow-y: auto;
        padding: 0 6px;
    }
</style>
