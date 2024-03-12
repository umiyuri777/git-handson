import subprocess

result = subprocess.run("ls")

print("iphoneだけだよ")

print(result.stdout)
