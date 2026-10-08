"""Service module 13821: business logic, no crypto."""


def calculate_total_13821(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13821():
    return 'module 13821 handles orders and invoices'
