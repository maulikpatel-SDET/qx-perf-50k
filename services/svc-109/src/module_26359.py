"""Service module 26359: business logic, no crypto."""


def calculate_total_26359(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26359():
    return 'module 26359 handles orders and invoices'
