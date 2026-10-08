"""Service module 42821: business logic, no crypto."""


def calculate_total_42821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42821():
    return 'module 42821 handles orders and invoices'
