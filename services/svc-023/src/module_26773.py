"""Service module 26773: business logic, no crypto."""


def calculate_total_26773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26773():
    return 'module 26773 handles orders and invoices'
