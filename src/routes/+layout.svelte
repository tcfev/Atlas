<script>
    import { fly } from "svelte/transition";
	import { cubicIn, cubicOut } from 'svelte/easing';

    import Transition from "$lib/components/layout/Transition.svelte";
    import Header from "$lib/components/layout/Header.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
    import "../app.css";
    export let data = {};
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
