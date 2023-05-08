for f in files/*.in; do
    [ -f "$f" ] || break
    python -m _run -i "$f"
done