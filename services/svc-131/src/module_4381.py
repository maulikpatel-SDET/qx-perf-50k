"""Service module 4381: business logic, no crypto."""


def calculate_total_4381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4381():
    return 'module 4381 handles orders and invoices'
