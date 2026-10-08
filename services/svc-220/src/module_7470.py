"""Service module 7470: business logic, no crypto."""


def calculate_total_7470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7470():
    return 'module 7470 handles orders and invoices'
