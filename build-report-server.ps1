Write-host "### Building report server"

docker buildx build -f .\Dockerfile_reports . --tag=dashboard
