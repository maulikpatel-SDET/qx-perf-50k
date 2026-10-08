"""Service module 7440: business logic, no crypto."""


def calculate_total_7440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7440():
    return 'module 7440 handles orders and invoices'
