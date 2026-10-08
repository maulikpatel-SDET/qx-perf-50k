"""Service module 5603: business logic, no crypto."""


def calculate_total_5603(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5603():
    return 'module 5603 handles orders and invoices'
