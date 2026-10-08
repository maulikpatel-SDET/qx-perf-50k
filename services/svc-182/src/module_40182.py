"""Service module 40182: business logic, no crypto."""


def calculate_total_40182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40182():
    return 'module 40182 handles orders and invoices'
