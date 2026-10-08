"""Service module 12821: business logic, no crypto."""


def calculate_total_12821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12821():
    return 'module 12821 handles orders and invoices'
