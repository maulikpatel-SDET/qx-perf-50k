"""Service module 23964: business logic, no crypto."""


def calculate_total_23964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23964():
    return 'module 23964 handles orders and invoices'
