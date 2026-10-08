"""Service module 39359: business logic, no crypto."""


def calculate_total_39359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39359():
    return 'module 39359 handles orders and invoices'
