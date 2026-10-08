"""Service module 36603: business logic, no crypto."""


def calculate_total_36603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36603():
    return 'module 36603 handles orders and invoices'
