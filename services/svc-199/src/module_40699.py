"""Service module 40699: business logic, no crypto."""


def calculate_total_40699(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40699():
    return 'module 40699 handles orders and invoices'
