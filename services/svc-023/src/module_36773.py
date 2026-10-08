"""Service module 36773: business logic, no crypto."""


def calculate_total_36773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36773():
    return 'module 36773 handles orders and invoices'
