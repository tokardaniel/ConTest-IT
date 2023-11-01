Write-Host "### build image"

docker buildx build . --tag contestit 
