"""Service module 27019: business logic, no crypto."""


def calculate_total_27019(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27019():
    return 'module 27019 handles orders and invoices'
