<script>
    import Button from "@/components/ui/button/button.svelte";
    import { onMount } from "svelte";
    import * as Card from "$lib/components/ui/card/index.js";
    import Link from "lucide-svelte/icons/link";
    import Scale from "lucide-svelte/icons/scale";
    import ScrollText from "lucide-svelte/icons/scroll-text";
    import Fullscreen from "lucide-svelte/icons/fullscreen";
    import MapPin from "lucide-svelte/icons/map-pin";
    import Users from "lucide-svelte/icons/users";
    import * as Tooltip from "$lib/components/ui/tooltip/index.js";
    import ListAllGroups from "@/sections/ListAllGroups.svelte";
    import Header from "@/sections/Header.svelte";
    import Hash from "lucide-svelte/icons/hash";

    let data = [];

    let stats = [
        { title: 'تعداد کل گروه‌های فعال', value: 0 },
        { title: 'اخرین بروزرسانی', value: '۱۴۰۳/۰۸/۱۰' }
    ];

    onMount(() => {
        fetch("/data/political_parties-2024-08-10.json")
            .then((response) => response.json())
            .then((json) => {
                data = json;
                stats[0].value = data.length;
            });
    });

</script>

<svelte:head>
    <title>
        اطلس جامعه مدنی ایران - احزاب
    </title>
</svelte:head>


<Header />

<div class="container mx-auto">
    <div class="my-32">
        <h1 class="text-4xl font-bold text-indigo-400 mb-4">
            احزاب
        </h1>
        <p class="text-justify text-gray-600">
            در این بخش می‌توانید اطلاعات مربوط به احزاب فعال در ایران را مشاهده کنید.
            احزاب فعال در این اطلس بر اساس اطلاعات موجود در منابع معتبر و مستندات عمومی
            جمع‌آوری شده‌اند.
            جمع‌آوری اطلاعات این اطلس از سال ۱۴۰۳ آغاز شده و تاکنون ادامه دارد.
            اگر اطلاعاتی در این اطلس ناقص یا نادرست است، خواهشمندیم از طریق صفحه‌ی تماس با ما به ما اطلاع دهید.
            شما هم می‌توانید به این اطلس کمک کنید برای اطلاعات بیشتر به بخش «همکاری» مراجعه کنید.
        </p>
    </div>
    
    <div class="flex flex-row my-16 gap-4">
        {#each stats as { title, value }}
            <Card.Root class="w-[250px]">
                <Card.Header class="flex flex-row items-center justify-between space-y-0 pb-2">
                    <Card.Title class="text-sm font-medium">
                        {title}
                    </Card.Title>
                </Card.Header>
                <Card.Content>
                    <div class="text-2xl font-bold">
                        {value}
                    </div>
                    <p class="text-muted-foreground text-xs"></p>
                </Card.Content>
            </Card.Root>
        {/each}
    </div>
    
    <ListAllGroups {data} />
</div>