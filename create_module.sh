#!/bin/bash
# Script to create a new training module structure

if [ "$#" -ne 2 ]; then
    echo "Usage: ./create_module.sh MODULE_NUMBER MODULE_NAME"
    echo "Example: ./create_module.sh 02 field-data-collection"
    exit 1
fi

MODULE_NUM=$1
MODULE_NAME=$2
MODULE_DIR="modules/${MODULE_NUM}-${MODULE_NAME}"

echo "Creating module structure: ${MODULE_DIR}"

# Create directories
mkdir -p "${MODULE_DIR}"/{lessons,videos,activities,resources,assessment,troubleshooting}
mkdir -p "${MODULE_DIR}/videos/transcripts"
mkdir -p "${MODULE_DIR}/activities/sample-data"
mkdir -p "${MODULE_DIR}/resources/samples"

# Create placeholder README files
cat > "${MODULE_DIR}/README.md" << EOF
# Module ${MODULE_NUM}: ${MODULE_NAME^}

**Duration:** TBD  
**Prerequisites:** Module $(printf "%02d" $((10#$MODULE_NUM - 1)))  

## Overview

[Add module overview here]

## Learning Objectives

[Add learning objectives here]

## Contents

- [Lessons](./lessons/)
- [Videos](./videos/)
- [Activities](./activities/)
- [Resources](./resources/)
- [Assessment](./assessment/)

---

**Last Updated:** $(date +%B\ %Y)
EOF

# Create lesson placeholder
cat > "${MODULE_DIR}/lessons/01-introduction.md" << EOF
# Introduction to ${MODULE_NAME^}

## Overview

[Add lesson content here]
EOF

# Create video index
cat > "${MODULE_DIR}/videos/video-index.md" << EOF
# Module ${MODULE_NUM} Videos

## Available Videos

1. [Module Overview](./00-overview.md)
2. TBD

---

**Last Updated:** $(date +%B\ %Y)
EOF

echo "✓ Module structure created successfully!"
echo "  Edit ${MODULE_DIR}/README.md to add content"