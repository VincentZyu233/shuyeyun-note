# 设置基础文本
base_text = "qwqqwqqwqqwqqwq"
static_lines = ["'&e" + base_text + "'"] * 6  # 保持开头和结尾的静态行
dynamic_lines = []
colors = ["&e", "&6"]

# 生成动态变化的文本
for i in range(len(base_text)):
    part1 = base_text[:i]
    part2 = base_text[i:i+1]
    part3 = base_text[i+1:]
    color = colors[i % len(colors)]
    if part2:  # 避免空字符的情况
        # dynamic_lines.append(f"'- &e{part1}{color}{part2}&e{part3}'")
        dynamic_lines.append(f"'&e{part1}{color}{part2}&e{part3}'")
        

# 拼接最终内容
output_lines = static_lines + dynamic_lines + static_lines

# 添加到配置文件格式
final_output = "  texts:\n" + "\n".join(f"  - {line}" for line in output_lines)

# 将生成的内容保存到文件
with open("animated_config.yaml", "w", encoding="utf-8") as file:
    file.write(final_output)

print("配置文件已生成到 animated_config.yaml")
