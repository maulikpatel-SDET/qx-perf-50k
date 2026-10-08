"""Service module 18874: business logic, no crypto."""


def calculate_total_18874(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18874():
    return 'module 18874 handles orders and invoices'
