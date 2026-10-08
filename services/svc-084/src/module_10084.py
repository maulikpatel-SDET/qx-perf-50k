"""Service module 10084: business logic, no crypto."""


def calculate_total_10084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10084():
    return 'module 10084 handles orders and invoices'
