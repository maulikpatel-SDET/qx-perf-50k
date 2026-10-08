"""Service module 10773: business logic, no crypto."""


def calculate_total_10773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10773():
    return 'module 10773 handles orders and invoices'
