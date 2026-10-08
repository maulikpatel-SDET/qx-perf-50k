"""Service module 42229: business logic, no crypto."""


def calculate_total_42229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42229():
    return 'module 42229 handles orders and invoices'
