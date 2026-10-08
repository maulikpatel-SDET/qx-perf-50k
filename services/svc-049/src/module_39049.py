"""Service module 39049: business logic, no crypto."""


def calculate_total_39049(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39049():
    return 'module 39049 handles orders and invoices'
