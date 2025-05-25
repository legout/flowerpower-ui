# Parent Task ID: ROO#TASK_20250525141010_A1B2C3D4
# Parent Task Context: [context.md](/.rooroo/tasks/ROO#TASK_20250525141010_A1B2C3D4/context.md)
# This Sub-task: 5 of 5
# Depends on: Sub-task 4 (Datastar Integration - Artifact: FastAPI app with basic Datastar SSE setup)
# Assumed artifact from previous task: FastAPI app with htmy, DaisyUI, and a working Datastar SSE connection displaying a store value.

## Goal for Expert (rooroo-developer):
Create a simple, interactive demonstration of the real-time update functionality using all integrated technologies.
- On the `index.htmy` page (styled with DaisyUI):
    - Display a value from the Datastar store (e.g., a counter, initially 0).
    - Add a button (styled with DaisyUI).
- When the button is clicked:
    - It should trigger a FastAPI endpoint (e.g., using an HTMX POST request or a simple JavaScript fetch).
    - This FastAPI endpoint should update the value in the Datastar store (e.g., increment the counter).
- The change in the Datastar store should be automatically reflected on the `index.htmy` page via the existing SSE connection without a full page reload.
- Ensure the interaction is smooth and clearly demonstrates the real-time update.