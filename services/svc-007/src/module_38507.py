"""Service module 38507: business logic, no crypto."""


def calculate_total_38507(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38507():
    return 'module 38507 handles orders and invoices'
