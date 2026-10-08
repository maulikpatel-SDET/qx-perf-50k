"""Service module 40507: business logic, no crypto."""


def calculate_total_40507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40507():
    return 'module 40507 handles orders and invoices'
