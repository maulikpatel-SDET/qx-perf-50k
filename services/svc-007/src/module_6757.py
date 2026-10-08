"""Service module 6757: business logic, no crypto."""


def calculate_total_6757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6757():
    return 'module 6757 handles orders and invoices'
