export const API_URL = 'http://localhost:8000'
const TOKEN = window.localStorage.getItem('token')

export const LOGIN_USER = (body) => {

    return {
        url: API_URL + "/login/",
        options: {
            method: "post",
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify(body)
        }
    }
}

export const TOKEN_VALIDATE_POST = (token) => {

    return {
        url: API_URL + "/jwt-auth/v1/token/validate",
        options: {
            method: "post",
            headers: {
                Authorization: "Bearer " + token
            }
        }
    }
}

export const GET_USER = () => {

    return {
        url: API_URL + "/users/getuser",
        options: {
            method: "get",
            headers: {
                Authorization: "Bearer " + TOKEN
            }
        }
    }
}

export const GET_TAGS = (token) => {

    return {
        url: API_URL + "/tags/",
        options: {
            method: "get",
            // headers: {
            //     Authorization: "Bearer " + token
            // }
        }
    }
}

export const GET_ARTICLES = (skip, limit) => {

    return {
        url: API_URL + `/articles?skip=${skip}&limit=${limit}`,
        options: {
            method: "get",
            headers: {
                Authorization: "Bearer " + TOKEN
            }
        }
    }
}

export const GET_COMMENTS = (articleId) => {

    return {
        url: API_URL + `/articles/${articleId}/comments`,
        options: {
            method: "get",
            headers: {
                Authorization: "Bearer " + TOKEN
            }
        }
    }
}

export const POST_COMMENT = (articleId, body) => {

    return {
        url: API_URL + `/articles/${articleId}/comments`,
        options: {
            method: "post",
            headers: {
                Authorization: "Bearer " + TOKEN,
                'Content-Type': "application/json"
            },
            body: JSON.stringify(body)
        }
    }
}

export const DELETE_COMMENT = (commentId) => {

    return {
        url: API_URL + `/comments/${commentId}`,
        options: {
            method: "delete",
            headers: {
                Authorization: "Bearer " + TOKEN,
                'Content-Type': "application/json"
            },
            // body: JSON.stringify(body)
        }
    }
}

export const POST_ARTICLE = (body) => {

    return {
        url: API_URL + `/articles/`,
        options: {
            method: "post",
            headers: {
                Authorization: "Bearer " + TOKEN,
                'Content-Type': "application/json"
            },
            body: JSON.stringify(body)
        }
    }
}

export const UPDATE_ARTICLE = (articleId, body) => {

    return {
        url: API_URL + `/articles/${articleId}`,
        options: {
            method: "put",
            headers: {
                Authorization: "Bearer " + TOKEN,
                'Content-Type': "application/json"
            },
            body: JSON.stringify(body)
        }
    }
}





