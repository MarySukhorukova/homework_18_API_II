from pytest_voluptuous import S
from schemas.user import register_user, login_user, create_user


def test_register_user(reqres):

    email = "eve.holt@reqres.in"
    password = "pistol"

    response = reqres.post("/api/register",
                             json={
                                 "email": email,
                                 "password": password
                             })

    assert response.status_code == 200
    assert S(register_user) == response.json()
    assert len(response.json()['token']) == 17


def test_login_user(reqres):

    email = "eve.holt@reqres.in"
    password = "cityslicka"

    response = reqres.post("/api/login",
                             json={
                                 "email": email,
                                 "password": password
                             })

    assert response.status_code == 200
    assert S(login_user) == response.json()
    assert len(response.json()['token']) == 17


def test_create_user(reqres):

    name = "harry potter"
    job = "wizard"

    response = reqres.post("/api/users",
                             json={
                                 "name": name,
                                 "job": job
                             })

    assert response.status_code == 201
    assert S(create_user) == response.json()
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_register_unsuccessful_user(reqres):

    email = "eve.holt@reqres.in"

    response = reqres.post("/api/register",
                             json={
                                 "email": email
                             })

    assert response.status_code == 400
    assert response.json()['error'] == "Missing password"


def test_update_user(reqres):

    name = "harry potter"
    job = "wizard"

    response = reqres.put("/api/users/2",
                             json={
                                 "name": name,
                                 "job": job
                             })

    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job