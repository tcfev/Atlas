<script>
    import Header from "@/components/layout/Header.svelte";
    import Footer from "@/components/layout/Footer.svelte";
    import { onMount } from "svelte";

    onMount(() => {});
</script>

<slot name="header" />

<div class="container mx-auto mt-[49px]" dir="auto">
    <slot />
</div>