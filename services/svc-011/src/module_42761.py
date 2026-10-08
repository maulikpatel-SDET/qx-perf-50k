"""Service module 42761: business logic, no crypto."""


def calculate_total_42761(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42761():
    return 'module 42761 handles orders and invoices'
