"""Service module 14967: business logic, no crypto."""


def calculate_total_14967(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14967():
    return 'module 14967 handles orders and invoices'
