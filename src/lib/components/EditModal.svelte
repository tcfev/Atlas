<script lang="ts">
    import * as Tabs from "$lib/components/ui/tabs";
    import * as Dialog from "$lib/components/ui/dialog";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";

    export let open = false;

    let forms = [
        {
            name: "اطلاعات کلی",
            value: "overall",
            selected: true,
            fields: [
                { id: "id", value: "", type: "text", disabled: false },

                { id: "نام", value: "", type: "text" },
                { id: "نام فارسی", value: "", type: "text" },
                { id: "پایگاه فعالیت", value: "", type: "text" },
                { id: "پایگاه اینترنتی", value: "", type: "url" },
                { id: "Contact", value: "", type: "text" },
                { id: "assets & specialties", value: "", type: "text" },
                {
                    id: "estimation of Nb of members",
                    value: "",
                    type: "number",
                },
                { id: "Needs/Wants", value: "", type: "text" },
                { id: "constitution", value: "", type: "text" },
                { id: "مرامنامه و باورها و منشور", value: "", type: "text" },
                { id: "Plan", value: "", type: "text" },
                { id: "گرایش سیاسی", value: "", type: "text" },
                { id: "about", value: "", type: "text" },
                { id: "activities", value: "", type: "text" },
                { id: "fullName", value: "", type: "text" },
                { id: "history", value: "", type: "text" },
            ],
        },
        {
            name: "نام",
            value: "name",
            selected: false,
            fields: [
                { id: "first-name", value: "Pedro", type: "text" },
                { id: "last-name", value: "Duarte", type: "text" },
            ],
        },
    ];
</script>

<div class="dialog-container max-h-full">
    <Dialog.Root {open}>
        <Dialog.Content>
            <Dialog.Header>
                <Dialog.Title>ویرایش گروه</Dialog.Title>
                <Dialog.Description>
                    تغییرات خود را اعمال کنید و در نهایت برای ذخیره کردن دکمه‌ی
                    ذخیره را بزنید.
                </Dialog.Description>
            </Dialog.Header>

            <Tabs.Root value="account">
                <Tabs.List>
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
                                        <Label for={field.id} class="text-right"
                                            >{field.id.charAt(0).toUpperCase() +
                                                field.id.slice(1)}</Label
                                        >
                                        <Input
                                            id={field.id}
                                            bind:value={field.value}
                                            type={field.type}
                                            class="col-span-3"
                                        />
                                    </div>
                                {/each}
                            </div>
                        </Tabs.Content>
                    {/each}
                </div>
            </Tabs.Root>

            <Dialog.Footer>
                <Button type="submit">ذخیره‌ی تغییرات</Button>
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
        overflow-y: scroll;
        padding: 0 6px;
    }
</style>
