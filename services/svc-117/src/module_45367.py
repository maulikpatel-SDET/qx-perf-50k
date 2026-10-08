"""Service module 45367: business logic, no crypto."""


def calculate_total_45367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45367():
    return 'module 45367 handles orders and invoices'
