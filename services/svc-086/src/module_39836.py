"""Service module 39836: business logic, no crypto."""


def calculate_total_39836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39836():
    return 'module 39836 handles orders and invoices'
