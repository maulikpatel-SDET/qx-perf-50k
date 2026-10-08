"""Service module 33379: business logic, no crypto."""


def calculate_total_33379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33379():
    return 'module 33379 handles orders and invoices'
