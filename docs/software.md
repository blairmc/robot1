
#### 3. docs/software.md – update vision section

```markdown
## Vision System – Current Progress

- USB camera connected to development machine (Mac Mini)
- OpenCV (`opencv-python`) successfully installed in local environment
- Initial scripts tested for camera discovery and frame capture
- GUI functions (`imshow`, `waitKey`) working locally (using full OpenCV package)
- Headless mode (`opencv-python-headless`) previously used in Codespaces – no longer needed locally

**Next steps:**
- Identify correct camera index (often 0, 1, or higher on macOS)
- Implement live preview loop with quit key
- Save sample images for algorithm development