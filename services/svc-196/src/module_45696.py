"""Service module 45696: business logic, no crypto."""


def calculate_total_45696(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45696():
    return 'module 45696 handles orders and invoices'
