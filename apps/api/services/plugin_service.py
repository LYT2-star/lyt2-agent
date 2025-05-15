# apps/api/services/plugin_service.py

import os
import zipfile
import shutil

PLUGIN_DIR = "packages/tools/builtin"

def upload_plugin(file):
    filename = file.filename
    if not filename.endswith(".zip"):
        return {"error": "仅支持上传zip插件包"}

    temp_path = os.path.join("/tmp", filename)
    with open(temp_path, "wb") as f:
        f.write(file.file.read())

    with zipfile.ZipFile(temp_path, "r") as zip_ref:
        zip_ref.extractall(PLUGIN_DIR)

    os.remove(temp_path)
    return {"message": f"插件 {filename} 上传并部署成功"}

def list_plugins():
    plugins = []
    for fname in os.listdir(PLUGIN_DIR):
        if fname.endswith(".py"):
            plugins.append({"name": fname, "enabled": True})
    return plugins

def enable_plugin(plugin_name: str):
    return {"message": f"插件 {plugin_name} 已启用（模拟）"}

def disable_plugin(plugin_name: str):
    return {"message": f"插件 {plugin_name} 已禁用（模拟）"}

