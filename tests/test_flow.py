def test_signup_then_unregister_flow(client):
    # Arrange
    activity = "Drama Club"
    email = "flow.student@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    unregister_response = client.delete(f"/activities/{activity}/participants", params={"email": email})
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert unregister_response.status_code == 200
    participants = activities_response.json()[activity]["participants"]
    assert email not in participants


def test_can_signup_same_email_to_different_activities(client):
    # Arrange
    email = "multi.activity@mergington.edu"

    # Act
    chess_response = client.post("/activities/Chess Club/signup", params={"email": email})
    science_response = client.post("/activities/Science Club/signup", params={"email": email})
    activities_response = client.get("/activities")

    # Assert
    assert chess_response.status_code == 200
    assert science_response.status_code == 200
    data = activities_response.json()
    assert email in data["Chess Club"]["participants"]
    assert email in data["Science Club"]["participants"]
