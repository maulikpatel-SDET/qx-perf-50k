"""Service module 39272: business logic, no crypto."""


def calculate_total_39272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39272():
    return 'module 39272 handles orders and invoices'
