"""Service module 12924: business logic, no crypto."""


def calculate_total_12924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12924():
    return 'module 12924 handles orders and invoices'
