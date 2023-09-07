
#!/bin/bash

# Function to run npm run dev inside static_vite folder
function run_npm_dev {
  echo "Running npm run dev in static_vite folder..."
  cd static_vite
  npm run dev
}

# Function to run docker compose up inside .ci/staging/ folder
function run_docker_compose {
  echo "Running docker compose up in .ci/staging/ folder..."
  cd .ci/staging/
  docker-compose up
}

# Run functions in parallel
run_npm_dev & run_docker_compose &

# Wait for all background processes to finish
wait
echo "Both commands have finished executing."