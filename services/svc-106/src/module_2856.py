"""Service module 2856: business logic, no crypto."""


def calculate_total_2856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2856():
    return 'module 2856 handles orders and invoices'
