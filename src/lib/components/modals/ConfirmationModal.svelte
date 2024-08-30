<script>
    import { closeModal } from "$lib/components/modals/store.js";
    import GeneralModal from "$lib/components/modals/GeneralModal.svelte";
    import Button from "$lib/components/Button.svelte";

    export let isOpen = false;

    export let title = "";
    export let description = "";
    export let acceptText = "OK";
    export let cancelText = "Cancel";
    export let onAccept = () => {};
</script>

<GeneralModal {isOpen}>
    <h2>{title}</h2>
    <p>{description}</p>
    <div class="actions">
        <button on:click={closeModal}>
            {cancelText}
        </button>
        <Button
            onClick={() => {
                if (typeof onAccept === "function") onAccept();
                closeModal();
            }}
            type="primary"
        >
            {acceptText}
        </Button>
    </div>
</GeneralModal>

<style>
    h2 {
        text-align: left;
        font-size: 24px;
    }

    p {
        text-align: center;
        margin-top: 16px;
    }

    .actions {
        @apply mt-8 flex flex-row justify-end gap-4;
    }
</style>
