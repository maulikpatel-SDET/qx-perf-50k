"""Service module 855: business logic, no crypto."""


def calculate_total_855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_855():
    return 'module 855 handles orders and invoices'
