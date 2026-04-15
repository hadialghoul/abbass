# Design System Specification: Executive Precision

## 1. Overview & Creative North Star: "The Digital Architect"
This design system is engineered to function as the "Operating System for Reliable Spaces." It rejects the cluttered, reactive aesthetic of traditional maintenance software in favor of a proactive, high-fidelity experience. 

**The Creative North Star: The Digital Architect.**
Imagine the precision of a Tesla cockpit combined with the editorial breathing room of an Apple product launch. We break the "standard template" look by utilizing heavy typographic weighting, intentional asymmetry, and "The Void"—using our Deep Navy (`primary_container`) not just as a background, but as a structural element that allows high-contrast data and glass-morphic components to "float" with executive authority.

---

## 2. Colors & Surface Architecture
Our palette is rooted in deep obsidian tones and electric accents. The goal is to feel "always on" and high-voltage yet sophisticated.

### Tonal Hierarchy
*   **The Void (Primary Foundation):** `primary_container` (#0A0F1C) is the canvas. Use this for the deepest layers of the UI.
*   **The Pulse (Accent):** `secondary_container` (#0055EA) and `secondary` (#B5C4FF) drive the "tech-enabled" energy. Use these for high-intent actions and active states.
*   **The Alert (Urgency):** `tertiary_container` (#250400) and `on_tertiary_container` (#E1420A) are reserved strictly for critical failures or urgent dispatches.

### The "No-Line" Rule
**Explicit Instruction:** Prohibit the use of 1px solid borders for sectioning. 
Structure must be defined through **Background Color Shifts**. To separate a sidebar from a main feed, transition from `surface_container_lowest` to `surface`. This creates a seamless, "milled from a single block" feel characteristic of premium hardware.

### The Glass & Gradient Rule
To move beyond "flat" design, implement glassmorphism for all floating overlays (modals, dropdowns, navigation bars).
*   **Glass Recipe:** `surface_container_highest` at 70% opacity + 20px Backdrop Blur.
*   **Signature Gradients:** Use a subtle radial gradient on primary CTAs: `on_secondary_fixed_variant` (#003CAC) to `secondary_container` (#0055EA). This creates a "glow" that feels powered by electricity.

---

## 3. Typography: The Editorial Voice
We pair the technical precision of **Space Grotesk** (Headings) with the Swiss-inspired clarity of **Inter** (Body).

*   **Display & Headlines (Space Grotesk):** These are your "Architectural Statements." Use `display-lg` (3.5rem) with tight letter-spacing (-0.02em) for hero metrics and executive summaries. It should feel bold, geometric, and immutable.
*   **Body & Titles (Inter):** Used for data density and reliability. `body-md` (0.875rem) is the workhorse for technical specs.
*   **Hierarchy as Authority:** Use extreme scale contrast. A `display-sm` headline next to a `label-sm` creates a sophisticated, data-rich environment that feels like a command center.

---

## 4. Elevation & Depth: Tonal Layering
Traditional shadows are too "organic" for this system. We use **Tonal Layering** to convey z-index.

*   **The Layering Principle:** 
    *   **Level 0 (Base):** `surface_container_lowest`
    *   **Level 1 (Cards):** `surface_container_low`
    *   **Level 2 (Active/Hover):** `surface_container_high`
*   **Ambient Shadows:** For floating elements, use a 32px blur, 0px offset, at 8% opacity using the `on_background` color. This mimics the soft ambient glow of a high-end monitor in a dark room.
*   **The "Ghost Border" Fallback:** If a boundary is legally or functionally required, use `outline_variant` (#46464C) at **15% opacity**. It should be felt, not seen.

---

## 5. Components: Precision Primitives

### Buttons: The "Power" State
*   **Primary:** High-gloss gradient (`secondary_container` to `on_secondary_fixed_variant`). Corner radius: `md` (0.375rem). No border. On hover: Add an external 4px glow using `secondary`.
*   **Secondary:** Ghost style. `outline_variant` at 20% opacity. Text in `on_surface`.
*   **Tertiary:** Text only. `label-md` uppercase with 0.05em tracking.

### Cards & Lists: The "Fluid Grid"
*   **Forbid Dividers:** Do not use lines between list items. Use 12px of vertical padding (`spacing-md`) and a subtle hover shift to `surface_container_highest`.
*   **Nesting:** Place `surface_container_high` cards inside a `surface_container_low` section to create natural focus.

### Input Fields: The "Terminal" Look
*   **Default:** `surface_container_lowest` background, `outline_variant` ghost border (10% opacity).
*   **Focus:** Border transitions to `secondary` (#B5C4FF) with a 2px outer "aura" glow. Label moves to `label-sm` in `secondary` color.

### Signature Component: The "Status Pulse"
For PrimeFix, real-time reliability is key. Use a 12px circle with a `secondary` fill and a CSS animation of a scaling, 10% opacity ring to indicate "Active System Monitoring."

---

## 6. Do's and Don'ts

### Do:
*   **Embrace Asymmetry:** Align high-level stats to the far right while keeping navigation on the left. This breaks the "Wordpress" feel.
*   **Use High-Contrast Scaling:** Make your big numbers *really* big (`display-lg`) and your labels *really* small (`label-sm`).
*   **Color for Intent:** Only use Urgency Orange (`on_tertiary_container`) when human intervention is required.

### Don't:
*   **No Pure Black:** Never use #000000. Always use the Deep Navy `primary_container` (#0A0F1C) to maintain "visual soul."
*   **No Round Pebbles:** Avoid `full` (pill) radius for functional buttons. Stick to `md` (0.375rem) to maintain a "sharp, engineered" persona.
*   **No Clutter:** If a piece of information isn't vital for executive decision-making, hide it in a "Technical Specs" glassmorphic drawer.