"""Service module 17985: business logic, no crypto."""


def calculate_total_17985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17985():
    return 'module 17985 handles orders and invoices'
