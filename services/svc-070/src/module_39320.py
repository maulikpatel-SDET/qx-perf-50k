"""Service module 39320: business logic, no crypto."""


def calculate_total_39320(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39320():
    return 'module 39320 handles orders and invoices'
