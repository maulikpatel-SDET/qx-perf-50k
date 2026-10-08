"""Service module 3029: business logic, no crypto."""


def calculate_total_3029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3029():
    return 'module 3029 handles orders and invoices'
