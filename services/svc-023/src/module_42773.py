"""Service module 42773: business logic, no crypto."""


def calculate_total_42773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42773():
    return 'module 42773 handles orders and invoices'
