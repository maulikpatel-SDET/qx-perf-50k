"""Service module 20924: business logic, no crypto."""


def calculate_total_20924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20924():
    return 'module 20924 handles orders and invoices'
