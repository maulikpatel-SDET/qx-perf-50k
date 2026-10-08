"""Service module 24018: business logic, no crypto."""


def calculate_total_24018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24018():
    return 'module 24018 handles orders and invoices'
