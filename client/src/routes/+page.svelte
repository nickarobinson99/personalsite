<script>
	import LogoLinkedin from "carbon-icons-svelte/lib/LogoLinkedin.svelte";
	import LogoGithub from "carbon-icons-svelte/lib/LogoGithub.svelte";
	import Email from "carbon-icons-svelte/lib/Email.svelte";

	let hoverIconColor = 'grey';
	let defaultIconColor = 'white';
	function handleIconMouseOver(e) {
		let element = e.target;
		element.setAttribute("fill", hoverIconColor)
	}

	function handleIconMouseOut(e) {
		let element = e.target;
		element.setAttribute("fill", defaultIconColor)
	}
</script>

<svelte:head>
	<title>Nicholas Robinson</title>
	<meta name="Personal website for Nicholas Robinson" content="Created with svelte" />
</svelte:head>

<section>
	<h1>
		Nicholas Robinson
	</h1>
	<div role="doc-subtitle">
		Software Engineer
		<div class='social-icons'>
			<!-- svelte-ignore a11y-mouse-events-have-key-events -->
			<a on:mouseover={handleIconMouseOver} on:mouseout={handleIconMouseOut} href="https://www.linkedin.com/in/nick-robinson-37412b35/">
				<LogoLinkedin fill={defaultIconColor} size={24}/>
			</a>
			<!-- svelte-ignore a11y-mouse-events-have-key-events -->
			<a on:mouseover={handleIconMouseOver} on:mouseout={handleIconMouseOut} href="https://github.com/nickarobinson99/personalsite">
				<LogoGithub fill={defaultIconColor} size={24}/>
			</a>
			<!-- svelte-ignore a11y-mouse-events-have-key-events -->
			<a on:mouseover={handleIconMouseOver} on:mouseout={handleIconMouseOut} href="mailto:nick@nickrobinson.site">
				<Email fill={defaultIconColor} size={24}/>
			</a>
			
		</div>
	</div>


</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
	[role="doc-subtitle"] {
		width: 100%;
	}
	.social-icons {
		width: 100%;
		margin-top: 0.2rem;
	}
</style>
