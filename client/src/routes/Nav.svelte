<script>
    import {
        SideNav,
        SideNavItems,
        SideNavLink,

    } from "carbon-components-svelte"
    import {
        Person,
        MessageQueue,
     } from "carbon-icons-svelte";
    let isSideNavOpen = false;
</script>

<SideNav bind:isOpen={isSideNavOpen} rail>
    <SideNavItems>
        <SideNavLink icon={Person} text="About Me" href="/"/>
        <SideNavLink icon={MessageQueue} text="Contact" href="/contact"/>
    </SideNavItems>
</SideNav>
