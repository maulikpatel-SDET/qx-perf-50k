"""Service module 17505: business logic, no crypto."""


def calculate_total_17505(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17505():
    return 'module 17505 handles orders and invoices'
