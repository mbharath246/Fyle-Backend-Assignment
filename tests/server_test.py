def test_server(client):
    response = client.get()

    assert response.status_code == 200
def test_invalid_endpoint(client, h_principal):
    response = client.get("/invalid", headers=h_principal)
    assert response.status_code == 404

