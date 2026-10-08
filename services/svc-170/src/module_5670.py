"""Service module 5670: business logic, no crypto."""


def calculate_total_5670(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5670():
    return 'module 5670 handles orders and invoices'
