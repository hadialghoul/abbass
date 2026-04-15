# Design System Strategy: PrimeFix USA

## 1. Overview & Creative North Star
**The Creative North Star: "The Technical Authority"**

To design for 'PrimeFix USA' is to balance the surgical precision of high-end hardware with the frictionless digital elegance of modern FinTech. We are moving beyond the "utility app" aesthetic to create a **High-End Editorial** experience. 

The system rejects the cluttered, line-heavy interfaces of traditional service brands. Instead, we embrace **The Technical Authority**: a philosophy where confidence is expressed through massive typographic scale, aggressive whitespace, and a "layered glass" depth model. We break the standard template look by utilizing intentional asymmetry—placing oversized headlines against meticulously organized, high-density data grids.

---

## 2. Colors & Surface Philosophy
The palette is rooted in 'Deep Midnight' for authority, energized by 'Electric Blue' for action. However, the premium feel is executed through how these colors *interact*, not just their hex codes.

### The "No-Line" Rule
**Explicit Instruction:** Traditional 1px solid borders are strictly prohibited for sectioning or containment. Boundaries must be defined exclusively through background color shifts.
*   **The Technique:** Place a `surface-container-low` (#f2f4f6) card against a `surface` (#f7f9fb) background. The subtle 2% shift in tonal value creates a sophisticated boundary that feels discovered rather than forced.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of materials. 
*   **Level 0 (Base):** `surface` (#f7f9fb) – The canvas.
*   **Level 1 (Sub-sections):** `surface-container-low` (#f2f4f6) – For grouping related content blocks.
*   **Level 2 (Interactive Elements):** `surface-container-lowest` (#ffffff) – Used for primary cards and input fields to make them "pop" against the light gray base.

### The "Glass & Gradient" Rule
To mimic the premium finish of high-end hardware:
*   **Hero Elements:** Use a subtle linear gradient for primary backgrounds, transitioning from `primary` (#000000 / Deep Midnight) to `primary-container` (#131b2e). This adds "soul" and prevents the flat, "dead" look of pure black/navy.
*   **Floating Navigation:** Utilize Glassmorphism. Apply `surface` at 80% opacity with a `20px` backdrop-blur. This ensures the UI feels integrated into the environment rather than pasted on top.

---

## 3. Typography
We use **Inter** as our typographic engine. The system relies on a "High-Contrast" scale where the gap between headlines and body text is intentionally dramatic to establish an editorial hierarchy.

*   **Display-LG (3.5rem):** Reserved for Hero value propositions. Tracking should be set to `-0.02em` to create a "tight," professional locked-in look.
*   **Headline-MD (1.75rem):** Used for section starts. Combined with generous top-padding, these act as visual anchors.
*   **Body-LG (1.0rem):** Our workhorse. Ensure a line-height of `1.6` to maintain the "Stripe-esque" breathing room.
*   **Label-SM (0.6875rem):** Always Uppercase with `+0.05em` letter spacing. Use `on-surface-variant` (#45464d) for metadata and overlines to provide an authoritative, technical feel.

---

## 4. Elevation & Depth
We eschew "Material" style drop shadows in favor of **Ambient Tonal Layering**.

*   **The Layering Principle:** Use the `surface-container` tiers to create lift. A `surface-container-highest` element placed on a `surface` background creates a natural recession.
*   **Ambient Shadows:** Where physical separation is required (e.g., a floating Modal), use an "Air-Shadow." 
    *   *Spec:* `Y: 20px, Blur: 40px, Color: rgba(25, 28, 30, 0.06)`. This mimics natural light diffusion.
*   **The "Ghost Border":** If accessibility requires a stroke (e.g., in high-contrast modes), use `outline-variant` (#c6c6cd) at **15% opacity**. It should be felt, not seen.
*   **Corner Radii:** Apply `DEFAULT` (0.5rem / 8px) for small components (buttons, chips) and `lg` (1.0rem / 16px) for major containers. This creates a "nested" curvature logic.

---

## 5. Components

### Buttons: The Kinetic Drivers
*   **Primary:** Background: `secondary` (#0058be / Electric Blue). Text: `on-secondary` (#ffffff). Shape: `0.5rem`. Use a subtle inner-glow (1px white at 10% opacity) on the top edge to create a "premium hardware" button feel.
*   **Secondary:** Background: `transparent`. Border: `Ghost Border` (15% opacity outline). Text: `secondary`.
*   **Tertiary:** Text only, `primary` color, with a `label-md` weight.

### Cards & Lists: The No-Line Content
*   **Cards:** Forbid divider lines. Use `1.5rem` (xl) spacing between items. 
*   **Lists:** Separate list items using a `surface-container-high` background on hover, rather than a line between rows.

### Inputs: The Precision Fields
*   **State:** Background should be `surface-container-lowest` (#ffffff). 
*   **Focus:** A 2px `secondary` (#0058be) outer ring with a 4px blur. This makes the active field feel "energized."

### Signature Component: The "Service Status" Chip
*   A custom component using `tertiary-container` with a pulsing `secondary` dot. This reinforces the "Fix" aspect of the brand with a technical, real-time aesthetic.

---

## 6. Do’s and Don’ts

### Do:
*   **Do** use asymmetrical margins. For example, a headline may have a 15% left-offset while the body text remains centered, creating a sophisticated editorial layout.
*   **Do** prioritize vertical whitespace. If a section feels "almost right," add 24px more padding.
*   **Do** use `on-surface-variant` for helper text to keep the visual noise low.

### Don't:
*   **Don't** use pure black (#000000) for text. Use `on-background` (#191c1e) to maintain a soft, premium feel.
*   **Don't** use 100% opaque borders. They create "visual cages" that break the flow of the clean grid.
*   **Don't** use standard icons. Use thick-stroke (2pt), rounded-cap icons that match the `8px` radius of the buttons.