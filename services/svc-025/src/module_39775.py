"""Service module 39775: business logic, no crypto."""


def calculate_total_39775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39775():
    return 'module 39775 handles orders and invoices'
