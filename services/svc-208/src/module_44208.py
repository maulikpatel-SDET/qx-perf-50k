"""Service module 44208: business logic, no crypto."""


def calculate_total_44208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44208():
    return 'module 44208 handles orders and invoices'
