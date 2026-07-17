@echo off
REM AIOS Pro 一键打包（Windows 双击即用）
REM 前提: 已安装 Python（python.org 下载，安装时勾选 "Add Python to PATH"）
cd /d "%~dp0.."
python automation\scripts\build_bundle.py --all
echo.
echo 打包完成，文件在 dist\ 文件夹。
pause
