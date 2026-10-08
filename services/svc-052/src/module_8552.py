"""Service module 8552: business logic, no crypto."""


def calculate_total_8552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8552():
    return 'module 8552 handles orders and invoices'
