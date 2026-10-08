"""Service module 48773: business logic, no crypto."""


def calculate_total_48773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48773():
    return 'module 48773 handles orders and invoices'
