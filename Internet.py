import speedtest
test= speedtest.Speedtest()
down = test.download()
upload = test.upload()
print(f"Download speed:{down}")
print(f"Upload Speed:{upload}")
