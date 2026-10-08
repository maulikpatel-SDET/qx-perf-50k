"""Service module 48821: business logic, no crypto."""


def calculate_total_48821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48821():
    return 'module 48821 handles orders and invoices'
