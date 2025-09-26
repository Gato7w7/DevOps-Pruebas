import json
from src.api import app

def test_suma_endpoint():
    with app.test_client() as client:
        response = client.post('/suma', 
                             json={'a': 7, 'b': 3},
                             content_type='application/json')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['resultado'] == 10

def test_historial_endpoint():
    with app.test_client() as client:
        # Hacer una suma primero
        client.post('/suma', json={'a': 2, 'b': 4})
        
        # Obtener historial
        response = client.get('/historial')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['historial']) > 0