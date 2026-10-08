"""Service module 17202: business logic, no crypto."""


def calculate_total_17202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17202():
    return 'module 17202 handles orders and invoices'
