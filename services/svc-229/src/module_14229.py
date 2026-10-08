"""Service module 14229: business logic, no crypto."""


def calculate_total_14229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14229():
    return 'module 14229 handles orders and invoices'
