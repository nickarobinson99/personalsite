<svelte:head>
	<title>Contact</title>
	<meta name="description" content="About this app" />
</svelte:head>
<script>
	import {
    Form,
    FormGroup,
    Checkbox,
    RadioButtonGroup,
    RadioButton,
    Select,
    SelectItem,
    Button,
	TextInput,
	TextArea,
	Row,
	Column,
	Grid,
	Content,
  } from "carbon-components-svelte";
</script>
<div class="text-column">
	<Content>
	<h1>Contact Me</h1>
	<div role="doc-subtitle">You can also email me at nick@nickrobinson.site (it all goes to the same place) </div>
	<Form method="POST">
		<FormGroup>
			<Grid>
				<Row>
					<Column>
						<TextInput labelText="Full Name" name="name" type="text"/>
					</Column>
					<Column>
						<TextInput labelText="Email" name="email" type="email"/>
					</Column>
					<Column>
						<TextInput labelText="Organization" name="organization" type="text"/>
					</Column>
				</Row>

				<Row>
					<Column>
						<TextInput labelText="Subject" name="subject" type="text"/>
					</Column>
				</Row>
				<Row>
					<Column>
						<TextArea labelText="Body" name="body" type="text"/>
					</Column>
				</Row>
				<Row>
					<Column>
						<Button type="submit">Submit</Button> 
					</Column>
					<Column>
						<div class="frc-captcha" data-sitekey="FCMKAQ43JP6LTSFR"></div>
					</Column>
				</Row>
			</Grid>
		</FormGroup>
	</Form>
</Content>
</div>
