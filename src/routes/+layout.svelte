<script>
    import { fly } from "svelte/transition";
    import { cubicIn, cubicOut } from "svelte/easing";

    import Transition from "$lib/components/layout/Transition.svelte";
    import Header from "$lib/components/layout/Header.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
    import { onMount } from "svelte";
    import { supabase } from "$lib/supabaseClient";
    import { authStore } from "$lib/stores/authStore";

    import "../app.css";
    export let data = {};

    onMount(async () => {
        const {
            data: { session },
        } = await supabase.auth.getSession();
        const user = session?.user ?? null;

        if (user) {
            const { email, email_confirmed_at, last_sign_in_at } = user;
            authStore.update((state) => {
                return {
                    ...state,
                    user: {
                        email,
                        email_confirmed_at,
                        last_sign_in_at
                    },
                };
            });
        }

        supabase.auth.onAuthStateChange((event, session) => {
            const user = session?.user ?? null;
            if (user) {
                const { email, email_confirmed_at, last_sign_in_at } = user;
                authStore.update((state) => {
                    return {
                        ...state,
                        isAuthenticated: !!user,
                        user: {
                            email,
                            email_confirmed_at,
                            last_sign_in_at
                        },
                    };
                });
            }else{
                authStore.update((state) => {
                    return {
                        ...state,
                        isAuthenticated: !!user,
                        user: null,
                    };
                });
            }
        });
    });
</script>


<div class="flex h-screen flex-col justify-between pt-[49px]">
    <Header />
    <main class="mb-auto">
        {#key data?.pathname}
            <div
                in:fly={{ easing: cubicOut, y: 10, duration: 300, delay: 400 }}
                out:fly={{ easing: cubicIn, y: -10, duration: 300 }}
            >
                <slot />
            </div>
        {/key}
    </main>
    <div class="w-full">
        <Footer />
    </div>
</div>