"""Service module 3229: business logic, no crypto."""


def calculate_total_3229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3229():
    return 'module 3229 handles orders and invoices'
