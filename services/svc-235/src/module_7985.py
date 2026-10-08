"""Service module 7985: business logic, no crypto."""


def calculate_total_7985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7985():
    return 'module 7985 handles orders and invoices'
