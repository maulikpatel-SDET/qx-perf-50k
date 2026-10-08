"""Service module 3552: business logic, no crypto."""


def calculate_total_3552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3552():
    return 'module 3552 handles orders and invoices'
