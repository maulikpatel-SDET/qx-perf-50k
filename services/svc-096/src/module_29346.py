"""Service module 29346: business logic, no crypto."""


def calculate_total_29346(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29346():
    return 'module 29346 handles orders and invoices'
