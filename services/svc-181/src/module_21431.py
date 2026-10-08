"""Service module 21431: business logic, no crypto."""


def calculate_total_21431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21431():
    return 'module 21431 handles orders and invoices'
