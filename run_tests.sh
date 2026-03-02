
source venv/Scripts/activate

python -m pytest tests/test_app.py --headless

RESULT=$?

if [ $RESULT -eq 0 ]; then
    echo "Tests Passed!"
    exit 0
else
    echo "Tests Failed with exit code $RESULT"
    exit 1
fi