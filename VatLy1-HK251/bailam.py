import numpy as np
import matplotlib.pyplot as plt

# Nhập giá trị của dòng điện và bán kính
R = float(input("Nhập bán kính vòng điện tròn: R(m) = "))
if R <= 0:
    raise ValueError("Bán kính phải là số dương.")

I = float(input("Nhập vào giá trị của dòng điện: I(A) = "))
if I <= 0:
    raise ValueError("Dòng điện phải là số dương.")

N = 360  # Số đoạn chia nhỏ của vòng tròn
B = np.array([0.0, 0.0, 0.0])
MU_0_OVER_4PI = (4 * np.pi * 10**-7) / (4 * np.pi)  # hằng số μ0/4π trong hệ SI
dtheta = 2 * np.pi / N

for i in range(N):
    theta1 = i * dtheta
    theta2 = (i + 1) * dtheta

    dlx1 = dlx2 = 0  # Xét trên mặt phẳng Ozy nên x=0
    dly1 = R * np.cos(theta1)
    dlz1 = R * np.sin(theta1)
    dly2 = R * np.cos(theta2)
    dlz2 = R * np.sin(theta2)

    dl = np.array([dlx2 - dlx1, dly2 - dly1, dlz2 - dlz1])
    r = -1 / 2 * np.array([dlx1 + dlx2, dly1 + dly2, dlz1 + dlz2])

    # Tính từ trường tại tâm vòng tròn
    # Vì tại tâm nên r = R
    B += MU_0_OVER_4PI * (I * np.cross(dl, r) / R**3)

print("----Kết quả tại tâm vòng tròn----")
print("Vector từ trường B là: B =", B)
print("Độ lớn từ trường |B| =", np.linalg.norm(B))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

t = np.linspace(0, 2 * np.pi, N)
x_circle = 0
y_circle = R * np.sin(t)
z_circle = R * np.cos(t)
ax.plot3D(x_circle, y_circle, z_circle, label="Vòng điện tròn", color="blue")

# Vẽ vector từ trường tại tâm vòng tròn
ax.quiver(
    0,
    0,
    0,
    B[0],
    B[1],
    B[2],
    color="red",
    label="Vector từ trường B",
)

xlimit = np.linalg.norm(B) * 1.5
ax.set_xlim([-xlimit, xlimit])

ax.set_xlabel("X (A)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Từ trường tại tâm vòng điện tròn")
ax.legend()

plt.show()
