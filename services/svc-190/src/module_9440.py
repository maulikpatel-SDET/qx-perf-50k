"""Service module 9440: business logic, no crypto."""


def calculate_total_9440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9440():
    return 'module 9440 handles orders and invoices'
