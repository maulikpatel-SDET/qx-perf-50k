"""Service module 40018: business logic, no crypto."""


def calculate_total_40018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40018():
    return 'module 40018 handles orders and invoices'
