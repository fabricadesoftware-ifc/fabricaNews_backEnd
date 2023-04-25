# Endpoints

### `/categories`
- **[GET]** http://localhost:8000/categories/ - lista todos os registros de `categories`.
- **[GET]** http://localhost:8000/categories/{categories_id}/ - lista um registro específico de `categories`.
- **[POST]** http://localhost:8000/categories/add - cria um novo registro em `categories`.
- **[PUT]** http://localhost:8000/categories/{categories_id}/ - altera um registro existente de `categories`.
- **[PATCH]** http://localhost:8000/categories/{categories_id}/ - altera parcialmente um registro existente de `categories`.
- **[DELETE]** http://localhost:8000/categories/{categories_id}/ - remove um registro de `categories`.

### `/user`
- **[GET]** http://localhost:8000/users/ - lista todos os registros de `users`.
- **[GET]** http://localhost:8000/users/{users_id}/ - lista um registro específico de `users`.
- **[POST]** http://localhost:8000/users/add - cria um novo registro em `users`.
- **[PUT]** http://localhost:8000/users/{users_id}/ - altera um registro existente de `users`.
- **[PATCH]** http://localhost:8000/users/{users_id}/ - altera parcialmente um registro existente de `users`.
- **[DELETE]** http://localhost:8000/users/{users_id}/ - remove um registro de `users`.

### `/post`
- **[GET]** http://localhost:8000/post/ - lista todos os registros de `post`.
- **[GET]** http://localhost:8000/post/{post_id}/ - lista um registro específico de `post`.
- **[POST]** http://localhost:8000/post/add  - cria um novo registro em `post`.
- **[PUT]** http://localhost:8000/post/{post_id}/ - altera um registro existente de `post`.
- **[PATCH]** http://localhost:8000/post/{post_id}/ - altera parcialmente um registro existente de `post`.
- **[DELETE]** http://localhost:8000/post/{post_id}/ - remove um registro de `post`.

### `/reactions`
- **[GET]** http://localhost:8000/reactions/ - lista todos os registros de `reactions`.
- **[GET]** http://localhost:8000/reactions/{reactions_id}/ - lista um registro específico de `reactions`.
- **[POST]** http://localhost:8000/reactions/add - cria um novo registro em `reactions`.
- **[PUT]** http://localhost:8000/reactions/{reactions_id}/ - altera um registro existente de `reactions`.
- **[PATCH]** http://localhost:8000/reactions/{reactions_id}/ - altera parcialmente um registro existente de `reactions`.
- **[DELETE]** http://localhost:8000/reactions/{reactions_id}/ - remove um registro de `reactions`.

### `/{post_id}/reactions/`
- **[GET]** http://localhost:8000/{post_id}/reactions/ - lista todos os registros de `reactions` em um registro específico de `/{post_id}/`.
- **[GET]** http://localhost:8000/{post_id}/reactions/{reactions_id}/ - lista um registro específico de `reactions`  em um registro específico de `/{post_id}/`.
- **[POST]** http://localhost:8000/{post_id}/reactions/add - cria um novo registro em `reactions` em um registro específico de `/{post_id}/`.
- **[PUT]** http://localhost:8000/{post_id}/reactions/{reactions_id}/ - altera um registro existente de `reactions` em um registro específico de `/{post_id}/`.
- **[PATCH]** http://localhost:8000/{post_id}/reactions/{reactions_id}/ - altera parcialmente um registro existente de `reactions` em um registro específico de `/{post_id}/`.
- **[DELETE]** http://localhost:8000/{post_id}/reactions/{reactions_id}/ - remove um registro de `reactions` em um registro específico de `/{post_id}/`.

### /post/{user_pub_id}/
- **[GET]** http://localhost:8000/post/{user_pub_id}/
- **[PUT]** http://localhost:8000/post/{user_pub_id}/
- **[PATCH]** http://localhost:8000/post/{user_pub_id}/
- **[DELETE]** http://localhost:8000/post/{user_pub_id}/

### /post/{project_id}/
- **[GET]** http://localhost:8000/post/{project_id}/
- **[PUT]** http://localhost:8000/post/{project_id}/
- **[PATCH]** http://localhost:8000/post/{project_id}/
- **[DELETE]** http://localhost:8000/post/{project_id}/
- **[GET]** http://localhost:8000/post/public/
- **[GET]** http://localhost:8000/post/tags/
- **[GET]** http://localhost:8000/post/{id}/data_pub/ 

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
- **[GET]** http://localhost:8000/save_to_read/user{id}/post{id}/
- **[PUT]** http://localhost:8000/save_to_read{id}/user{id}/post{id}/
- **[PATCH]** http://localhost:8000/save_to_read{id}/user{id}/post{id}/
- **[DELETE]** http://localhost:8000/save_to_{id}/user{id}/post{id}/

### /favorites
- **[GET]** http://localhost:8000/favorites/user{id}/post{id}/
- **[PUT]** http://localhost:8000/favorites{id}/user{id}/post{id}/
- **[PATCH]** http://localhost:8000/favorites{id}/user{id}/post{id}/ 
- **[DELETE]** http://localhost:8000/favorites{id}/user{id}/post{id}/

### /comments
- **[GET]** http://localhost:8000/comments/post{id}/user{id}/
- **[PUT]** http://localhost:8000/comments{id}/post{id}/user{id}/
- **[PATCH]** http://localhost:8000/comments{id}/post{id}/user{id}/
- **[POST]** http://localhost:8000/comments/post{id}/user{id}/
- **[DELETE]** http://localhost:8000/comments{id}/post{id}/user{id}/

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