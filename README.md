# Astral Documentation (Offline)

This repository provides a solution for running the Astral toolchain documentation offline. It includes the pre-built static site for: [Ruff](https://github.com/astral-sh/ruff), [uv](https://github.com/astral-sh/uv), and [ty](https://github.com/astral-sh/ty).

## Running Offline

### Using Docker

1.  Build the image:
    ```bash
    docker build -t astral-docs .
    ```
2.  Run the container:
    ```bash
    docker run -d -p 8080:8080 astral-docs
    ```
3.  Open [http://localhost:8080](http://localhost:8080)

### Using Python

1.  Run the server:
    ```bash
    python -m http.server 8000 --directory site
    ```
2.  Open [http://localhost:8000](http://localhost:8000)

## License

uv is licensed under either of

- Apache License, Version 2.0, ([LICENSE-APACHE](LICENSE-APACHE) or https://www.apache.org/licenses/LICENSE-2.0)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or https://opensource.org/licenses/MIT)

at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in uv by you, as defined in the Apache-2.0 license, shall be
dually licensed as above, without any additional terms or conditions.

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/uv/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
