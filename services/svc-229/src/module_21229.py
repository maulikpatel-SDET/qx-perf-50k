"""Service module 21229: business logic, no crypto."""


def calculate_total_21229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21229():
    return 'module 21229 handles orders and invoices'
