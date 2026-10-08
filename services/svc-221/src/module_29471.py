"""Service module 29471: business logic, no crypto."""


def calculate_total_29471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29471():
    return 'module 29471 handles orders and invoices'
