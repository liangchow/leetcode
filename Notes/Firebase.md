# Firebase Notes

## Benefits
- Improve SOE by sending pre-rendered code directly to the client
- File system routing
- Automatic code splitting. Reduce websaite load time.
- Extension of React

## Client vs. Server Components
- By default, all components created in Next.js is `server` component. If we want to use `client` side component, add `'use client'` on top. If any React hooks is used, make sure to add `use client`. See [Server and Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)

## Routing Structure
- Routing based on file system: add new folder for a new nested page.js.
