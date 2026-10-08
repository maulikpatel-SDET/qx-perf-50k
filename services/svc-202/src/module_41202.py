"""Service module 41202: business logic, no crypto."""


def calculate_total_41202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41202():
    return 'module 41202 handles orders and invoices'
