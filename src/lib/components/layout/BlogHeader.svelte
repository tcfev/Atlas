<script>
    import Contact from "lucide-svelte/icons/contact";
    export let title;
    export let date;
    export let updated;
</script>

<div class="w-full bg-white h-64 p-8 shadow-sm header"></div>

<div class="w-full mx-auto max-w-[800px] relative">
    <div
        class="w-16 h-16 bg-white rounded-md border top-[-40px] absolute p-2 text-gray-700  md:right-0 right-8"
    >
        <slot name="page-logo" />
    </div>
    <h1 class="pt-8 pb-8 text-5xl md:pr-0 px-8">
        {title}
    </h1>
    <div class="flex flex-col gap-2 text-sm mt-2 md:pr-0 px-8">
        <div>
            <b>نوشته شده در:</b>
            <span>{date}</span>
        </div>
        <div>
            <b>بروزرسانی شده در:</b>
            <span>{updated}</span>
        </div>
    </div>
</div>

<style>
    .header {
        background-image: linear-gradient(-225deg, #fffeff 0%, #d7fffe 100%);
    }
</style>
