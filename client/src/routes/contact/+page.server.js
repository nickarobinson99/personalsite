export const actions = {
    default: async ({cookies, request}) => {
        let data = await request.formData();
        let output = new Object();
        output['organization'] = data.get('organization')
        output['name'] = data.get('name');
        output['email'] = data.get('email');
        output['subject'] = data.get('subject');
        output['body'] = data.get('body');
        output['frc_captcha_solution'] = data.get('frc-captcha-solution'); 
        
        const response = await postEmail(output);
    }
}

async function postEmail (data) {
    console.log(JSON.stringify(data))
    const res = await fetch('https://personalsite-gnqgnymh4q-ue.a.run.app/contact_form', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    const response = await res.json()
    return JSON.stringify(response)
}
