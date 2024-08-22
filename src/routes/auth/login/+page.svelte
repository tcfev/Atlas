<script lang="ts">
    import * as Dialog from "$lib/components/ui/dialog";
    import { Button } from "$lib/components/ui/button";
    import { Input } from "$lib/components/ui/input/index.js";
    import { Label } from "$lib/components/ui/label/index.js";
    import { createEventDispatcher, onMount } from "svelte";
    import { supabase } from '$lib/supabaseClient';

    const dispatch = createEventDispatcher();

    export let open = true;
    let loading = false;
    let email = '';
    let password = '';

    const handleLogin = async () => {
        try {
            loading = true;
            const { error } = await supabase.auth.signInWithPassword({ email, password });
            if (error) throw error;
            alert('Check your email for login link!');
        } catch (error) {
            if (error instanceof Error) {
                alert(error.message);
            }
        } finally {
            loading = false;
        }
    };

    function onOpenChange() {
        dispatch("close");
    }

    
    onMount( async () => {
    });
</script>

<div class="dialog-container max-h-full">
    <Dialog.Root {open} {onOpenChange}>
        <Dialog.Content>
            <Dialog.Header>
                <Dialog.Title>
                    ورود به سیستم
                </Dialog.Title>
                <Dialog.Description>
                    لطفا ایمیل و رمز عبور خود را وارد کنید.
                </Dialog.Description>
            </Dialog.Header>

            <div class="grid gap-4 py-4">
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="email" class="text-right">
                        ایمیل
                    </Label>
                    <Input
                        id="email"
                        bind:value={email}
                        type="email"
                        class="col-span-3"
                    />
                </div>
                <div class="grid grid-cols-4 items-center gap-4">
                    <Label for="password" class="text-right">
                        رمز عبور
                    </Label>
                    <Input
                        id="password"
                        bind:value={password}
                        type="password"
                        class="col-span-3"
                    />
                </div>
            </div>

            <Dialog.Footer>
                <Button type="submit" on:click={handleLogin} disabled={loading}>
                    <span>{loading ? 'در حال بارگذاری' : 'ورود'}</span>
                </Button>
            </Dialog.Footer>
        </Dialog.Content>
    </Dialog.Root>
</div>

<style>
    .dialog-container {
        direction: rtl;
    }
</style>