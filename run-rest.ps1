Write-Host "### run test"
docker run -it --rm contestit behave ./features/first_test.feature
