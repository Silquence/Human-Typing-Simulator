import subprocess

result = subprocess.run(
    [
        "osascript",
        "-e",
        'button returned of (display dialog "Pause?" buttons {"No", "Yes"} default button "Yes")'
    ],
    capture_output=True,
    text=True
)

print("stdout:", result.stdout)
print("stderr:", result.stderr)

choice = result.stdout.strip()

if choice == "Yes":
    print("Paused")
else:
    print("Continue")