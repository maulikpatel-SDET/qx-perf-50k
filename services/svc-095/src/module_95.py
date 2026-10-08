"""Service module 95: business logic, no crypto."""


def calculate_total_95(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_95():
    return 'module 95 handles orders and invoices'
