"""Service module 36950: business logic, no crypto."""


def calculate_total_36950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36950():
    return 'module 36950 handles orders and invoices'
