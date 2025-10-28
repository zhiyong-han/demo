import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb  # 需安装：pip install ttkbootstrap

# 初始化 bootstrap 主题（先创建 Tk，再把主题应用到该 root）
root = tk.Tk()
style = ttkb.Style(master=root, theme="pulse")  # 可替换为其他主题如 "litera"、"pulse"
root.title("修复下拉框三角形位置")

# 1. 自定义 Combobox 样式，调整箭头位置
style = ttkb.Style()

# 重新定义 Combobox 下拉箭头的布局
style.layout(
    "Custom.TCombobox",
    [
        ("Combobox.field", {
            "children": [
                ("Combobox.downarrow", {  # 下拉箭头区域
                    "side": "right",       # 靠右显示
                    "sticky": "ns",        # 垂直方向居中（关键）
                    "padding": (0, 2, 2, 2)  # 微调内边距（上右下左）
                }),
                ("Combobox.padding", {
                    "children": [
                        ("Combobox.textarea", {"sticky": "nswe"})  # 文本区域
                    ],
                    "sticky": "nswe"
                })
            ],
            "sticky": "nswe",
            "borderwidth": 1
        })
    ]
)

# 2. 创建使用自定义样式的下拉框
ttkb.Label(root, text="项目:").pack(side="left", padx=5, pady=10)
project_cb = ttkb.Combobox(
    root,
    values=["项目1", "项目2", "项目3"],
    style="Custom.TCombobox",  # 应用自定义样式
    width=20
)
project_cb.pack(side="left", padx=5, pady=10)

root.mainloop()