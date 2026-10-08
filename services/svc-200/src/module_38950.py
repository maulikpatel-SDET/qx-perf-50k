"""Service module 38950: business logic, no crypto."""


def calculate_total_38950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38950():
    return 'module 38950 handles orders and invoices'
