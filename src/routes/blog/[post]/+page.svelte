<script>
    import BlogPageLayout from "@/components/layout/BlogPageLayout.svelte";
    import Contact from "lucide-svelte/icons/contact";
    export let data;

    const {
        title,
        date,
        updated,
    } = data.meta;
    const { PostContent } = data;
</script>

<BlogPageLayout>
    <div slot="header" class="w-full bg-white h-64 p-8 shadow-sm header"></div>
    <article class="w-full mx-auto max-w-[800px] prose lg:prose-xl relative">
        <div
            class="w-16 h-16 bg-white rounded-md border top-[-80px] absolute p-2 text-gray-700"
        >
            <Contact class="w-full h-full" />
        </div>
        <h1 class="pt-8 pb-8 border-b">
            {title}
        </h1>
        <div class="flex flex-col gap-2 text-sm mt-[-30px]">
            <div>
                <b>نوشته شده در:</b>
                <span>{date}</span>
            </div>
            <div>
                <b>بروزرسانی شده در:</b>
                <span>{updated}</span>
            </div>
        </div>

        <svelte:component this={PostContent} dir="auto" />

    </article>
</BlogPageLayout>

<style>
    .header {
        background-color: #ffdee9;
        background-image: linear-gradient(0deg, #ffdee9 0%, #b5fffc 100%);
    }
</style>
