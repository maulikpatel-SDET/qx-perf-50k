"""Service module 8669: business logic, no crypto."""


def calculate_total_8669(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8669():
    return 'module 8669 handles orders and invoices'
