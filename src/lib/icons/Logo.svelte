<svg
    xmlns="http://www.w3.org/2000/svg"
    width="200"
    height="200"
    viewBox="0 0 24 24"
    class="w-full h-full"
>
    <defs>
        <!-- Define the gradient with animated stops -->
        <linearGradient id="animated-gradient" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#4A90E2">
                <animate
                    attributeName="stop-color"
                    values="#4A90E2;#50E3C2;#4A90E2"
                    dur="5s"
                    repeatCount="indefinite"
                />
            </stop>
            <stop offset="100%" stop-color="#50E3C2">
                <animate
                    attributeName="stop-color"
                    values="#50E3C2;#4A90E2;#50E3C2"
                    dur="5s"
                    repeatCount="indefinite"
                />
            </stop>
        </linearGradient>
    </defs>
    <circle
        cx="12"
        cy="12"
        r="10"
        fill="none"
        stroke="url(#animated-gradient)"
        stroke-width="1"
        stroke-linecap="round"
        stroke-linejoin="round"
    ></circle>
    <path
        d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"
        fill="none"
        stroke="url(#animated-gradient)"
        stroke-width="1"
        stroke-linecap="round"
        stroke-linejoin="round"
    ></path>
    <path
        d="M2 12h20"
        fill="none"
        stroke="url(#animated-gradient)"
        stroke-width="1"
        stroke-linecap="round"
        stroke-linejoin="round"
    ></path>
</svg>

<style>
</style>
