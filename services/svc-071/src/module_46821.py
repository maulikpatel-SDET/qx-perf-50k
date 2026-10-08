"""Service module 46821: business logic, no crypto."""


def calculate_total_46821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46821():
    return 'module 46821 handles orders and invoices'
