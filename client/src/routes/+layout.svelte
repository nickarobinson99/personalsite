<script>
	import Header from './Header.svelte';
	import Nav from './Nav.svelte';
	import "carbon-components-svelte/css/g90.css";
	import UnderConstruction from './UnderConstruction.svelte';
	const env = import.meta.env.MODE;
</script>

<div class="app">
	{#if env=='development'}
	<Nav/>
	<main>
		<slot />
	</main>
	{/if}
	{#if env=='production'}
	<UnderConstruction/>
	{/if}
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}
</style>
