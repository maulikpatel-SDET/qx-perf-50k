"""Service module 44257: business logic, no crypto."""


def calculate_total_44257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44257():
    return 'module 44257 handles orders and invoices'
