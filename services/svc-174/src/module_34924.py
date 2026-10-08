"""Service module 34924: business logic, no crypto."""


def calculate_total_34924(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34924():
    return 'module 34924 handles orders and invoices'
