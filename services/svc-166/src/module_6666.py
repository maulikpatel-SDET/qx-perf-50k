"""Service module 6666: business logic, no crypto."""


def calculate_total_6666(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6666():
    return 'module 6666 handles orders and invoices'
