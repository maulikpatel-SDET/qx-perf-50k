"""Service module 2018: business logic, no crypto."""


def calculate_total_2018(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2018():
    return 'module 2018 handles orders and invoices'
