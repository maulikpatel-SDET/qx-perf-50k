"""Service module 46603: business logic, no crypto."""


def calculate_total_46603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46603():
    return 'module 46603 handles orders and invoices'
