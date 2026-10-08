"""Service module 4985: business logic, no crypto."""


def calculate_total_4985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4985():
    return 'module 4985 handles orders and invoices'
