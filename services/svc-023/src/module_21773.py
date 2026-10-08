"""Service module 21773: business logic, no crypto."""


def calculate_total_21773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21773():
    return 'module 21773 handles orders and invoices'
