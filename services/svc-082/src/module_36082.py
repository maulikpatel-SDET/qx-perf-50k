"""Service module 36082: business logic, no crypto."""


def calculate_total_36082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36082():
    return 'module 36082 handles orders and invoices'
