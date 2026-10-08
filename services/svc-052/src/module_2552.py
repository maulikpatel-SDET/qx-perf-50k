"""Service module 2552: business logic, no crypto."""


def calculate_total_2552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2552():
    return 'module 2552 handles orders and invoices'
