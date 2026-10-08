"""Service module 40082: business logic, no crypto."""


def calculate_total_40082(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40082():
    return 'module 40082 handles orders and invoices'
