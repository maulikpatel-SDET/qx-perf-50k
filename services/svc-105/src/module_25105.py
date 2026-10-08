"""Service module 25105: business logic, no crypto."""


def calculate_total_25105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25105():
    return 'module 25105 handles orders and invoices'
