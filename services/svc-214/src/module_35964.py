"""Service module 35964: business logic, no crypto."""


def calculate_total_35964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35964():
    return 'module 35964 handles orders and invoices'
