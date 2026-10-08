"""Service module 20603: business logic, no crypto."""


def calculate_total_20603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20603():
    return 'module 20603 handles orders and invoices'
