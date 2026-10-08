"""Service module 4964: business logic, no crypto."""


def calculate_total_4964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4964():
    return 'module 4964 handles orders and invoices'
