# Endpoints

### `/categories/`
- **[GET]** http://localhost:8000/categories/ - lista todos os registros de `categories`.
- **[GET]** http://localhost:8000/categories/{id}/ - lista um registro específico de `categories`.
- **[POST]** http://localhost:8000/categories/ - cria um novo registro em `categories`.
- **[PUT]** http://localhost:8000/categories/{id}/ - altera um registro existente de `categories`.
- **[PATCH]** http://localhost:8000/categories/{id}/ - altera parcialmente um registro existente de `categories`.
- **[DELETE]** http://localhost:8000/categories/{id}/ - remove um registro de `categories`.

### `/users/`
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

### `/reactions/`
- **[GET]** http://localhost:8000/reactions/ - lista todos os registros de `reactions`.
- **[GET]** http://localhost:8000/reactions/{id}/ - lista um registro específico de `reactions`.
- **[POST]** http://localhost:8000/reactions/ - cria um novo registro em `reactions`.
- **[PUT]** http://localhost:8000/reactions/{id}/ - altera um registro existente de `reactions`.
- **[PATCH]** http://localhost:8000/reactions/{id}/ - altera parcialmente um registro existente de `reactions`.
- **[DELETE]** http://localhost:8000/reactions/{id}/ - remove um registro de `reactions`.

    ### `/news/{id}/reactions/`**
    - **[GET]** http://localhost:8000/news/{id}/reactions/ - lista todos os registros de `reactions` em um registro específico de `/{post_id}/`.
    - **[GET]** http://localhost:8000/news/{id}/reactions/{id}/ - lista um registro específico de `reactions`  em um registro específico de `/{post_id}/`.
    - **[POST]** http://localhost:8000/news/{id}/reactions/ - cria um novo registro em `reactions` em um registro específico de `/{post_id}/`.
    - **[PUT]** http://localhost:8000/news/{id}/reactions/{id}/ - altera um registro existente de `reactions` em um registro específico de `/{post_id}/`.
    - **[PATCH]** http://localhost:8000/news/{id}/reactions/{id}/ - altera parcialmente um registro existente de `reactions` em um registro específico de `/{post_id}/`.
    - **[DELETE]** http://localhost:8000/news/{id}/reactions/{id}/ - remove um registro de `reactions` em um registro específico de `/{post_id}/`.

### `/savetoread/`
- **[GET]** http://localhost:8000/savetoread/ - lista todos os registros de `savetoread`.
- **[DELETE]** http://localhost:8000/savetoread/news/{id}/ - remove um registro de `savetoread`.

    ### `/news/{id}/savetoread/`
    - **[POST]** http://localhost:8000/news/{id}/savetoread/ - cria um novo registro em `savetoread` em um registro específico de `/news/{id}/`.
    - **[PUT]** http://localhost:8000/news/{id}/savetoread/{id} - altera um registro existente de `savetoread` em um registro específico de `/news/{id}/`.
    - **[DELETE]** http://localhost:8000/news/{id}/savetoread/{id} - remove um registro de `savetoread` em um registro específico de `/news/{id}/`.

    ### `/projects/{id}/savetoread/`
    - **[POST]** http://localhost:8000/projects/{id}/savetoread/ - cria um novo registro em `savetoread` em um registro específico de `/projects/{id}/`.
    - **[PUT]** http://localhost:8000/projects/{id}/savetoread/{id} - altera um registro existente de `savetoread` em um registro específico de `/projects/{id}/`.
    - **[DELETE]** http://localhost:8000/projects/{id}/savetoread/{id} - remove um registro de `savetoread` em um registro específico de `/projects/{id}/`.

    
### `/favorites/{id}/users/`
- **[GET]** http://localhost:8000/favorites/{id}/users/ - lista todos os registros de `favorites` em um registro específico de `/favorites/{id}/`.

### `/news/{id}/favorites/`
- **[GET]** http://localhost:8000/news/{id}/favorites/ - lista todos os registros de `favorites` em um registro específico de `/news/{id}/`.
- **[PUT]** http://localhost:8000/news/{id}/favorites/{id}/ - altera um registro existente de `favorites` em um registro específico de `/news/{id}/`.
- **[DELETE]** http://locahost:8000/news/{id}/favorites/{id}/ - remove um registro de `favorites` em um registro específico de `/news/{id}/`.

### `/projects/{id}/favorites/`**
- **[GET]** http://localhost:8000/projects/{id}/favorites/ - lista todos os registros de `favorites` em um registro específico de `/projects/{id}/`.
- **[PUT]** http://localhost:8000/projects/{id}/favorites/{id}/ - altera um registro existente de `favorites` em um registro específico de `/projects/{id}/`.
- **[DELETE]** http://locahost:8000/projects/{id}/favorites/{id}/ - remove um registro de `favorites` em um registro específico de `/projects/{id}/`.           

### `/news/{id}/comments/`
- **[GET]** http://localhost:8000/news/{id}/comments/ - lista todos os registros de `comments`.
- **[GET]** http://localhost:8000/news/{id}/comments/{id}/ - lista um registro específico de `comments`.
- **[PUT]** http://localhost:8000/news/{id}/comments/{id}/ - altera um registro existente de `comments`.
- **[PATCH]** http://localhost:8000/news/{id}/comments/{id}/ - altera parcialmente um registro existente de `comments`.
- **[DELETE]** http://locahost:8000/news/{id}/comments/{id}/ - remove um registro de `comments`.

### `/projects/{id}/comments/`
- **[GET]** http://localhost:8000/projects/{id}/comments/ - lista todos os registros de `comments`.
- **[GET]** http://localhost:8000/projects/{id}/comments/{id}/ - lista um registro específico de `comments`.
- **[PUT]** http://localhost:8000/projects/{id}/comments/{id}/ - altera um registro existente de `comments`.
- **[PATCH]** http://localhost:8000/projects/{id}/comments/{id}/ - altera parcialmente um registro existente de `comments`.
- **[DELETE]** http://locahost:8000/projects/{id}/comments/{id}/ - remove um registro de `comments`.

<!-- ### /user_category_follow
- **[GET]** http://localhost:8000/user_category_follow/user{id}/category{id}/
- **[PUT]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/
- **[PATCH]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/
- **[DELETE]** http://localhost:8000/user_category_follow{id}/user{id}/category{id}/ -->


<!-- ### /user_project_follow
- **[GET]** http://localhost:8000/user_project_follow/user{id}/project{id}/
- **[PUT]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/
- **[PATCH]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/
- **[DELETE]** http://localhost:8000/user_project_follow{id}/user{id}/project{id}/ -->
