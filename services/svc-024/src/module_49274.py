"""Service module 49274: business logic, no crypto."""


def calculate_total_49274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49274():
    return 'module 49274 handles orders and invoices'
