"""Service module 36470: business logic, no crypto."""


def calculate_total_36470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36470():
    return 'module 36470 handles orders and invoices'
