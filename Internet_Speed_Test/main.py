import speedtest

st = speedtest.Speedtest()
print("Your download speed is",st.download()//10**6, "Mbps")
print("Your upload speed is",st.upload()//10**6, "Mbps")
print("Your ping speed is",int(st.results.ping),"MS")
