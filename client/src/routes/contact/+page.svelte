<svelte:head>
	<title>Contact</title>
	<meta name="description" content="About this app" />
</svelte:head>

<div class="text-column">
	<form method="POST">
		<label>
			Full name
			<input name="name", type="text">
		</label>
		<label>
			Email
			<input name="email", type="email">
		</label>
		<label>
			Organization
			<input name="organization", type="text">
		</label>
		<label>
			Subject
			<input name="subject", type="text">
		</label>
		<label>
			Body
			<input name="body", type="text">
		</label>
		<div class="frc-captcha" data-sitekey="FCMKAQ43JP6LTSFR"></div>
		<button>Submit</button>
	</form>
</div>
