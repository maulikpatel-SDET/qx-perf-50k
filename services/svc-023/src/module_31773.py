"""Service module 31773: business logic, no crypto."""


def calculate_total_31773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31773():
    return 'module 31773 handles orders and invoices'
