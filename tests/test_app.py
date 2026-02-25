def test_get_activities(client):
    # Arrange: (No setup needed)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0


def test_signup_success(client):
    # Arrange
    activity = next(iter(client.get("/activities").json().keys()))
    email = "testuser@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json().get("message", "")


def test_signup_duplicate(client):
    # Arrange
    activity = next(iter(client.get("/activities").json().keys()))
    email = "duplicate@mergington.edu"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json().get("detail", "")
