"""Service module 25229: business logic, no crypto."""


def calculate_total_25229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25229():
    return 'module 25229 handles orders and invoices'
