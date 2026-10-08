"""Service module 34855: business logic, no crypto."""


def calculate_total_34855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34855():
    return 'module 34855 handles orders and invoices'
