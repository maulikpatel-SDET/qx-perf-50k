"""Service module 39229: business logic, no crypto."""


def calculate_total_39229(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39229():
    return 'module 39229 handles orders and invoices'
