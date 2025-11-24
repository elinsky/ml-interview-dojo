#!/bin/bash
# Quick stats viewer - run this anytime for a status update

cd "$(dirname "$0")/.." || exit

echo "ML Interview Dojo - Quick Stats"
echo "=================================="
echo ""

python3 srs.py stats

echo ""
echo "💡 Commands:"
echo "  python3 srs.py review    - Start review session"
echo "  python3 srs.py stats     - View stats"
echo "  ./scripts/quick-stats.sh - This screen"