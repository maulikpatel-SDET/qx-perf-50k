"""Service module 42419: business logic, no crypto."""


def calculate_total_42419(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42419():
    return 'module 42419 handles orders and invoices'
