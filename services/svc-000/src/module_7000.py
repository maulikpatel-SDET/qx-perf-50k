"""Service module 7000: business logic, no crypto."""


def calculate_total_7000(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7000():
    return 'module 7000 handles orders and invoices'
