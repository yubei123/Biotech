curl -d '{"username":"test", "password":"123"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:6000/api/user/login
curl -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X GET http://127.0.0.1:6000/api/user/check_token
curl -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X GET http://127.0.0.1:6000/api/menu/menulist
curl -d '{"username":"yubei", "password":"123", "department":"Bioinfo"}' -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X POST http://127.0.0.1:6000/api/user/addUser
curl -d '{"username":"yubei", "password":"456"}' -H "Content-Type: application/json" -H "Authorization: Bearer token_xxx" -X POST http://127.0.0.1:6000/api/user/changePassword
