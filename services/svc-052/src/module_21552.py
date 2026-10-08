"""Service module 21552: business logic, no crypto."""


def calculate_total_21552(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21552():
    return 'module 21552 handles orders and invoices'
