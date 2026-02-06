# .github Repository

This repository manages shared profile content and repository-level governance files.

## Purpose

- Hosts the organization/profile landing page content
- Stores profile assets used by that page
- Keeps contribution and licensing documents in one place

## Repository Layout

```text
.github
|- profile/
|  |- README.md
|  `- assets/
|     |- logos/
|     `- wordcloud/
|- CONTRIBUTING.md
|- LICENSE
`- NOTICE
```

## Primary Entry Point

The main public profile content is in:

- `profile/README.md`

Supporting image assets referenced by the profile README are under:

- `profile/assets/logos/`
- `profile/assets/wordcloud/`

## Editing Guidelines

- Use complete absolute links for external references.
- Keep markdown tables readable on GitHub desktop and mobile views.
- Keep badge labels consistent across sections.
- Avoid placeholder links and verify every outbound URL after edits.

## Local Review Checklist

1. Open `profile/README.md` and validate section flow.
2. Confirm image paths resolve correctly from GitHub markdown context.
3. Confirm all outbound links are complete and reachable.
4. Confirm no formatting regressions in tables, badges, or details blocks.

## License

Licensed under Apache License 2.0. See `LICENSE`.
