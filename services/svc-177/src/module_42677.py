"""Service module 42677: business logic, no crypto."""


def calculate_total_42677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42677():
    return 'module 42677 handles orders and invoices'
