def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9
    for _, details in data.items():
        assert expected_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)


def test_get_activities_counts_match_participant_lists(client):
    # Arrange
    response = client.get("/activities")

    # Act
    data = response.json()

    # Assert
    for _, details in data.items():
        assert details["max_participants"] >= len(details["participants"])
