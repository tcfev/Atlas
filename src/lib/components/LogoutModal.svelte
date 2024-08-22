<script lang="ts">
    import * as Dialog from "$lib/components/ui/dialog";
    import { Button } from "$lib/components/ui/button";
    import { createEventDispatcher, onMount } from "svelte";
    import { supabase } from "$lib/supabaseClient";

    const dispatch = createEventDispatcher();

    export let open = false;
    let loading = false;
    let logoutSuccess = false;

    const handleLogout = async () => {
        try {
            loading = true;
            const { error } = await supabase.auth.signOut();
            if (error) throw error;
            logoutSuccess = true;
            setTimeout(() => {
                open = false;
                dispatch("close");
            }, 2000); // Close the dialog after 2 seconds
        } catch (error) {
            if (error instanceof Error) {
                alert(error.message);
            }
        } finally {
            loading = false;
        }
    };

    function onOpenChange() {
        open = false;
        dispatch("close");
    }

    onMount(async () => {});
</script>

<div class="dialog-container max-h-full">
    <Dialog.Root {open} {onOpenChange}>
        <Dialog.Content>
            <Dialog.Header>
                <Dialog.Title>خروج از سیستم</Dialog.Title>
                <Dialog.Description>
                    آیا مطمئن هستید که می‌خواهید خارج شوید؟
                </Dialog.Description>
            </Dialog.Header>

            <div class="grid gap-4 py-4">
                {#if logoutSuccess}
                    <div class="text-center text-green-500">
                        خروج موفقیت آمیز بود!
                    </div>
                {/if}
            </div>

            <Dialog.Footer>
                {#if !logoutSuccess}
                    <Button
                        type="button"
                        on:click={handleLogout}
                        disabled={loading}
                    >
                        <span>{loading ? "در حال بارگذاری" : "خروج"}</span>
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
</style>
