"""Service module 49773: business logic, no crypto."""


def calculate_total_49773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49773():
    return 'module 49773 handles orders and invoices'
