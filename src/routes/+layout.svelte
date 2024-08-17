<script>
    import Transition from "$lib/components/layout/Transition.svelte";
    import Header from "$lib/components/layout/Header.svelte";
    import Footer from "$lib/components/layout/Footer.svelte";
    import "../app.css";
    export let data = {};
</script>

<div class="flex h-screen flex-col justify-between">
    <Header />
    <main class="mb-auto">
        <Transition pathname={data?.pathname}>
            <slot />
        </Transition>
    </main>
    <div class="w-full">
        <Footer />
    </div>
</div>
