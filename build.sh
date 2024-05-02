#!/usr/bin/env bash
# exit on error # 出錯時退出
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
