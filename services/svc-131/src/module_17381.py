"""Service module 17381: business logic, no crypto."""


def calculate_total_17381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17381():
    return 'module 17381 handles orders and invoices'
