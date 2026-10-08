"""Service module 856: business logic, no crypto."""


def calculate_total_856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_856():
    return 'module 856 handles orders and invoices'
