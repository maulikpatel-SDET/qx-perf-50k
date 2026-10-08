"""Service module 30603: business logic, no crypto."""


def calculate_total_30603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30603():
    return 'module 30603 handles orders and invoices'
