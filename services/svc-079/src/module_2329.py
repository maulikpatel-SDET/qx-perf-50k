"""Service module 2329: business logic, no crypto."""


def calculate_total_2329(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2329():
    return 'module 2329 handles orders and invoices'
