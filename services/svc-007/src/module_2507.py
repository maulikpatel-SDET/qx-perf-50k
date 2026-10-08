"""Service module 2507: business logic, no crypto."""


def calculate_total_2507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2507():
    return 'module 2507 handles orders and invoices'
