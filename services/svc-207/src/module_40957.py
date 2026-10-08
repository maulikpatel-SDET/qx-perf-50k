"""Service module 40957: business logic, no crypto."""


def calculate_total_40957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40957():
    return 'module 40957 handles orders and invoices'
