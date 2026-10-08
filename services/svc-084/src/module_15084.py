"""Service module 15084: business logic, no crypto."""


def calculate_total_15084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15084():
    return 'module 15084 handles orders and invoices'
