# Next.js Notes

## Benefits
- Improve SOE by sending pre-rendered code directly to the client
- File system routing
- Automatic code splitting. Reduce websaite load time.
- Extension of React

## Client vs. Server Components
- By default, all components created in Next.js is `server` component. If we want to use `client` side component, add `'use client'` on top. If any React hooks is used, make sure to add `use client`. See [Server and Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components)

## Routing Structure
- Routing based on file system: add new folder for a new nested page.js.

```
app
|-- api\users
|   |-- route.js        // API endpoint: first approach
|-- posts
|   |-- [postId]        // Dynamic postID
|   |   |--page.js
|   |-- new
|   |   |-- error.js
|   |   |-- loading.js
|   |   |-- layout.js   
|	|	|-- page.js     // localhost:3000/posts/new
|   |-- page.js         // localhost:3000/posts
|-- global.css
|-- layout.js
|-- page.js              // localhost:3000
```
## Data Fetching

Next.js provides three choices for data fetching.

- **`Server Side Rendering (SSR)`**: Fetch fresh on each request.
- **`Static Site Generation (SSG)`**: By default, Next.js use SSG. Automatically fetch data but also cache it. It is ideal for content that doesn't change frequently like blog post, documentation, or marketing pages. 
- **`Incremental Static Generation (ISG)`**: It combines SSR and SSG for dynamic static sites with `next: {revalidate: 10}` for revalidation after a specific time frame.

## API Endpoints

Next.js simplifies backend development like those in Express.js. The first approach is to create a folder route `api\users` in the app directory. The second approach is to create a direct route handle within the app directory itself with a new file `route.js`. These two cannot interfer. "They" recommend the first approach to distinguish between front-end and back-end applications with the folder naming convention.

```
// Next.js supports the following HTTP methods:

1. **GET**: Retrieve data or resources from the server.
2. **POST**: Submit data to the server to create a new resources.
3. **PUT**: Update of replace an existing resource on the server.
4. **PATCH**: Partially update an existing resource on the server.
5. **DELETE**: Remove a specific resource from the server.
6. **HEAD**: Retrieve the headers of a resource without fetching its body.
7. **OPTIONS**: Retrieve the supported HTTP methods and other communication options for a resource.


// Example: api\users > route.js
// http://localhost:3000/api/users

export async function GET(request){
    // Handle GET request for /api/users
    // Retrieve users from the database or any data source
    const users = [
        {id: 1, name: 'John'},
        {id: 2, name: 'Jane'},
        {id: 3, name: 'Bob'}
    ]

    // Send the users as a response
    return new Response('JSON.stringify(users)')
}
```
## SEO and Metadata
Next.js let you define Metadata in two ways: static and dynamic.

```
// Static

export const metadata = {
    title: 'Home',
}

// Output:
// <head>
//      <title>Home</title>
// <head>
```
```
// Dynamic

export async function generateMetadata({ params, searchParams }){
    const product = await.getProduct(params, id)
    return { title: product.title }
}

// Output:
// <head>
//      <title>My Unique Product</title>
// <head>
```






