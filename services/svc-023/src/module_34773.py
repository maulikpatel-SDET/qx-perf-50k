"""Service module 34773: business logic, no crypto."""


def calculate_total_34773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34773():
    return 'module 34773 handles orders and invoices'
