"""Service module 28088: business logic, no crypto."""


def calculate_total_28088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28088():
    return 'module 28088 handles orders and invoices'
