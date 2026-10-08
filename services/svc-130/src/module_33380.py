"""Service module 33380: business logic, no crypto."""


def calculate_total_33380(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33380():
    return 'module 33380 handles orders and invoices'
