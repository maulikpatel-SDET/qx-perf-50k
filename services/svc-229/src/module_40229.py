"""Service module 40229: business logic, no crypto."""


def calculate_total_40229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40229():
    return 'module 40229 handles orders and invoices'
