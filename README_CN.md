# GPyLang - 大语言模型驱动的脚本语言

[中](README_CN.md)/[EN](README.md)

GPyLang是由大语言模型驱动的编程语言，旨在具有类似Python的语法，并具备一些独特功能。GPyLang编译器通过特定规则，将GPyLang代码转化为标准Python代码。

## 语法与关键词

GPyLang紧密类似于Python，但引入了新的关键词以扩展其功能：

- `use`：用于让编辑器实现一个函数（你只需给出清晰的函数名）。例如：`use 删除文件 as delete\ndelete("test.txt")`。

- `gen:[type]`：此关键词用于快速构建变量（包括算法等）。例如：
  - `files = gen:[list(str)]("此目录中的所有文件")`。
  - `nums = gen:[list(int)]("100以下的所有完全平方数")`。

- `chat`：此关键词会将返回值替换为直接询问该问题chatgpt得到的答案。例如：
  ```python
  print(chat("你是谁")) #结果是GPYLang编译器
  ```


## 示例用法

以下是GPyLang编译器应如何行为的示例：
```
用户输入:
print(chat:[bool]("中国是亚洲国家吗？"))
print(gen:[list(int)]("100以内能被2整除的数字"))

编译器输出:
{
    "status": 0,
    "message": "success!",
    "code": "print(True)\nprint([x for i in range(100) if x % 2 == 0])"
}
```

在此示例中，用户输入包含GPyLang代码，编译器提供了一个JSON响应，其中包含翻译后的Python代码和成功消息。

## 安装

要安装GPyLang，请运行以下命令（未实现）：

```
pip install gpylang
```

## 生成和运行您的脚本

注意：以下功能尚未实现。项目目前正在开发中，且由于作者精力有限，进展可能较慢。

将来，要生成和运行您的GPyLang脚本，您可以使用以下命令：

```
gpy filename.gpy -o output.py
```

## 贡献

作为一苦逼国服初中生，能投入的精力少之又少。如果您希望为此项目做出贡献，请考虑提交Pull Request（PR）或创建issue。

感谢您对GPyLang项目的支持。

## 捐赠

此项目目前不接受任何捐赠