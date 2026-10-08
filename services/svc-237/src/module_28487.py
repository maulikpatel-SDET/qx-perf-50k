"""Service module 28487: business logic, no crypto."""


def calculate_total_28487(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28487():
    return 'module 28487 handles orders and invoices'
