curl -d '{"username":"test", "password":"123"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8502/api/user/login
curl -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X GET http://127.0.0.1:8502/api/user/check_token
curl -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X GET http://127.0.0.1:8502/api/menu/menulist
curl -d '{"username":"yubei", "password":"123", "department":"Bioinfo"}' -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X POST http://127.0.0.1:8502/api/user/addUser
curl -d '{"username":"yubei", "password":"456"}' -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X POST http://127.0.0.1:8502/api/user/changePassword
curl -F "file=@/work/users/beitai/backend/Biotech/config.py" -H "Content-Type: multipart/form-data" -H "Authorization: Bearer token_xxx" -X POST http://127.0.0.1:8502/api/sample/uploadfile
