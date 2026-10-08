"""Service module 47773: business logic, no crypto."""


def calculate_total_47773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47773():
    return 'module 47773 handles orders and invoices'
