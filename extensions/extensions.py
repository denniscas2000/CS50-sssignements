gif = ("image/gif")
jpg = ("image/jpeg")
jpeg = ("image/jpeg")
png = ("image/png")
pdf = ("application/pdf")
txt = ("text/plain")
zip = ("application/zip")

file = input(" File name: ").lower().strip()

if file.endswith("gif"):
    print(gif)
elif file.endswith("jpg"):
    print(jpg)
elif file.endswith("jpeg"):
    print(jpeg)
elif file.endswith("png"):
    print(png)
elif file.endswith("pdf"):
    print(pdf)
elif file.endswith("txt"):
    print(txt)
elif file.endswith("zip"):
    print(zip)
else:
    print("application/octet-stream")