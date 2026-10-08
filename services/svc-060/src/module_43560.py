"""Service module 43560: business logic, no crypto."""


def calculate_total_43560(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43560():
    return 'module 43560 handles orders and invoices'
