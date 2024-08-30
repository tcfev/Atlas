<script>
    import { toasts, removeToast } from "../stores/toast";
    import X from "lucide-svelte/icons/x";

    let toastArray = [
        {
            id: 1,
            title: "Notice",
            message: "This is a notice",
            color: "#333",
            action: () => removeToast(1),
            actionText: "Close",
        },
        {
            id: 2,
            title: "Warning",
            message: "This is a warning",
            color: "orange",
            action: () => removeToast(2),
            actionText: "Close",
        },
        {
            id: 3,
            title: "Error",
            message: "This is an error",
            color: "red",
            action: () => removeToast(3),
            actionText: "Close",
        },
    ];
</script>

سس
<div class="toast-container animate-in">
    {#each toastArray as toast (toast.id)}
        <div class="toast">
            <div class="flex justify-between items-center">
                <div>
                    <p class="font-semibold">
                        {toast.title || "Notice"}
                    </p>
                    <p>
                        {toast.message}
                    </p>
                </div>
                <button class="close-btn" on:click={toast.action}>
                    <X />
                </button>
            </div>
        </div>
    {/each}
</div>

<style>
    .toast-container {
        @apply fixed bottom-4 right-4 flex flex-col space-y-2;
    }
    .toast {
        @apply bg-gray-100 text-gray-600 p-4 rounded-lg border-2 border-gray-200;
    }
    .close-btn {
        @apply ml-4 p-2 bg-gray-900 text-gray-200 rounded hover:bg-gray-700;
    }
</style>
