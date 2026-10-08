"""Service module 2984: business logic, no crypto."""


def calculate_total_2984(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2984():
    return 'module 2984 handles orders and invoices'
