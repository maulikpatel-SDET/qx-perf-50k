"""Service module 7229: business logic, no crypto."""


def calculate_total_7229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7229():
    return 'module 7229 handles orders and invoices'
