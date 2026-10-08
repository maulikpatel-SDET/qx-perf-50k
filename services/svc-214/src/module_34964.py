"""Service module 34964: business logic, no crypto."""


def calculate_total_34964(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34964():
    return 'module 34964 handles orders and invoices'
