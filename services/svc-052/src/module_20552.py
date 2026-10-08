"""Service module 20552: business logic, no crypto."""


def calculate_total_20552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20552():
    return 'module 20552 handles orders and invoices'
