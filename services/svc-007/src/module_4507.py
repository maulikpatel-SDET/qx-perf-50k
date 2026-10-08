"""Service module 4507: business logic, no crypto."""


def calculate_total_4507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4507():
    return 'module 4507 handles orders and invoices'
