"""Service module 49229: business logic, no crypto."""


def calculate_total_49229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49229():
    return 'module 49229 handles orders and invoices'
