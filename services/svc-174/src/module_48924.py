"""Service module 48924: business logic, no crypto."""


def calculate_total_48924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48924():
    return 'module 48924 handles orders and invoices'
