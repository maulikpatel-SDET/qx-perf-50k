"""Service module 15552: business logic, no crypto."""


def calculate_total_15552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15552():
    return 'module 15552 handles orders and invoices'
