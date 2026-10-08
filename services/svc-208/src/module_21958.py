"""Service module 21958: business logic, no crypto."""


def calculate_total_21958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21958():
    return 'module 21958 handles orders and invoices'
