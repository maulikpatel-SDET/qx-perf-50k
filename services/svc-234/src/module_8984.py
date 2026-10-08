"""Service module 8984: business logic, no crypto."""


def calculate_total_8984(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8984():
    return 'module 8984 handles orders and invoices'
