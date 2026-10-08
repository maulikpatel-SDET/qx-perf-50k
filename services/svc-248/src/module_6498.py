"""Service module 6498: business logic, no crypto."""


def calculate_total_6498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6498():
    return 'module 6498 handles orders and invoices'
