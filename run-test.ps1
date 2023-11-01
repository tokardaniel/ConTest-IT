Write-Host "### run test"

if (!$args[0]) {
    Write-Host "Add meg a feature fajlt. $($MyInvocation.MyCommand.Name) poth/to/featurefile"
    exit(1)
}

docker run -it --rm contestit behave $args[0].replace("\", "/")
