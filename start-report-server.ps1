Write-Host "### starting report server"

docker run --volume contestit_volume:/dashboard/reports -v contestit_volume:/dashboard/screenshots -d -it --rm -p 9999:9999 dashboard
