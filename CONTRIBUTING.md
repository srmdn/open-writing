# Contributing

Thanks for contributing to `open-translation`.

Read the [contributor guide](./docs/contributors/README.md) before changing a
skill. It explains skill boundaries, evaluation expectations, model
assumptions, and the public/private workspace split.

## Before opening a pull request

- Keep the change focused on one reusable problem.
- Explain the evidence behind the change and why it belongs in the selected
  skill.
- Mention sibling-skill overlap, terminology tradeoffs, and format constraints.
- Keep project-specific preferences out of public guidance unless
  representative cases show that the pattern recurs.
- Do not commit files from `.local/`.
- Run the public skill validator:

  ```shell
  python3 .github/validate-skills.py
  ```

See [project decisions](./DECISIONS.md) before changing public scope or skill
architecture. For usage guidance, see the
[end-user documentation](./docs/end-users/README.md).
