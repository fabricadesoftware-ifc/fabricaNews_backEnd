# Endpoints

### `/categories`
- **[GET]** http://localhost:8000/categories/ - lista todos os registros de `categories`.
- **[GET]** http://localhost:8000/categories/{id}/ - lista um registro específico de `categories`.
- **[POST]** http://localhost:8000/categories/ - cria um novo registro em `categories`.
- **[PUT]** http://localhost:8000/categories/{id}/ - altera um registro existente de `categories`.
- **[PATCH]** http://localhost:8000/categories/{id}/ - altera parcialmente um registro existente de `categories`.
- **[DELETE]** http://localhost:8000/categories/{id}/ - remove um registro de `categories`.

### /user
- **[GET]** http://localhost:8000/users/ - retorna todos os usuários registrados.
- **[GET]** http://localhost:8000/users/{id}/ - retorna os detalhes de um usuário específico.
- **[POST]** http://localhost:8000/users/ - cria um novo usuário
- **[PUT]** http://localhost:8000/users/{id}/ - atualiza as informações de um usuário específico.
- **[PATCH]** http://localhost:8000/users/{id}/ - atualiza parcialmente as informações de um usuário específico.
- **[DELETE]** http://localhost:8000/users/{id}/ - remove um usuário específico.

### /newsfeel
- **[GET]** http://localhost:8000/newsfeel/ - retorna todas as entradas registradas.
- **[GET]** http://localhost:8000/newsfeel/{id}/ - retorna os detalhes de uma entrada específica.
- **[POST]** http://localhost:8000/newsfeel/ - cria uma nova entrada.
- **[PUT]** http://localhost:8000/newsfeel/{id}/ - atualiza as informações de uma entrada específica.
- **[PATCH]** http://localhost:8000/newsfeel/{id}/ - atualiza parcialmente as informações de uma entrada específica.
- **[DELETE]** http://localhost:8000/newsfeel/{id}/ - remove uma entrada específica.

### /newsfeel/{news_id}/
- **[GET]** http://localhost:8000/newsfeel/{news_id}/
- **[PUT]** http://localhost:8000/newsfeel/{news_id}/
- **[PATCH]** http://localhost:8000/newsfeel/{news_id}/
- **[DELETE]** http://localhost:8000/newsfeel/{news_id}/

### /newsfeel/{user_id}/
- **[GET]** http://localhost:8000/newsfeel/{users_id}/
- **[PUT]** http://localhost:8000/newsfeel/{users_id}/
- **[PATCH]** http://localhost:8000/newsfeel/{users_id}/
- **[DELETE]** http://localhost:8000/newsfeel/{users_id}/

### /feeling *
- **[GET]** http://localhost:8000/feelings/ - retorna todos os feelings registrados.
- **[GET]** http://localhost:8000/feelings/{id}/ - retorna os detalhes de um feeling específico.
- **[POST]** http://localhost:8000/feelings/ - cria um novo feeling.
- **[PUT]** http://localhost:8000/feelings/{id}/ - atualiza as informações de um feeling específico.
- **[PATCH]** http://localhost:8000/feelings/{id}/ - atualiza parcialmente as informações de um feeling específico.
- **[DELETE]** http://localhost:8000/feelings/{id}/ - remove um feeling específico.

### /news *
- **[GET]** http://localhost:8000/news/ - retorna todas as news registradas.
- **[GET]** http://localhost:8000/news/{id}/ - retorna os detalhes de uma news específica.
- **[POST]** http://localhost:8000/news/  - cria uma nova news.
- **[PUT]** http://localhost:8000/news/{id}/ - atualiza as informações de uma news específica.
- **[PATCH]** http://localhost:8000/news/{id}/ - atualiza parcialmente as informações de uma news específica.
- **[DELETE]** http://localhost:8000/news/{id}/ - remove uma news específica.

### /news/{category_id}/
- **[GET]** http://localhost:8000/news/{category_id}/ 
- **[PUT]** http://localhost:8000/news/{category_id}/
- **[PATCH]** http://localhost:8000/news/{category_id}/
- **[DELETE]** http://localhost:8000/news/{category_id}/

### /news/{user_pub_id}/
- **[GET]** http://localhost:8000/news/{user_pub_id}/
- **[PUT]** http://localhost:8000/news/{user_pub_id}/
- **[PATCH]** http://localhost:8000/news/{user_pub_id}/
- **[DELETE]** http://localhost:8000/news/{user_pub_id}/

### /news/{project_id}/
- **[GET]** http://localhost:8000/news/{project_id}/
- **[PUT]** http://localhost:8000/news/{project_id}/
- **[PATCH]** http://localhost:8000/news/{project_id}/
- **[DELETE]** http://localhost:8000/news/{project_id}/
- **[GET]** http://localhost:8000/news/public/
- **[GET]** http://localhost:8000/news/tags/
- **[GET]** http://localhost:8000/news/{id}/data_pub/ 

### /project
- **[GET]** http://localhost:8000/projects/ - retorna todos os projects registrados.
- **[GET]** http://localhost:8000/projects/{id}/ - retorna um project específico.
- **[PUT]** http://localhost:8000/projects/{id}/ - atualiza as informações de um project específico.
- **[PATCH]** http://localhost:8000/projects/{id}/  - atualiza parcialmente as informações de um project específico.
- **[DELETE]** http://localhost:8000/projects/{id}/ - remove um project específico.
- **[GET]** http://localhost:8000/projects/{supervisor_id}/
- **[PUT]** http://localhost:8000/projects/{supervisor_id}/
- **[PATCH]** http://localhost:8000/projects/{supervisor_id}/
- **[DELETE]** http://localhost:8000/projects/{supervisor_id}/

### /save_to_read
- **[GET]** http://localhost:8000/save_to_read/user{id}/news{id}/
- **[PUT]** http://localhost:8000/save_to_read{id}/user{id}/news{id}/
- **[PATCH]** http://localhost:8000/save_to_read{id}/user{id}/news{id}/
- **[DELETE]** http://localhost:8000/save_to_{id}/user{id}/news{id}/

### /favorites
- **[GET]** http://localhost:8000/favorites/user{id}/news{id}/
- **[PUT]** http://localhost:8000/favorites{id}/user{id}/news{id}/
- **[PATCH]** http://localhost:8000/favorites{id}/user{id}/news{id}/ 
- **[DELETE]** http://localhost:8000/favorites{id}/user{id}/news{id}/

### /comments
- **[GET]** http://localhost:8000/comments/news{id}/user{id}/
- **[PUT]** http://localhost:8000/comments{id}/news{id}/user{id}/
- **[PATCH]** http://localhost:8000/comments{id}/news{id}/user{id}/
- **[POST]** http://localhost:8000/comments/news{id}/user{id}/
- **[DELETE]** http://localhost:8000/comments{id}/news{id}/user{id}/

### /user_notifications
- **[GET]** http://localhost:8000/user_notifications/user{id}/category{id}/project{id}/
- **[PUT]** http://localhost:8000/user_notifications{id}/user{id}/category{id}/project/{id}/
- **[PATCH]** http://localhost:8000/user_notifications{id}/user{id}/category{id}/project{id}/
- **[DELETE]** http://localhost:8000/user_notifications{id}/user{id}/category{id}/project{id}/

### /user_category_follow
- **[GET]** http://localhost:8000/user_category_follow/user{id}/category{id}/
- **[PUT]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/
- **[PATCH]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/
- **[DELETE]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/

### /user_project_follow
- **[GET]** http://localhost:8000/user_project_follow/user{id}/project{id}/
- **[PUT]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/
- **[PATCH]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/
- **[DELETE]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/