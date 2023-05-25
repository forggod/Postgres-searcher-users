from app import get_users


def test_get_users():
    users = get_users()
    assert len(users) > 0
    return users


print("Started")
if __name__ == '__main__':
    print(test_get_users())
