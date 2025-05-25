# Parent Task ID: ROO#TASK_20250525141010_A1B2C3D4
# Parent Task Context: [context.md](/.rooroo/tasks/ROO#TASK_20250525141010_A1B2C3D4/context.md)
# This Sub-task: 4 of 5
# Depends on: Sub-task 3 (DaisyUI/Tailwind Integration - Artifact: FastAPI app with htmy and styled UI)
# Assumed artifact from previous task: FastAPI app serving htmy templates styled with DaisyUI/Tailwind.

## Goal for Expert (rooroo-developer):
Integrate Datastar (`datastar-py` SDK) into the FastAPI application for basic real-time updates via Server-Sent Events (SSE).
- Add `datastar-py` as a project dependency.
- Include the Datastar JavaScript client library in the htmy template (e.g., via CDN or local static file).
- In FastAPI, create a simple Datastar store (e.g., for a counter or a message).
- Create an SSE endpoint using `datastar-py` that allows clients to subscribe to changes in this store.
- On the `index.htmy` page, use Datastar's client-side JavaScript to connect to the SSE endpoint and display a value from the store.
- Implement a mechanism to trigger an update to the store from the backend (e.g., a separate test endpoint that modifies the store's value) to verify that the frontend updates in real-time.