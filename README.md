# autoscan-test
Đây là thực mục project Python hướng dẫn cài đặt các công cụ cần thiết thực hiện autoscan

## Cài đặt

```bash
pip install -r requirements.txt
pre-commit install
```

Các thư viện sử dụng bao gồm:

  1. Isort : Sắp xếp lại thứ tự import (file config: isort.cfg)
  2. Black : Sửa các lỗi convention cơ bản (file config: pyproject.toml)
  3. Flake8 : Tự động kiểm tra convention (file config: .flake8)
  4. Pre-commit: Tự động chạy các phần mềm trên trước khi thực hiện commit (file config: .pre-commit-config.yaml)

## Sử dụng

Sau khi cài đặt mỗi khi tiền hành commit code, precommit sẽ tự động check các file đã chỉnh sửa. Nếu không có lỗi commit sẽ được báo hoàn thành, ngược lại nếu có lỗi, người lập trình cần sửa các lỗi đó và tiến hành commit lại
