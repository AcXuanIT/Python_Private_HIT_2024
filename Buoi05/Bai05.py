#Tạo một từ điển chứa nội dung file docker-compose sau:
docker_compose = {
    "version": "3.8",
    "services": "app",
    "image": "python:3.10-slim",
    "command": "python app.py",
    "volumes": "./app:/app",
    "restart": "always",
    "ports": "5000:5000",
    "depends_on": "db"
}

#in toàn bộ nội dung của dictionary.
print("Nội dung ban đầu:")
for key, value in docker_compose.items():
    print(f"{key}: {value}")

#Sửa version thành '3.10', in kết quả.
docker_compose["version"] = "3.10"
print("Nội dung Sửa version thành '3.10':")
for key, value in docker_compose.items():
    print(f"{key}: {value}")

#Lấy giá trị của key 'image' và in ra màn hình.
print("Giá trị của key 'image':", docker_compose["image"])

#Thêm key 'environment' với giá trị ['PYTHONUNBUFFERED=1'], in kết quả.
docker_compose["environment"] ="PYTHONUNBUFFERED=1"
for key, value in docker_compose.items():
    print(f"{key}: {value}")

#Kiểm tra xem dictionary có chứa key 'volumes' hay không?
if "volumes" in docker_compose:
    print("volumes in docker_compose")
else:
    print("volumes not in docker_compose")

#Xóa key 'depends_on' khỏi dictionary, in kết quả.
docker_compose.pop("depends_on")
for key, value in docker_compose.items():
    print(f"{key}: {value}")

#Đếm số lượng key trong dictionary.
print(len(docker_compose))

#Tạo một list chứa tất cả các giá trị trong dictionary và in kết quả.
listvalues = [x for x in docker_compose.values()]
print("listvalues : " , listvalues)

#Kiểm tra xem 'always' có phải là giá trị của bất kỳ key nào không?
print("'always' có trong dict:", "always" in listvalues)

#Nhập vào từ bàn phím một key mới và giá trị tương ứng, sau đó thêm vào dictionary và in lại kết quả.
new_key = input("Nhap key : ")
new_value = input("Nhap value: ")
docker_compose[new_key] = new_value
print("Sau khi thêm key mới:")
for key, value in docker_compose.items():
    print(f"{key}: {value}")