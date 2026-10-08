"""Service module 19757: business logic, no crypto."""


def calculate_total_19757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19757():
    return 'module 19757 handles orders and invoices'
