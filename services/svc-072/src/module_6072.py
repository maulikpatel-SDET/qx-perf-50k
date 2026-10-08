"""Service module 6072: business logic, no crypto."""


def calculate_total_6072(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6072():
    return 'module 6072 handles orders and invoices'
