"""Service module 24985: business logic, no crypto."""


def calculate_total_24985(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24985():
    return 'module 24985 handles orders and invoices'
