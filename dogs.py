import requests
import pytest

base_url = "https://dog.ceo/api/"

@pytest.mark.parametrize("breed", ["beagle", "boxer", "dalmatian"])
def test_get_all_breeds(breed):
    response = requests.get(f"base_urlbreeds/list/all")
    data = response.json()
    assert response.status_code == 200
    assert breed in data["message"]

def test_get_random_dog_image():
    response = requests.get(f"base_urlbreeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

@pytest.mark.parametrize("breed", ["labrador", "spitz", "bulldog"])
def test_get_breed_image(breed):
    response = requests.get(f"base_urlbreed/breed/images/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

@pytest.mark.parametrize("breed", ["chihuahua", "husky", "dachshund"])
def test_get_subbreeds(breed):
    response = requests.get(f"base_urlbreed/breed/list")
    data = response.json()
    assert response.status_code == 200
    assert breed in data["message"]

def test_get_random_dog_info():
    response = requests.get(f"base_urlbreeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

    breed = data["message"].split("/")[-2]
    response_breed = requests.get(f"base_urlbreed/breed/list")
    data_breed = response_breed.json()
    assert response_breed.status_code == 200
    assert breed in data_breed["message"]
