"""Service module 26821: business logic, no crypto."""


def calculate_total_26821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26821():
    return 'module 26821 handles orders and invoices'
