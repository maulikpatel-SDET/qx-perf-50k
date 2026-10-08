"""Service module 3082: business logic, no crypto."""


def calculate_total_3082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3082():
    return 'module 3082 handles orders and invoices'
