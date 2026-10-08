"""Service module 45740: business logic, no crypto."""


def calculate_total_45740(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45740():
    return 'module 45740 handles orders and invoices'
