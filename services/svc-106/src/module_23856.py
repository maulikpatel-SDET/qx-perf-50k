"""Service module 23856: business logic, no crypto."""


def calculate_total_23856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23856():
    return 'module 23856 handles orders and invoices'
