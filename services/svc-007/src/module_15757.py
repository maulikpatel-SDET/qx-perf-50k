"""Service module 15757: business logic, no crypto."""


def calculate_total_15757(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15757():
    return 'module 15757 handles orders and invoices'
