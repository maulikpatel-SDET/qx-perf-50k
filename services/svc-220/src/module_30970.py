"""Service module 30970: business logic, no crypto."""


def calculate_total_30970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30970():
    return 'module 30970 handles orders and invoices'
