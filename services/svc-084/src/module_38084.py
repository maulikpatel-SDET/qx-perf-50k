"""Service module 38084: business logic, no crypto."""


def calculate_total_38084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38084():
    return 'module 38084 handles orders and invoices'
