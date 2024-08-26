<script>
    import BlogHeader from "@/components/layout/BlogHeader.svelte";
    import OrgPageLayout from "@/components/layout/OrgPageLayout.svelte";
    import Contact from "lucide-svelte/icons/contact";
    import Header from "@/components/layout/Header.svelte";
    import Footer from "@/components/layout/Footer.svelte";
    export let data;

    const { title, date, updated, headerBg , isSvx } = data.meta;
    const { PostContent } = data;
</script>

{#if !isSvx}
    <BlogHeader {title} {date} {updated} {headerBg}>
        <Contact class="w-full h-full" slot="page-logo" />
    </BlogHeader>

    <OrgPageLayout>
        <article
            class="w-full mx-auto max-w-[800px] prose lg:prose-xl relative"
        >
            <svelte:component this={PostContent} dir="auto" />
        </article>
    </OrgPageLayout>
{:else}
    <Header />

    <div class="w-full mx-auto max-w-[800px] prose lg:prose-xl relative mb-24">
        <svelte:component this={PostContent} dir="auto" />
    </div>

    <Footer />
{/if}
