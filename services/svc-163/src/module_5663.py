"""Service module 5663: business logic, no crypto."""


def calculate_total_5663(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5663():
    return 'module 5663 handles orders and invoices'
