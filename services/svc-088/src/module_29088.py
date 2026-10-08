"""Service module 29088: business logic, no crypto."""


def calculate_total_29088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29088():
    return 'module 29088 handles orders and invoices'
