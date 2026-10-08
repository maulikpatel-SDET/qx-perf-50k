"""Service module 49855: business logic, no crypto."""


def calculate_total_49855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49855():
    return 'module 49855 handles orders and invoices'
