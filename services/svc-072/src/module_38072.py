"""Service module 38072: business logic, no crypto."""


def calculate_total_38072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38072():
    return 'module 38072 handles orders and invoices'
