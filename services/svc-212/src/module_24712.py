"""Service module 24712: business logic, no crypto."""


def calculate_total_24712(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24712():
    return 'module 24712 handles orders and invoices'
