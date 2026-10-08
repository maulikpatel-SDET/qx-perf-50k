"""Service module 48440: business logic, no crypto."""


def calculate_total_48440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48440():
    return 'module 48440 handles orders and invoices'
