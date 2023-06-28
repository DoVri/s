import subprocess

ip_target = input("Masukkan IP target: ")
subprocess.run(["gcloud", "compute", "ssh", ip_target, "--zone", "ZONE", "--command", "sudo shutdown"])
