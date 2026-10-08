"""Service module 4506: business logic, no crypto."""


def calculate_total_4506(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4506():
    return 'module 4506 handles orders and invoices'
