"""Service module 30919: business logic, no crypto."""


def calculate_total_30919(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30919():
    return 'module 30919 handles orders and invoices'
