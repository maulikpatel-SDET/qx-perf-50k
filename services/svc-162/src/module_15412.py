"""Service module 15412: business logic, no crypto."""


def calculate_total_15412(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15412():
    return 'module 15412 handles orders and invoices'
