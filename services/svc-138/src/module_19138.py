"""Service module 19138: business logic, no crypto."""


def calculate_total_19138(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19138():
    return 'module 19138 handles orders and invoices'
