"""Service module 2084: business logic, no crypto."""


def calculate_total_2084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2084():
    return 'module 2084 handles orders and invoices'
