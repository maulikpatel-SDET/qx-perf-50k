"""Service module 8381: business logic, no crypto."""


def calculate_total_8381(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8381():
    return 'module 8381 handles orders and invoices'
