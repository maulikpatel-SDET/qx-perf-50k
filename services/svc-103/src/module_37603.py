"""Service module 37603: business logic, no crypto."""


def calculate_total_37603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37603():
    return 'module 37603 handles orders and invoices'
