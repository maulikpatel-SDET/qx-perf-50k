"""Service module 3202: business logic, no crypto."""


def calculate_total_3202(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3202():
    return 'module 3202 handles orders and invoices'
